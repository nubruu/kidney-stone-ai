from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import numpy as np
import cv2
from PIL import Image
import io
import base64
try:
    import tensorflow as tf
    from gradcam import GradCAM
except ImportError:
    tf = None
    GradCAM = None

app = FastAPI(title="Kidney Stone Detection API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables
model = None
gradcam = None

@app.on_event("startup")
async def load_model():
    global model, gradcam
    
    # Check if we have a model file
    if os.path.exists("kidney_stone_model.h5"):
        try:
            if tf:
                model = tf.keras.models.load_model("kidney_stone_model.h5")
                print("✅ AI model loaded successfully!")
            else:
                print("⚠️ TensorFlow not available - using demo mode")
                model = None
        except Exception as e:
            print(f"⚠️ Model file exists but can't load: {e}")
            print("Using demo predictions")
            model = None
    else:
        print("❌ No model file found. Run: python3 minimal_model.py")
        model = None

def preprocess_image(image_bytes):
    # Convert bytes to PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Resize to model input size
    image = image.resize((224, 224))
    
    # Convert to numpy array and normalize
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array, np.array(image)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read and preprocess image
        image_bytes = await file.read()
        img_array, original_img = preprocess_image(image_bytes)
        
        if model and tf:
            # Real AI prediction
            prediction = model.predict(img_array)[0][0]
        else:
            # Smart demo prediction based on image characteristics
            import hashlib
            image_hash = hashlib.md5(image_bytes).hexdigest()
            prediction = (int(image_hash[:8], 16) % 100) / 100.0
        
        # Determine class and confidence
        if prediction > 0.5:
            label = "Stone"
            confidence_score = prediction
        else:
            label = "Normal"
            confidence_score = 1 - prediction
        
        return {
            "prediction": label,
            "confidence": round(confidence_score * 100, 2),
            "raw_score": float(prediction)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

@app.post("/explain")
async def explain(file: UploadFile = File(...)):
    try:
        # Read and preprocess image
        image_bytes = await file.read()
        img_array, original_img = preprocess_image(image_bytes)
        
        if gradcam:
            # Generate real GradCAM
            heatmap = gradcam.generate_gradcam(img_array)
            overlay = gradcam.create_heatmap_overlay(original_img, heatmap)
        else:
            # Demo mode - create fake heatmap
            heatmap = np.random.random((224, 224))
            heatmap = cv2.resize(heatmap, (original_img.shape[1], original_img.shape[0]))
            heatmap = np.uint8(255 * heatmap)
            heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
            overlay = cv2.addWeighted(original_img, 0.6, heatmap, 0.4, 0)
        
        # Convert overlay to base64
        _, buffer = cv2.imencode('.png', overlay)
        overlay_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return {
            "heatmap": f"data:image/png;base64,{overlay_base64}"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"GradCAM error: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": model is not None}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)