# Marble Fracture Detection

AI-powered marble defect detection system using OpenVINO. Detects fractures in marble surfaces with real-time camera support and responsive web interface.

![Status](https://img.shields.io/badge/status-deployed-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![OpenVINO](https://img.shields.io/badge/OpenVINO-2026.0.0-orange)

## 🎯 Features

- **Binary Classification**: Fracture Defect vs Normal Surface
- **Smart Detection**: Only highlights fractures with red bounding boxes
- **Real-time Camera**: Live detection using webcam
- **Responsive UI**: Optimized for desktop, tablet, and mobile
- **Touch Support**: Full gesture support for mobile devices

## 🚀 Quick Deploy

### Option 1: Render.com (Recommended - Free)
1. Go to https://render.com
2. Sign up with GitHub
3. Create "Web Service" from this repo
4. Build: `pip install -r requirements.txt`
5. Start: `python app.py`
6. Deploy! (Free tier, sleeps after 15 min)

**Detailed guide**: See DEPLOY_RENDER.md in repo

### Option 2: Railway.app (Free $5 credit)
1. Go to https://railway.app
2. Deploy from GitHub repo
3. Auto-detects and deploys
4. No sleep mode!

## 🖼️ How It Works

| Input | Output |
|-------|--------|
| Marble with fractures | Red bounding boxes around defects |
| Normal marble surface | "Normal Surface" classification, no boxes |

## 🛠️ Local Development

```bash
# Clone repository
git clone https://github.com/ANOUARELIDRISSI/CounterTops.git
cd CounterTops

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Open browser: http://localhost:5000
```

## 📦 Technology Stack

- **Backend**: Flask (Python)
- **ML Framework**: OpenVINO 2026.0.0
- **Computer Vision**: OpenCV
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Render / Railway

## 📊 Detection Logic

The system uses a two-class approach:

1. **Fracture Defect** 🔴
   - Red bounding boxes around detected fractures
   - Confidence score displayed
   - Each fracture counted separately

2. **Normal Surface** 🟢
   - No bounding boxes
   - Displayed when no fractures detected

## 📱 Browser Compatibility

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari (iOS/macOS)
- ✅ Mobile browsers with camera support

## 📄 License

For demonstration and evaluation purposes.

## 🆘 Support

For issues or questions, open an issue on GitHub.

---

**Live Demo**: [Deploy your own!](https://render.com)

