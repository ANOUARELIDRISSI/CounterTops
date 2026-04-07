# Deploy to Railway.app (RECOMMENDED)

Railway is the best free option for your 155MB model!

## Why Railway?

- ✅ **$5 free credit/month** (enough for testing)
- ✅ **500MB+ size limit** (your model fits!)
- ✅ **No sleep mode** (always responsive)
- ✅ **Easy setup** (5 minutes)
- ✅ **GitHub integration** (auto-deploy on push)

## Prerequisites

- GitHub account
- Your code pushed to GitHub

## Method 1: Web Deploy (EASIEST) ⭐

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

### Step 2: Deploy on Railway
1. Go to https://railway.app
2. Click "Start a New Project"
3. Click "Deploy from GitHub repo"
4. Authorize Railway to access GitHub
5. Select your repository
6. Railway will:
   - Detect Python automatically
   - Install from requirements.txt
   - Start your app
   - Give you a URL!

### Step 3: Get Your URL
1. Click on your deployment
2. Go to "Settings" tab
3. Click "Generate Domain"
4. Your app is live at: `https://your-app.railway.app`

**That's it! 🎉**

---

## Method 2: CLI Deploy

### Step 1: Install Railway CLI
```bash
npm install -g @railway/cli
```

### Step 2: Login
```bash
railway login
```
This opens a browser to authenticate.

### Step 3: Initialize Project
```bash
railway init
```
- Choose "Create new project"
- Give it a name (e.g., "marble-detection")

### Step 4: Deploy
```bash
railway up
```

Railway will:
1. Upload your code
2. Detect Python
3. Install dependencies
4. Start your app

### Step 5: Get URL
```bash
railway domain
```
Or visit the Railway dashboard.

---

## Configuration

Railway automatically detects Python and uses:
- **Install**: `pip install -r requirements.txt`
- **Start**: `python app.py`

Your `Procfile` helps Railway know how to start:
```
web: python app.py
```

Your `app.py` is configured to read PORT from environment:
```python
port = int(os.environ.get('PORT', 5000))
```

---

## Environment Variables (Optional)

If you need to set environment variables:

### Via Web:
1. Go to your project
2. Click "Variables" tab
3. Add variables

### Via CLI:
```bash
railway variables set KEY=VALUE
```

---

## Monitoring

### View Logs
```bash
railway logs
```

### Via Web:
1. Go to your project
2. Click "Deployments" tab
3. Click on a deployment
4. View logs in real-time

---

## Updating Your App

### If using GitHub integration:
```bash
git add .
git commit -m "Update"
git push
```
Railway auto-deploys on push!

### If using CLI:
```bash
railway up
```

---

## Free Tier Limits

**$5 credit/month includes:**
- ~500 hours of usage
- 100GB outbound bandwidth
- 1GB RAM
- 1 vCPU

**Perfect for:**
- Testing
- Demos
- Portfolio projects
- Low-traffic apps

**When you run out:**
- Add $5/month for more credits
- Or use another free platform

---

## Troubleshooting

### Build Fails
```bash
# Check logs
railway logs

# Common issues:
# 1. Missing requirements.txt → Add it
# 2. Wrong Python version → Railway uses 3.9+
# 3. Model files missing → Check .gitignore
```

### App Not Starting
```bash
# Check if PORT is configured
# app.py should have:
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

### Model Not Loading
```bash
# Verify model files are in repo
git ls-files | grep model/

# Should show:
# model/saved_model.xml
# model/saved_model.bin
# model/saved_model.onnx
```

### Out of Memory
- Railway free tier: 1GB RAM
- Your model: ~156MB
- Should work fine!
- If issues, upgrade to $5/month plan

---

## Custom Domain (Optional)

### Add Custom Domain:
1. Go to project settings
2. Click "Domains"
3. Add your domain
4. Update DNS records as shown

---

## Cost Monitoring

### Check Usage:
1. Go to Railway dashboard
2. Click "Usage" tab
3. See credit consumption

### Typical Usage:
- Idle app: ~$0.50/month
- Light usage: ~$2-3/month
- Heavy usage: ~$5+/month

---

## Comparison with Other Platforms

| Feature | Railway | Vercel Free | Render Free |
|---------|---------|-------------|-------------|
| Size Limit | 500MB+ | 100MB | No limit |
| Sleep Mode | No | No | Yes (15min) |
| Free Tier | $5 credit | Limited | 750 hrs |
| Setup | Easy | Easy | Easy |
| **Best For** | **Your project!** | Small apps | Demos |

---

## Next Steps After Deployment

1. ✅ Test upload functionality
2. ✅ Test camera (requires HTTPS - Railway provides it)
3. ✅ Test on mobile
4. ✅ Share your URL!
5. ✅ Monitor usage in dashboard

---

## Support

- **Railway Docs**: https://docs.railway.app
- **Railway Discord**: https://discord.gg/railway
- **Railway Status**: https://status.railway.app

---

## Quick Reference

```bash
# Install CLI
npm install -g @railway/cli

# Login
railway login

# Initialize
railway init

# Deploy
railway up

# View logs
railway logs

# Open in browser
railway open

# Check status
railway status
```

---

**Ready to deploy?** Just run:
```bash
railway login
railway init
railway up
```

Your app will be live in minutes! 🚀
