# Marble Fracture Detection

AI-powered marble defect detection system using OpenVINO. Detects fractures in marble surfaces with real-time camera support and responsive web interface.

![Status](https://img.shields.io/badge/status-ready%20to%20deploy-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![OpenVINO](https://img.shields.io/badge/OpenVINO-2026.0.0-orange)

## 🎯 Features

- **Binary Classification**: Fracture Defect vs Normal Surface
- **Smart Detection**: Only highlights problematic areas with red bounding boxes
- **Real-time Camera**: Live detection using webcam
- **Responsive UI**: Optimized for desktop, tablet, and mobile
- **Touch Support**: Full gesture support for mobile devices
- **Easy Deployment**: Ready for Vercel, Railway, or other platforms

## 🖼️ Detection Examples

| Input | Output |
|-------|--------|
| Marble with fractures | Red bounding boxes around defects |
| Normal marble surface | "Normal Surface" classification, no boxes |

## 🚀 Quick Start

### Local Development

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/marble-fracture-detection.git
cd marble-fracture-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Open browser
# http://localhost:5000
```

### Deploy to Vercel

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 📋 Detection Logic

The system uses a two-class approach:

1. **Fracture Defect** 🔴
   - Red bounding boxes drawn around detected fractures
   - Confidence score displayed
   - Each fracture counted separately

2. **Normal Surface** 🟢
   - No bounding boxes
   - Displayed when no fractures detected
   - Clean, unmarked image

The underlying model detects 4 classes internally, but post-processing filters to show only fractures. See [DETECTION_LOGIC.md](DETECTION_LOGIC.md) for details.

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **ML Framework**: OpenVINO 2026.0.0
- **Computer Vision**: OpenCV
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Vercel / Railway / Render

## 📦 Project Structure

```
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Web interface
├── model/                # OpenVINO model files
│   ├── saved_model.xml
│   ├── saved_model.bin
│   └── saved_model.onnx
├── dm.json               # Class definitions
├── meta.json             # Model metadata
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
└── README.md            # This file
```

## 🎨 UI Features

- **Fixed-size display**: Consistent layout regardless of image size
- **Responsive design**: Adapts to screen size
  - Desktop: 500px height
  - Tablet: 400px height
  - Mobile: 300px height
- **Touch gestures**: Zoom and pan on mobile
- **Camera support**: Uses back camera on mobile devices

## 📊 API Endpoints

### POST /upload
Upload an image for detection.

**Request**: `multipart/form-data` with image file

**Response**:
```json
{
  "detections": [
    {
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
Process webcam frame.

**Request**: JSON with base64 encoded frame

**Response**: Same as /upload

## ⚙️ Configuration

### Detection Threshold
Adjust in `app.py`:
```python
if confidence > 0.15:  # Change threshold (0.0 - 1.0)
```

### Camera Frame Rate
Adjust in `templates/index.html`:
```javascript
setTimeout(loop, 500);  // Change interval (milliseconds)
```

## 🚨 Deployment Notes

**Model Size**: 155.85 MB

**Platform Requirements**:
- ✅ Vercel Pro: 250MB limit ($20/month)
- ❌ Vercel Free: 100MB limit (too small)
- ✅ Railway: More generous limits
- ✅ Render: Supports large deployments

See [DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md) for platform comparison.

## 📱 Browser Compatibility

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari (iOS/macOS)
- ✅ Mobile browsers with camera support

## 🧪 Testing

```bash
# Test locally
python app.py

# Test with sample images
# 1. Upload image with fractures → Should show red boxes
# 2. Upload normal marble → Should show "Normal Surface"
# 3. Test camera → Should work with HTTPS
```

## 📚 Documentation

- [DEPLOYMENT.md](DEPLOYMENT.md) - Detailed deployment guide
- [DEPLOY_CHECKLIST.md](DEPLOY_CHECKLIST.md) - Quick deployment steps
- [DETECTION_LOGIC.md](DETECTION_LOGIC.md) - How detection works
- [README_APP.md](README_APP.md) - Application documentation

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

For demonstration and evaluation purposes.

## 🆘 Support

For issues or questions:
1. Check documentation files
2. Review deployment logs
3. Test locally first
4. Open an issue on GitHub

## 🎯 Roadmap

- [ ] Add batch processing
- [ ] Export detection reports
- [ ] Add severity levels
- [ ] Implement user authentication
- [ ] Add detection history
- [ ] Support multiple image formats

---

**Ready to deploy?** Check [DEPLOY_CHECKLIST.md](DEPLOY_CHECKLIST.md) to get started!
