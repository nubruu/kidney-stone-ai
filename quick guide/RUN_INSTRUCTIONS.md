# KidneyAI Pro - Setup Instructions

I've written this guide to help you get the kidney stone detection system running on your computer. Follow the steps below for your operating system.

## macOS Setup

### Step 1: Install Node.js
You have two options here:

**Option A: Download from the website**
- Go to https://nodejs.org/
- Download and install the LTS version

**Option B: Use Homebrew (if you have it)**
```bash
brew install node
```

Check if it installed correctly:
```bash
node --version
npm --version
```

### Step 2: Navigate to the project folder
Open Terminal (press Cmd + Space, then type "Terminal") and run:
```bash
cd /Users/[YOUR_USERNAME]/Desktop/kdstdt/react-frontend
```
Replace [YOUR_USERNAME] with your actual username.

### Step 3: Install the required packages
This will download all the libraries the project needs:
```bash
npm install
```

### Step 4: Start the application
This command starts the development server:
```bash
npm run dev
```

### Step 5: Access the Application (Mac)
- Open your web browser
- Go to: **http://localhost:3000**
- You should see the KidneyAI Pro interface

### Step 6: Start Backend - Optional (Mac)
```bash
# Open a new terminal window (Cmd + T)
cd /Users/[YOUR_USERNAME]/Desktop/kdstdt

# Start the Python backend
python3 simple_backend.py
```

---

## 🪟 Windows Setup Guide

### Step 1: Install Node.js on Windows
```cmd
# Download from official website
# Go to: https://nodejs.org/
# Download Windows Installer (.msi)
# Run the installer and follow setup wizard

# Verify installation (open Command Prompt)
node --version
npm --version
```

### Step 2: Navigate to Project (Windows)
```cmd
# Open Command Prompt (Win + R, type "cmd")
cd C:\Users\[YOUR_USERNAME]\Desktop\kdstdt\react-frontend
```

### Step 3: Install Dependencies (Windows)
```cmd
# Install all required packages
npm install
```

### Step 4: Start Frontend Application (Windows)
```cmd
# Start the React development server
npm run dev
```

### Step 5: Access the Application (Windows)
- Open your web browser
- Go to: **http://localhost:3000**
- You should see the KidneyAI Pro interface

### Step 6: Start Backend - Optional (Windows)
```cmd
# Open a new Command Prompt window
cd C:\Users\[YOUR_USERNAME]\Desktop\kdstdt

# Start the Python backend
python simple_backend.py
```

## 🎯 What You'll See

1. **Upload Scan Page** - Drag & drop medical images
2. **About Page** - System information and medical disclaimer
3. **Dark Mode Toggle** - Switch between light/dark themes
4. **Professional Medical UI** - Healthcare-focused design

## 🔧 Troubleshooting

### Mac Troubleshooting
```bash
# If npm install fails
npm cache clean --force
npm install

# If port 3000 is busy
lsof -ti:3000 | xargs kill -9
npm run dev -- --port 3001

# If permission errors
sudo chown -R $(whoami) ~/.npm
```

### Windows Troubleshooting
```cmd
# If npm install fails
npm cache clean --force
npm install

# If port 3000 is busy
netstat -ano | findstr :3000
taskkill /PID [PID_NUMBER] /F
npm run dev -- --port 3001

# If permission errors
# Run Command Prompt as Administrator
```

## ✅ Success Indicators

- ✅ Terminal shows: "Local: http://localhost:3000"
- ✅ Browser opens automatically
- ✅ You see "KidneyAI Pro" interface
- ✅ Upload Scan and About pages work
- ✅ Dark mode toggle functions

## 📱 Features Available

- **Upload Medical Images** - PNG, JPG, JPEG support
- **AI Analysis** - Mock kidney stone detection
- **Confidence Scoring** - Circular progress indicators
- **Grad-CAM Heatmaps** - AI explainability with visual focus areas
- **Dark Mode** - Professional theme switching
- **Responsive Design** - Works on all screen sizes

## 🔥 Grad-CAM Heatmap Details

**What is Grad-CAM?**
- **Gradient-weighted Class Activation Mapping**
- Shows which parts of the image the AI focused on
- Red/warm colors = high attention areas
- Blue/cool colors = low attention areas

**How to Use:**
1. Upload a kidney scan image
2. Click "Analyze Image" to get prediction
3. Click "View Heatmap" to see AI focus areas
4. Heatmap opens in new window showing overlay

**What the Colors Mean:**
- 🔴 **Red/Orange** - AI detected important features here
- 🟡 **Yellow** - Moderate attention from AI
- 🟢 **Green** - Some relevance to decision
- 🔵 **Blue** - Low importance for classification

**Medical Interpretation:**
- Bright areas show potential stone locations
- Helps doctors understand AI reasoning
- Validates AI decision-making process
- Assists in medical education and training

## 🚀 Production Build

```bash
# Build for production
npm run build

# Preview production build
npm run preview
```

---

**🎉 You're all set! The KidneyAI Pro application is now running on your Mac.**