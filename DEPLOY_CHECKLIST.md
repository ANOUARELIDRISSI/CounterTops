# Quick Deployment Checklist

## ⚠️ Important: Model Size
Your model is **155.85 MB** - too large for Vercel free tier (100MB limit)

**Recommended Platform: Railway.app** ✅
- $5 free credit/month
- 500MB+ size limit
- No sleep mode
- Easy setup

See [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md) for Railway-specific guide.

## Pre-Deployment

- [x] Model updated to model_marbles2
- [x] Detection logic updated (Fracture vs Normal Surface)
- [x] UI updated for 2 classes
- [x] .gitignore created
- [x] Deployment configs created (vercel.json, Procfile)
- [x] requirements.txt optimized (opencv-python-headless)
- [x] app.py configured for deployment (PORT environment variable)

## Git Setup

```bash
# 1. Initialize git
git init

# 2. Add files
git add .

# 3. Check what will be committed (should exclude venv, datasets, etc.)
git status

# 4. Commit
git commit -m "Initial commit: Marble fracture detection"

# 5. Create GitHub repo at https://github.com/new

# 6. Add remote (replace YOUR_USERNAME and REPO_NAME)
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# 7. Push
git branch -M main
git push -u origin main
```

## Railway Deployment (RECOMMENDED) ⭐

### Quick Deploy via Web (5 minutes!)
1. Push code to GitHub (see Git Setup above)
2. Go to https://railway.app
3. Click "Start a New Project"
4. Click "Deploy from GitHub repo"
5. Select your repository
6. Railway auto-deploys!
7. Click "Generate Domain" to get your URL

### CLI Deploy
```bash
npm install -g @railway/cli
railway login
railway init
railway up
railway domain  # Get your URL
```

**See [DEPLOY_RAILWAY.md](DEPLOY_RAILWAY.md) for detailed Railway guide.**

---

## Vercel Deployment (Requires Pro Tier)

⚠️ **Note**: Your model (155MB) exceeds Vercel free tier (100MB)
- Requires Vercel Pro: $20/month
- Or use Railway instead (recommended)

## Post-Deployment Testing

- [ ] Test upload with fracture image
- [ ] Test upload with normal surface image
- [ ] Verify bounding boxes only show for fractures
- [ ] Test camera (requires HTTPS)
- [ ] Check mobile responsiveness
- [ ] Verify detection results panel

## Files Being Pushed (Essential Only)

```
├── app.py
├── templates/
│   └── index.html
├── model/
│   ├── saved_model.xml
│   ├── saved_model.bin
│   └── saved_model.onnx
├── dm.json
├── meta.json
├── requirements.txt
├── vercel.json
├── README_APP.md
└── DEPLOYMENT.md
```

## Files NOT Being Pushed (Excluded)

```
├── venv/
├── __pycache__/
├── Dataset/
├── model_marbles/
├── model_marbles2/
├── test_*.py
├── *.zip
└── images/
```

## Important Notes

⚠️ **Model Size**: Check if your model files fit within Vercel limits (100MB free, 250MB pro)

⚠️ **Alternative Platforms** if Vercel fails:
- Railway.app
- Render.com
- Heroku
- Google Cloud Run

## Quick Commands Reference

```bash
# Check repository size
du -sh model/

# View what git will push
git ls-files

# Force add a file if needed
git add -f filename

# Remove file from git (keep local)
git rm --cached filename

# Update deployment
git add .
git commit -m "Update"
git push
```

## Success Indicators

✅ Build completes without errors
✅ Deployment URL is accessible
✅ Upload functionality works
✅ Fractures are detected and boxed
✅ Normal surfaces show "Normal Surface" classification
✅ Mobile UI is responsive

## Need Help?

- Check DEPLOYMENT.md for detailed instructions
- View Vercel logs for errors
- Test locally first: `python app.py`
