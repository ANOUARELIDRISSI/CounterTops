from flask import Flask, render_template, request, jsonify, Response
import cv2
import numpy as np
import openvino as ov
import json
import base64
from pathlib import Path

app = Flask(__name__)

# Load OpenVINO model
class MarbleDetector:
    def __init__(self, model_path="model"):
        self.core = ov.Core()
        model_xml = Path(model_path) / "saved_model.xml"
        model_bin = Path(model_path) / "saved_model.bin"
        
        self.model = self.core.read_model(model=str(model_xml))
        self.compiled_model = self.core.compile_model(model=self.model, device_name="CPU")
        
        self.input_layer = self.compiled_model.input(0)
        self.output_layer = self.compiled_model.output(0)
        
        # Load class names
        with open("dm.json", "r") as f:
            self.classes = json.load(f)
    
    def preprocess_image(self, image):
        """Preprocess image for LandingLens model input with ImageNet normalization"""
        # LandingLens models expect 640x640 input
        h, w = 640, 640
        
        # Resize image
        resized = cv2.resize(image, (w, h))
        
        # Convert BGR to RGB
        resized_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        
        # Apply ImageNet standardization (mean and std normalization)
        # This is what LandingLens models expect
        mean = np.array([123.675, 116.28, 103.53], dtype=np.float32)
        std = np.array([58.395, 57.12, 57.375], dtype=np.float32)
        
        input_image = resized_rgb.astype(np.float32)
        input_image = (input_image - mean) / std
        
        # Transpose to (C, H, W) and add batch dimension
        input_image = input_image.transpose((2, 0, 1))
        input_image = np.expand_dims(input_image, 0)
        
        return input_image
    
    def detect(self, image):
        """Run detection on image using LandingLens model"""
        input_image = self.preprocess_image(image)
        
        # Run inference
        result = self.compiled_model([input_image])
        
        # LandingLens outputs: 'dets' [batch, num_detections, 5] and 'labels' [batch, num_detections]
        # dets format: [x_min, y_min, x_max, y_max, confidence] in 640x640 space
        dets_output = None
        labels_output = None
        
        for output_name, output_data in result.items():
            if 'dets' in str(output_name) or len(output_data.shape) == 3:
                dets_output = output_data
            elif 'labels' in str(output_name) or len(output_data.shape) == 2:
                labels_output = output_data
        
        if dets_output is None:
            return []
        
        # Parse detections
        detections = []
        has_fracture = False
        orig_h, orig_w = image.shape[:2]
        model_size = 640  # LandingLens model input size
        
        # Calculate scaling factors
        scale_x = orig_w / model_size
        scale_y = orig_h / model_size
        
        for i, det in enumerate(dets_output[0]):
            confidence = float(det[4])
            
            if confidence > 0.15:  # Confidence threshold
                # Get label
                class_id = int(labels_output[0][i]) if labels_output is not None else 0
                
                # Coordinates are in 640x640 space, scale to original image
                xmin = int(det[0] * scale_x)
                ymin = int(det[1] * scale_y)
                xmax = int(det[2] * scale_x)
                ymax = int(det[3] * scale_y)
                
                # Clip to image bounds
                xmin = max(0, min(xmin, orig_w))
                ymin = max(0, min(ymin, orig_h))
                xmax = max(0, min(xmax, orig_w))
                ymax = max(0, min(ymax, orig_h))
                
                # Skip invalid boxes
                if xmax <= xmin or ymax <= ymin:
                    continue
                
                class_name = self.classes.get(str(class_id), {}).get("name", "Unknown")
                
                # Only add fracture defects to detections list
                if class_name == "Fracture_Defect":
                    has_fracture = True
                    detections.append({
                        "class_id": class_id,
                        "class_name": class_name,
                        "confidence": confidence,
                        "bbox": [xmin, ymin, xmax, ymax]
                    })
        
        # If no fractures detected, return Normal Surface classification
        if not has_fracture:
            detections.append({
                "class_id": -1,
                "class_name": "Normal_Surface",
                "confidence": 1.0,
                "bbox": None
            })
        
        return detections
    
    def draw_detections(self, image, detections):
        """Draw bounding boxes only for fracture defects"""
        # Red color for fractures
        fracture_color = (0, 0, 255)  # Bright Red
        
        for det in detections:
            # Skip if no bbox (Normal Surface classification)
            if det["bbox"] is None:
                continue
                
            class_name = det["class_name"]
            
            # Only draw fracture defects
            if class_name == "Fracture_Defect":
                xmin, ymin, xmax, ymax = det["bbox"]
                confidence = det["confidence"]
                
                # Draw thicker rectangle with shadow effect
                # Shadow
                cv2.rectangle(image, (xmin+2, ymin+2), (xmax+2, ymax+2), (0, 0, 0), 6)
                # Main box - much thicker
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), fracture_color, 5)
                
                # Draw label with larger font
                label = f"Fracture: {int(confidence * 100)}%"
                font_scale = 0.8
                font_thickness = 2
                label_size, baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_DUPLEX, font_scale, font_thickness)
                
                # Label background with padding
                padding = 8
                label_ymin = max(ymin - label_size[1] - padding * 2, 0)
                
                # Shadow for label
                cv2.rectangle(image, 
                             (xmin + 2, label_ymin + 2), 
                             (xmin + label_size[0] + padding * 2 + 2, ymin + 2), 
                             (0, 0, 0), -1)
                
                # Label background
                cv2.rectangle(image, 
                             (xmin, label_ymin), 
                             (xmin + label_size[0] + padding * 2, ymin), 
                             fracture_color, -1)
                
                # Label text
                cv2.putText(image, label, 
                           (xmin + padding, ymin - padding), 
                           cv2.FONT_HERSHEY_DUPLEX, font_scale, (255, 255, 255), font_thickness)
        
        return image

# Initialize detector
detector = MarbleDetector()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    """Handle image upload and detection"""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    # Read image
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    if image is None:
        return jsonify({"error": "Invalid image file"}), 400
    
    # Run detection
    detections = detector.detect(image)
    
    # Draw detections
    result_image = detector.draw_detections(image.copy(), detections)
    
    # Encode result image to base64
    _, buffer = cv2.imencode('.jpg', result_image)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    
    return jsonify({
        "detections": detections,
        "image": f"data:image/jpeg;base64,{img_base64}",
        "total_defects": len([d for d in detections if d["class_name"] == "Fracture_Defect"])
    })

@app.route('/stream_frame', methods=['POST'])
def stream_frame():
    """Handle webcam frame detection"""
    data = request.json
    if 'frame' not in data:
        return jsonify({"error": "No frame data"}), 400
    
    # Decode base64 image
    img_data = base64.b64decode(data['frame'].split(',')[1])
    nparr = np.frombuffer(img_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if image is None:
        return jsonify({"error": "Invalid frame"}), 400
    
    # Run detection
    detections = detector.detect(image)
    
    # Draw detections
    result_image = detector.draw_detections(image.copy(), detections)
    
    # Encode result
    _, buffer = cv2.imencode('.jpg', result_image)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    
    return jsonify({
        "detections": detections,
        "image": f"data:image/jpeg;base64,{img_base64}",
        "total_defects": len([d for d in detections if d["class_name"] == "Fracture_Defect"])
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
