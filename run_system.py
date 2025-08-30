#!/usr/bin/env python3
"""
Kidney Stone Detection System Runner
Automates the complete workflow: training, backend, and GUI
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*50}")
    print(f"🚀 {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def check_model_exists():
    """Check if trained model exists"""
    model_files = [
        "best_kidney_stone_model_efficientnet.h5",
        "best_kidney_stone_model_resnet50.h5"
    ]
    return any(os.path.exists(f) for f in model_files)

def main():
    print("🏥 Kidney Stone Detection System")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("Kidney Ultrasound Images Stone and No Stone"):
        print("❌ Dataset folder not found!")
        print("Please ensure you're in the correct directory with the dataset.")
        return
    
    # Menu
    print("\nSelect an option:")
    print("1. 🎯 Train Models (EfficientNetB0 & ResNet50)")
    print("2. 🚀 Start Backend Server")
    print("3. 🖥️  Launch Streamlit GUI")
    print("4. 🔄 Complete Workflow (Train → Backend → GUI)")
    print("5. 📊 Quick Demo (Backend → GUI)")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        # Train models
        if not run_command("python train_model.py", "Training AI Models"):
            return
            
    elif choice == "2":
        # Start backend
        if not check_model_exists():
            print("❌ No trained model found! Please train models first (option 1).")
            return
        
        print("🚀 Starting FastAPI backend server...")
        print("Backend will be available at: http://localhost:8000")
        print("Press Ctrl+C to stop the server")
        
        try:
            subprocess.run("python backend.py", shell=True)
        except KeyboardInterrupt:
            print("\n🛑 Backend server stopped.")
            
    elif choice == "3":
        # Launch GUI
        print("🖥️ Launching Streamlit GUI...")
        print("GUI will open in your browser at: http://localhost:8501")
        print("Press Ctrl+C to stop the GUI")
        
        try:
            subprocess.run("streamlit run streamlit_app.py", shell=True)
        except KeyboardInterrupt:
            print("\n🛑 Streamlit GUI stopped.")
            
    elif choice == "4":
        # Complete workflow
        print("🔄 Starting complete workflow...")
        
        # Step 1: Train models
        if not run_command("python train_model.py", "Training AI Models"):
            return
        
        print("\n✅ Training completed! Now you can:")
        print("1. Run 'python backend.py' in one terminal")
        print("2. Run 'streamlit run streamlit_app.py' in another terminal")
        print("\nOr use option 5 for quick demo setup.")
        
    elif choice == "5":
        # Quick demo
        if not check_model_exists():
            print("❌ No trained model found! Please train models first (option 1 or 4).")
            return
        
        print("📊 Setting up quick demo...")
        print("\n🚀 Starting backend server in background...")
        
        # Start backend in background
        backend_process = subprocess.Popen(
            ["python", "backend.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for backend to start
        time.sleep(3)
        
        print("🖥️ Launching Streamlit GUI...")
        print("Demo will open in your browser!")
        
        try:
            subprocess.run("streamlit run streamlit_app.py", shell=True)
        except KeyboardInterrupt:
            print("\n🛑 Stopping demo...")
        finally:
            backend_process.terminate()
            print("✅ Demo stopped.")
    
    else:
        print("❌ Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()