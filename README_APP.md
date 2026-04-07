# Marble Vision - Defect Detection Web App

AI-powered marble defect detection using OpenVINO, optimized for both PC browsers and mobile devices.

## Features

- **Upload & Analyze**: Upload marble images for instant defect detection
- **Live Camera**: Real-time detection using your device camera
- **Responsive Design**: Optimized UI for desktop, tablet, and mobile devices
- **Touch Support**: Full touch gesture support for mobile devices
- **Zoom & Pan**: Zoom into detection results with mouse/touch pan
- **Download Results**: Save annotated images with detections

## Model Information

- **Model**: model_marbles2 (OpenVINO IR format)
- **Classes**: 
  - OK (no defects)
  - Surface_Normal
  - Natural_Veining
  - Fracture_Defect
- **Input Size**: 640x640
- **Backend**: OpenVINO CPU inference

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask app:
```bash
python app.py
```

3. Open your browser:
- Desktop: http://localhost:5000
- Mobile: http://[your-ip]:5000

## Usage

### Upload Mode
1. Click "Upload image" tab
2. Drag & drop or click to browse for a marble image
3. View detection results with bounding boxes
4. Zoom, download, or upload another image

### Camera Mode
1. Click "Live camera" tab
2. Click "Start camera" and allow camera access
3. Point camera at marble surface
4. View real-time detections (updates every 500ms)

## Mobile Optimization

The UI is fully responsive with:
- Adaptive layouts for different screen sizes
- Touch gestures for zoom and pan
- Mobile-friendly camera access (uses back camera)
- Optimized button sizes and spacing
- Collapsible side panel on smaller screens

## Responsive Breakpoints

- **Desktop**: > 900px (side-by-side layout)
- **Tablet**: 600px - 900px (stacked layout)
- **Mobile**: < 600px (compact UI)
- **Small Mobile**: < 400px (minimal UI)

## Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari (iOS/macOS)
- Mobile browsers with camera support

## API Endpoints

### POST /upload
Upload an image file for detection.

**Request**: multipart/form-data with 'file' field

**Response**:
```json
{
  "detections": [
    {
      "class_id": 3,
      "class_name": "Fracture_Defect",
      "confidence": 0.95,
      "bbox": [100, 150, 300, 400]
    }
  ],
  "image": "data:image/jpeg;base64,...",
  "total_defects": 1
}
```

### POST /stream_frame
Process a single webcam frame.

**Request**:
```json
{
  "frame": "data:image/jpeg;base64,..."
}
```

**Response**: Same as /upload

## Performance

- Inference time: ~100-300ms per image (CPU)
- Camera stream: 2 FPS (500ms interval)
- Supports images up to 4K resolution

## Configuration

### Detection Threshold
Adjust confidence threshold in `app.py`:
```python
if confidence > 0.15:  # Change this value (0.0 - 1.0)
```

### Stream Processing Rate
Adjust frame processing interval in `index.html`:
```javascript
setTimeout(loop, 500); // Change milliseconds
```

## Troubleshooting

**Model not loading:**
- Verify model files exist in `model/` directory
- Check OpenVINO installation: `python -c "import openvino"`

**Camera not working:**
- Ensure HTTPS or localhost (WebRTC requirement)
- Grant camera permissions in browser
- Check if camera is already in use

**Mobile issues:**
- Use HTTPS for camera access on mobile
- Ensure browser supports getUserMedia API
- Check camera permissions in device settings

## License

For demonstration and evaluation purposes.
