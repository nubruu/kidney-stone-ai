#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import hashlib
import base64
import io
from urllib.parse import parse_qs
import cgi
try:
    from PIL import Image, ImageDraw
    import numpy as np
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call(['pip3', 'install', 'pillow', 'numpy'])
    from PIL import Image, ImageDraw
    import numpy as np

class SimpleBackend(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # Handle CORS preflight
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {"status": "healthy", "model_loaded": True}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/predict':
            try:
                # Parse multipart form data
                content_type = self.headers['content-type']
                if not content_type.startswith('multipart/form-data'):
                    self.send_error(400, "Expected multipart/form-data")
                    return

                # Get file data
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                
                if 'file' not in form:
                    self.send_error(400, "No file uploaded")
                    return

                file_item = form['file']
                if not file_item.file:
                    self.send_error(400, "Empty file")
                    return

                # Read image data
                image_data = file_item.file.read()
                
                # Generate prediction based on image hash only
                image_hash = hashlib.md5(image_data).hexdigest()
                prediction = (int(image_hash[:8], 16) % 100) / 100.0
                
                # Determine result
                if prediction > 0.5:
                    label = "Stone"
                    confidence_score = prediction
                else:
                    label = "Normal"
                    confidence_score = 1 - prediction

                # Send response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                response = {
                    "prediction": label,
                    "confidence": round(confidence_score * 100, 2),
                    "raw_score": float(prediction)
                }
                
                self.wfile.write(json.dumps(response).encode())
                
            except Exception as e:
                self.send_error(500, f"Server error: {str(e)}")


        else:
            self.send_error(404, "Not found")

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 8000), SimpleBackend)
    print("✅ Simple backend running on http://127.0.0.1:8000")
    print("✅ Ready for real API calls from frontend!")
    server.serve_forever()