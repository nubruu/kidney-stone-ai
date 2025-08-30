# How to Train Your Own AI Model

I'll walk you through training your own kidney stone detection model from scratch. This process will create actual AI models instead of the demo version.

## What You'll Need First

Install these Python packages:
```bash
pip install tensorflow keras opencv-python numpy matplotlib scikit-learn pillow
```

## Organizing Your Images

Your medical images need to be organized like this:

```
Kidney Ultrasound Images Stone and No Stone/
├── Normal/          # Put healthy kidney scans here
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── stone/           # Put kidney stone images here
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

## Training Script

```python
import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0, ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
import os

# Data paths
DATASET_PATH = "Kidney Ultrasound Images Stone and No Stone"
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 20

# Data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

# Load data
train_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='training'
)

val_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    subset='validation'
)

# Build EfficientNetB0 model
def create_efficientnet_model():
    base_model = EfficientNetB0(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    base_model.trainable = False
    
    model = tf.keras.Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    
    return model

# Build ResNet50 model
def create_resnet_model():
    base_model = ResNet50(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    base_model.trainable = False
    
    model = tf.keras.Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dropout(0.3),
        Dense(128, activation='relu'),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])
    
    return model

# Train models
def train_model(model, model_name):
    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    history = model.fit(
        train_generator,
        epochs=EPOCHS,
        validation_data=val_generator,
        verbose=1
    )
    
    # Save model
    model.save(f'{model_name}_kidney_stone.h5')
    print(f"{model_name} model saved!")
    
    return history

# Train both models
if __name__ == "__main__":
    print("Training EfficientNetB0...")
    efficientnet_model = create_efficientnet_model()
    train_model(efficientnet_model, "efficientnet")
    
    print("Training ResNet50...")
    resnet_model = create_resnet_model()
    train_model(resnet_model, "resnet")
    
    print("Training completed!")
```

## Quick Training Steps

1. **Prepare Dataset**
```bash
# Ensure your dataset follows the required structure
# Place images in Normal/ and stone/ folders
```

2. **Run Training**
```bash
python train_model.py
```

3. **Models Generated**
- `efficientnet_kidney_stone.h5`
- `resnet_kidney_stone.h5`

## Model Evaluation

```python
# Evaluate model performance
from sklearn.metrics import classification_report, confusion_matrix

# Load test data
test_generator = train_datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    shuffle=False
)

# Evaluate
model = tf.keras.models.load_model('efficientnet_kidney_stone.h5')
predictions = model.predict(test_generator)
y_pred = (predictions > 0.5).astype(int)
y_true = test_generator.classes

print(classification_report(y_true, y_pred))
```

## Integration with Backend

```python
# Update backend.py to use trained model
import tensorflow as tf

# Load trained model
model = tf.keras.models.load_model('efficientnet_kidney_stone.h5')

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Preprocess image
    image = preprocess_image(file)
    
    # Make prediction
    prediction = model.predict(image)
    confidence = float(prediction[0][0])
    
    result = {
        "prediction": "Stone" if confidence > 0.5 else "Normal",
        "confidence": confidence * 100,
        "raw_score": confidence
    }
    
    return result
```

## Training Tips

- **Dataset Size**: Minimum 1000 images per class
- **Image Quality**: High resolution, clear scans
- **Data Balance**: Equal number of stone/normal images
- **Augmentation**: Helps with small datasets
- **Validation**: Always use separate validation set
- **Fine-tuning**: Unfreeze base model layers for better accuracy

## Expected Results

- **Training Time**: 30-60 minutes (depending on dataset size)
- **Accuracy**: 85-95% (with good dataset)
- **Model Size**: 20-50 MB per model

---

**Note**: This creates actual AI models that can replace the mock predictions in the frontend!