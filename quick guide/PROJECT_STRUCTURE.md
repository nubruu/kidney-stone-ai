# KidneyAI Pro - Project Structure

Here's how I organized all the files in this kidney stone detection project. This should help you understand what each file does and where to find things.

```
kdstdt/
├── Kidney Ultrasound Images Stone and No Stone/    # Medical image dataset
│   ├── Normal/                                     # Healthy kidney scans
│   │   ├── normal_001.jpg
│   │   ├── normal_002.jpg
│   │   └── ...
│   └── stone/                                      # Images showing kidney stones
│       ├── stone_001.jpg
│       ├── stone_002.jpg
│       └── ...
│
├── react-frontend/                                 # Modern web interface
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx                          # Top navigation bar
│   │   │   └── Sidebar.jsx                         # Left sidebar menu
│   │   ├── pages/
│   │   │   ├── Upload.jsx                          # Main page for uploading images
│   │   │   └── About.jsx                           # Information about the system
│   │   ├── App.jsx                                 # Main React application
│   │   ├── main.jsx                                # Application entry point
│   │   └── index.css                               # Styling with Tailwind CSS
│   ├── package.json                                # Project dependencies
│   ├── tailwind.config.js                         # UI styling configuration
│   ├── vite.config.js                             # Build tool settings
│   └── postcss.config.js                          # CSS processing config
│
├── 📄 streamlit_app.py                                # Streamlit GUI (Alternative)
├── 📄 backend.py                                      # FastAPI backend server
├── 📄 train_model.py                                  # Model training script
├── 📄 gradcam.py                                      # Grad-CAM implementation
├── 📄 run_system.py                                   # System runner script
├── 📄 requirements.txt                                # Python dependencies
├── 📄 README.md                                       # Main project documentation
├── 📄 RUN_INSTRUCTIONS.md                             # Setup instructions
├── 📄 MODEL_TRAINING_GUIDE.md                         # Model training guide
└── 📄 PROJECT_STRUCTURE.md                            # This file
```

## What Each File Does

### Main Application Files

Let me explain what the important files do:

| File | What it does | Built with |
|------|-------------|------------|
| `react-frontend/` | The main web interface users see | React + Tailwind CSS |
| `streamlit_app.py` | A simpler alternative interface | Streamlit |
| `backend.py` | Handles AI predictions and API calls | FastAPI |
| `train_model.py` | Creates and trains the AI models | TensorFlow/Keras |
| `gradcam.py` | Shows which parts of images the AI focuses on | Grad-CAM |

### 🔧 Configuration Files

| File | Purpose |
|------|---------|
| `package.json` | React dependencies |
| `tailwind.config.js` | UI styling configuration |
| `vite.config.js` | Build tool configuration |
| `requirements.txt` | Python dependencies |

### 📚 Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Project overview |
| `RUN_INSTRUCTIONS.md` | Setup guide for Mac/Windows |
| `MODEL_TRAINING_GUIDE.md` | AI training instructions |
| `PROJECT_STRUCTURE.md` | This file structure guide |

### 🖼️ Data Files

| Directory | Contents |
|-----------|----------|
| `Normal/` | Healthy kidney scan images |
| `stone/` | Kidney stone scan images |

## How to Run Different Parts

### To start the main web interface:
```bash
cd react-frontend
npm install
npm run dev
```

### To start the API server:
```bash
python3 backend.py
```

### To use the simple Streamlit interface:
```bash
streamlit run streamlit_app.py
```

### To train your own AI models:
```bash
python3 train_model.py
```

## 🌐 Application URLs

- **React Frontend**: http://localhost:3000
- **Streamlit GUI**: http://localhost:8501
- **FastAPI Backend**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📱 Features by File

### React Frontend (`react-frontend/`)
- Professional medical UI
- Drag & drop image upload
- Real-time AI analysis
- Circular progress indicators
- Dark mode support
- Responsive design
- Grad-CAM heatmap viewer
- PDF report generation

### Streamlit GUI (`streamlit_app.py`)
- Simple web interface
- Image upload and preview
- Basic prediction display
- Confidence visualization

### Backend API (`backend.py`)
- `/predict` - Image classification
- `/explain` - Grad-CAM generation
- `/health` - Server status
- File upload handling
- CORS support

### Training System (`train_model.py`)
- EfficientNetB0 model
- ResNet50 model
- Transfer learning
- Data augmentation
- Model comparison
- Performance metrics

## How the System Works

Here's what happens when someone uses the system:

```
1. User uploads a medical image → React Frontend
2. Frontend sends image to → FastAPI Backend
3. Backend runs it through → AI Model
4. Model returns → Prediction + Confidence Score
5. Backend creates → Grad-CAM heatmap
6. Frontend shows → Results + Visual Explanation
7. User can download → Professional Medical Report
```

## 🛠️ Development Workflow

1. **Setup**: Follow `RUN_INSTRUCTIONS.md`
2. **Train Models**: Use `MODEL_TRAINING_GUIDE.md`
3. **Start Backend**: `python3 backend.py`
4. **Start Frontend**: `npm run dev`
5. **Test**: Upload images and verify results
6. **Deploy**: Build production versions

---

**Total Files**: 20+ files organized in a professional medical AI application structure