import streamlit as st
import requests
import numpy as np
from PIL import Image
import io
import base64

# Page config
st.set_page_config(
    page_title="KidneyAI Pro",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --primary: #007AFF;
    --secondary: #34C759;
    --danger: #FF3B30;
    --warning: #FF9500;
    --surface: #FFFFFF;
    --background: #F2F2F7;
    --text-primary: #1D1D1F;
    --text-secondary: #86868B;
    --border: #D1D1D6;
    --shadow: 0 4px 20px rgba(0,0,0,0.08);
    --shadow-lg: 0 8px 40px rgba(0,0,0,0.12);
}

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Hide Streamlit elements */
.stAppToolbar, .stMainMenu, .stStatusWidget, .stDeployButton {
    display: none !important;
}

/* Navigation */
.nav-container {
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255,255,255,0.2);
    padding: 1rem 2rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    margin: -1rem -1rem 0 -1rem;
}

.nav-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

.logo {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.nav-links {
    display: flex;
    gap: 2rem;
    align-items: center;
}

.nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.2s;
}

.nav-link:hover {
    color: var(--primary);
}

/* Hero Section */
.hero {
    text-align: center;
    padding: 4rem 2rem;
    background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
    margin: 0 -1rem 3rem -1rem;
}

.hero h1 {
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(135deg, #FFFFFF 0%, rgba(255,255,255,0.8) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    letter-spacing: -0.02em;
}

.hero p {
    font-size: 1.25rem;
    color: rgba(255,255,255,0.8);
    max-width: 600px;
    margin: 0 auto 2rem auto;
    line-height: 1.6;
}

/* Cards */
.card {
    background: var(--surface);
    border-radius: 16px;
    padding: 2rem;
    box-shadow: var(--shadow);
    border: 1px solid var(--border);
    transition: all 0.3s ease;
    height: 100%;
}

.card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-2px);
}

.card-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.card-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
}

.card-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0;
}

/* Upload Area */
.upload-area {
    border: 2px dashed var(--border);
    border-radius: 16px;
    padding: 3rem;
    text-align: center;
    transition: all 0.3s ease;
    background: rgba(0,122,255,0.02);
}

.upload-area:hover {
    border-color: var(--primary);
    background: rgba(0,122,255,0.05);
}

/* Results */
.result-positive {
    background: linear-gradient(135deg, #FF3B30 0%, #FF6B6B 100%);
    color: white;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(255,59,48,0.3);
}

.result-negative {
    background: linear-gradient(135deg, #34C759 0%, #30D158 100%);
    color: white;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 8px 32px rgba(52,199,89,0.3);
}

.confidence-bar {
    background: rgba(255,255,255,0.2);
    border-radius: 8px;
    height: 8px;
    margin: 1rem 0;
    overflow: hidden;
}

.confidence-fill {
    height: 100%;
    background: white;
    border-radius: 8px;
    transition: width 0.8s ease;
}

/* Buttons */
.btn-primary {
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 1rem 2rem;
    font-weight: 600;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.btn-primary:hover {
    background: #0056CC;
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(0,122,255,0.3);
}

.btn-secondary {
    background: var(--surface);
    color: var(--text-primary);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem 2rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
}

.btn-secondary:hover {
    background: var(--background);
    border-color: var(--primary);
}

/* Status indicators */
.status-online {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--secondary);
    font-weight: 500;
}

.status-offline {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--danger);
    font-weight: 500;
}

.status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: currentColor;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

/* Footer */
.footer {
    background: var(--text-primary);
    color: white;
    padding: 3rem 2rem 2rem 2rem;
    margin: 4rem -1rem -1rem -1rem;
    text-align: center;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 2rem;
}

.footer-link {
    color: rgba(255,255,255,0.7);
    text-decoration: none;
    transition: color 0.2s;
}

.footer-link:hover {
    color: white;
}

/* Responsive */
@media (max-width: 768px) {
    .hero h1 { font-size: 2.5rem; }
    .nav-content { flex-direction: column; gap: 1rem; }
    .nav-links { gap: 1rem; }
    .footer-links { flex-direction: column; gap: 1rem; }
}
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="nav-container">
    <div class="nav-content">
        <div class="logo">
            🏥 KidneyAI Pro
        </div>
        <div class="nav-links">
            <a href="#" class="nav-link">Dashboard</a>
            <a href="#" class="nav-link">Analytics</a>
            <a href="#" class="nav-link">Reports</a>
            <a href="#" class="nav-link">Settings</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>AI-Powered Kidney Stone Detection</h1>
    <p>Advanced medical imaging analysis using state-of-the-art deep learning models. Get instant, accurate results with confidence scoring and visual explanations.</p>
</div>
""", unsafe_allow_html=True)

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000"

def check_backend():
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=2)
        return response.status_code == 200
    except:
        return False

# Main Content
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <div class="card-icon" style="background: rgba(0,122,255,0.1); color: var(--primary);">
                📤
            </div>
            <h2 class="card-title">Upload Medical Image</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Backend status
    backend_status = check_backend()
    if backend_status:
        st.markdown('<div class="status-online"><div class="status-dot"></div>AI System Online</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-offline"><div class="status-dot"></div>AI System Offline</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader(
        "Select kidney ultrasound or CT scan image",
        type=['png', 'jpg', 'jpeg'],
        help="Supported formats: PNG, JPG, JPEG (Max 10MB)"
    )
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="📋 Medical Image Preview", use_container_width=True)
        
        if backend_status:
            if st.button("🔬 Analyze Image", key="analyze", help="Start AI analysis"):
                with st.spinner("🧠 AI is analyzing the image..."):
                    try:
                        img_bytes = io.BytesIO()
                        image.save(img_bytes, format='PNG')
                        img_bytes.seek(0)
                        
                        files = {"file": ("image.png", img_bytes, "image/png")}
                        response = requests.post(f"{BACKEND_URL}/predict", files=files)
                        
                        if response.status_code == 200:
                            result = response.json()
                            st.session_state.prediction_result = result
                            st.session_state.uploaded_image = uploaded_file
                            st.success("✅ Analysis completed successfully!")
                        else:
                            st.error("❌ Analysis failed. Please try again.")
                    except Exception as e:
                        st.error(f"❌ Error: {str(e)}")
        else:
            st.warning("⚠️ Please start the backend server: `python3 simple_backend.py`")
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <div class="card-icon" style="background: rgba(52,199,89,0.1); color: var(--secondary);">
                📊
            </div>
            <h2 class="card-title">Analysis Results</h2>
        </div>
    """, unsafe_allow_html=True)
    
    if hasattr(st.session_state, 'prediction_result'):
        result = st.session_state.prediction_result
        
        if result['prediction'] == 'Stone':
            st.markdown(f"""
            <div class="result-positive">
                <h2 style="font-size: 2rem; margin-bottom: 1rem;">⚠️ Kidney Stone Detected</h2>
                <div style="font-size: 3rem; font-weight: 700; margin: 1rem 0;">{result['confidence']:.1f}%</div>
                <div class="confidence-bar">
                    <div class="confidence-fill" style="width: {result['confidence']}%;"></div>
                </div>
                <p style="margin: 1rem 0 0 0; opacity: 0.9;">High confidence detection. Recommend immediate medical consultation.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-negative">
                <h2 style="font-size: 2rem; margin-bottom: 1rem;">✅ No Kidney Stone Detected</h2>
                <div style="font-size: 3rem; font-weight: 700; margin: 1rem 0;">{result['confidence']:.1f}%</div>
                <div class="confidence-bar">
                    <div class="confidence-fill" style="width: {result['confidence']}%;"></div>
                </div>
                <p style="margin: 1rem 0 0 0; opacity: 0.9;">Normal kidney structure detected. Continue regular health monitoring.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Grad-CAM Section
        if st.button("🔍 Generate AI Explanation", key="gradcam"):
            with st.spinner("🎨 Generating visual explanation..."):
                try:
                    img_bytes = io.BytesIO()
                    image = Image.open(st.session_state.uploaded_image)
                    image.save(img_bytes, format='PNG')
                    img_bytes.seek(0)
                    
                    files = {"file": ("image.png", img_bytes, "image/png")}
                    response = requests.post(f"{BACKEND_URL}/explain", files=files)
                    
                    if response.status_code == 200:
                        gradcam_result = response.json()
                        st.image(gradcam_result['heatmap'], caption="🔥 AI Focus Areas (Grad-CAM)", use_container_width=True)
                        st.info("🎯 Red/warm areas show where the AI focused its attention for the diagnosis.")
                    else:
                        st.error("❌ Failed to generate explanation")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
    else:
        st.markdown("""
        <div style="text-align: center; padding: 4rem 2rem; color: var(--text-secondary);">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔬</div>
            <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Ready for Analysis</h3>
            <p>Upload a medical image to begin AI-powered kidney stone detection</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Features Section
st.markdown("<br><br>", unsafe_allow_html=True)

feat_col1, feat_col2, feat_col3 = st.columns(3)

with feat_col1:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🧠</div>
        <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Advanced AI</h3>
        <p style="color: var(--text-secondary);">State-of-the-art deep learning models trained on thousands of medical images</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col2:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">⚡</div>
        <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Instant Results</h3>
        <p style="color: var(--text-secondary);">Get accurate diagnosis in seconds with confidence scoring and explanations</p>
    </div>
    """, unsafe_allow_html=True)

with feat_col3:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🔒</div>
        <h3 style="color: var(--text-primary); margin-bottom: 1rem;">Secure & Private</h3>
        <p style="color: var(--text-secondary);">Your medical data is processed securely and never stored permanently</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <div class="footer-links">
            <a href="#" class="footer-link">Privacy Policy</a>
            <a href="#" class="footer-link">Terms of Service</a>
            <a href="#" class="footer-link">Medical Disclaimer</a>
            <a href="#" class="footer-link">Support</a>
        </div>
        <p style="color: rgba(255,255,255,0.6); margin: 0;">
            ⚠️ This AI system is for educational and research purposes only. Always consult qualified medical professionals for diagnosis and treatment.
        </p>
        <br>
        <p style="color: rgba(255,255,255,0.4); margin: 0; font-size: 0.9rem;">
            © 2024 KidneyAI Pro. Built with advanced machine learning for medical imaging.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)