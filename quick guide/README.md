# AI-Based Kidney Stone Detection System

This project implements an AI-powered system for detecting kidney stones in medical images. I built this using deep learning models (EfficientNetB0 and ResNet50) with transfer learning, along with a modern web interface and API backend.

## Getting Started

To run this system on your machine:

1. **Install the required packages**
```bash
pip3 install -r requirements.txt
```

2. **Start the application**
```bash
python3 run_system.py
```

## 📁 Project Structure

```
kdstdt/
├── Kidney Ultrasound Images Stone and No Stone/  # Dataset
│   ├── Normal/                                   # Normal kidney images
│   └── stone/                                    # Kidney stone images
├── train_model.py                                # Model training script
├── gradcam.py                                    # Grad-CAM implementation
├── backend.py                                    # FastAPI backend
├── streamlit_app.py                              # Streamlit GUI
├── run_system.py                                 # System runner
├── requirements.txt                              # Dependencies
└── README.md                                     # This file
```

## 🎯 Features

### 🤖 AI Models
- **EfficientNetB0** and **ResNet50** with transfer learning
- Binary classification: Stone vs Normal
- Data augmentation and preprocessing
- Model comparison and best model selection

### 📊 Evaluation Metrics
- Accuracy, Precision, Recall, F1-score
- ROC-AUC curve
- Confusion matrix visualization

### 🔍 Explainable AI
- **Grad-CAM** heatmap visualization
- Shows which regions the AI focused on for decisions

### 🌐 Backend API
- **FastAPI** with two endpoints:
  - `/predict` - Image classification
  - `/explain` - Grad-CAM heatmap generation

### 🖥️ User Interface
- **Streamlit** web application
- Image upload and preview
- Real-time prediction with confidence scores
- Grad-CAM visualization overlay

## 📋 Usage Instructions

### Option 1: Complete Workflow
```bash
python3 run_system.py
# Select option 4 for complete workflow
```

### Option 2: Step by Step

1. **Train Models**
```bash
python3 train_model.py
```

2. **Start Backend** (in terminal 1)
```bash
python3 backend.py
```

3. **Launch GUI** (in terminal 2)
```bash
streamlit run streamlit_app.py
```

### Option 3: Quick Demo
```bash
python3 run_system.py
# Select option 5 for quick demo
```

## 🔧 API Endpoints

### Prediction Endpoint
```
POST /predict
Content-Type: multipart/form-data
Body: image file

Response:
{
  "prediction": "Stone" | "Normal",
  "confidence": 92.5,
  "raw_score": 0.925
}
```

### Explanation Endpoint
```
POST /explain
Content-Type: multipart/form-data
Body: image file

Response:
{
  "heatmap": "data:image/png;base64,..."
}
```

## 📈 Model Performance

The system compares two models:
- **EfficientNetB0**: Lightweight, efficient
- **ResNet50**: Deep residual network

Best performing model is automatically saved and used for inference.

## 🎨 GUI Features

- **Image Upload**: Drag & drop or browse
- **Real-time Analysis**: Instant predictions
- **Confidence Visualization**: Progress bars and percentages
- **Grad-CAM Heatmaps**: Visual explanations
- **Professional UI**: Clean, medical-themed interface

## ⚠️ Important Notes

- **Medical Disclaimer**: This system is for educational purposes only
- **Dataset**: Ensure proper dataset structure with Normal/Stone folders
- **Model Training**: First run requires training (20-30 minutes)
- **Dependencies**: All required packages in requirements.txt

## 🔍 Troubleshooting

### Model Not Found Error
```bash
# Train models first
python3 train_model.py
```

### Backend Connection Error
```bash
# Ensure backend is running
python3 backend.py
# Check http://localhost:8000/health
```

### Dataset Path Error
```bash
# Verify dataset folder structure:
# Kidney Ultrasound Images Stone and No Stone/
#   ├── Normal/
#   └── stone/
```

## 🏆 Results Display

### Positive Detection
```
⚠️ Kidney Stone Detected
Confidence: 92.3%
```

### Negative Detection
```
✅ No Kidney Stone Detected  
Confidence: 87.6%
```

## 🚀 Next Steps

1. **Model Improvement**: Add more data, try other architectures
2. **Deployment**: Docker containerization, cloud deployment
3. **Features**: Multi-class classification, size estimation
4. **Integration**: DICOM support, hospital system integration

---

**Built with ❤️ for medical AI applications**