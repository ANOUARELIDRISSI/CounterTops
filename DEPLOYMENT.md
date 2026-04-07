# Deployment Guide - Vercel

## Prerequisites

1. GitHub account
2. Vercel account (sign up at https://vercel.com)
3. Git installed on your machine

## Files to Push to GitHub

The `.gitignore` file is configured to only push essential files:

### Essential Files (will be pushed):
- `app.py` - Flask application
- `templates/index.html` - Web interface
- `model/` - Active model directory
  - `saved_model.xml`
  - `saved_model.bin`
  - `saved_model.onnx`
- `dm.json` - Class definitions
- `meta.json` - Model metadata
- `requirements.txt` - Python dependencies
- `vercel.json` - Vercel configuration
- `README_APP.md` - Documentation

### Excluded Files (will NOT be pushed):
- `venv/` - Virtual environment
- `__pycache__/` - Python cache
- `Dataset/` - Training datasets
- `model_marbles/` and `model_marbles2/` - Backup models
- Test files and images
- Archives (.zip, .tar, etc.)

## Step 1: Initialize Git Repository

```bash
# Initialize git (if not already done)
git init

# Add all files (respecting .gitignore)
git add .

# Commit
git commit -m "Initial commit: Marble defect detection app"
```

## Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (e.g., "marble-defect-detection")
3. Don't initialize with README (we already have files)

## Step 3: Push to GitHub

```bash
# Add remote (replace with your repository URL)
git remote add origin https://github.com/YOUR_USERNAME/marble-defect-detection.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Deploy to Vercel

### Option A: Via Vercel Dashboard (Recommended)

1. Go to https://vercel.com/dashboard
2. Click "Add New" → "Project"
3. Import your GitHub repository
4. Vercel will auto-detect the configuration from `vercel.json`
5. Click "Deploy"

### Option B: Via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy
vercel
```

## Important Notes

### Model Size Limitations

⚠️ **WARNING**: Vercel has deployment size limits:
- Free tier: 100MB total deployment size
- Pro tier: 250MB total deployment size

Your model files may exceed these limits. If deployment fails:

1. **Option 1**: Use Vercel Pro account
2. **Option 2**: Host model files externally (AWS S3, Google Cloud Storage)
3. **Option 3**: Use alternative platforms:
   - Railway.app (more generous limits)
   - Render.com (supports larger deployments)
   - Heroku
   - Google Cloud Run
   - AWS Elastic Beanstalk

### Alternative: Railway Deployment

If Vercel fails due to size limits, try Railway:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy
railway up
```

### Environment Variables

No environment variables needed for this app.

### Custom Domain (Optional)

1. Go to your Vercel project settings
2. Navigate to "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

## Testing Deployment

After deployment, test:
1. Upload an image with fractures
2. Upload an image without fractures (should show "Normal Surface")
3. Test camera functionality (requires HTTPS)

## Troubleshooting

### Build Fails
- Check Vercel build logs
- Verify all dependencies in requirements.txt
- Ensure model files are present

### Model Not Loading
- Check file paths in app.py
- Verify model files are in correct directory
- Check Vercel function logs

### Large Deployment Size
- Use `opencv-python-headless` instead of `opencv-python` ✅ (already configured)
- Consider model compression
- Use external storage for model files

## Monitoring

- View logs: Vercel Dashboard → Your Project → Logs
- Monitor performance: Vercel Dashboard → Analytics
- Check errors: Vercel Dashboard → Runtime Logs

## Updating Deployment

```bash
# Make changes to your code
git add .
git commit -m "Update: description of changes"
git push

# Vercel will automatically redeploy
```

## Cost Considerations

- Vercel Free Tier: Good for testing, limited bandwidth
- Vercel Pro: $20/month, better for production
- Consider serverless function execution limits

## Security Recommendations

1. Add rate limiting for production
2. Implement file upload size limits
3. Add authentication if needed
4. Use HTTPS (automatic on Vercel)
5. Monitor usage and costs

## Support

- Vercel Docs: https://vercel.com/docs
- Vercel Community: https://github.com/vercel/vercel/discussions
