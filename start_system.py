#!/usr/bin/env python3
import subprocess
import time
import sys

def start_system():
    print("🏥 Starting Kidney Stone Detection System...")
    
    # Start backend
    print("🚀 Starting backend server...")
    backend = subprocess.Popen([sys.executable, "simple_backend.py"])
    
    # Wait for backend to start
    time.sleep(3)
    
    # Start Streamlit
    print("🖥️ Starting Streamlit GUI...")
    streamlit = subprocess.Popen(["/Users/subhajitbepari/Library/Python/3.9/bin/streamlit", "run", "streamlit_app.py"])
    
    print("✅ System started!")
    print("📱 GUI: http://localhost:8501")
    print("🔧 API: http://localhost:8000")
    print("Press Ctrl+C to stop both servers")
    
    try:
        backend.wait()
        streamlit.wait()
    except KeyboardInterrupt:
        print("\n🛑 Stopping servers...")
        backend.terminate()
        streamlit.terminate()
        print("✅ System stopped")

if __name__ == "__main__":
    start_system()