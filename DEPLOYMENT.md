# Deployment Guide

## Backend Deployment (Railway)

1. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/kidney-stone-ai.git
git push -u origin main
```

2. **Deploy on Railway:**
- Go to [railway.app](https://railway.app)
- Sign up with GitHub
- Click "New Project" → "Deploy from GitHub repo"
- Select your repository
- Railway will auto-detect Python and deploy

3. **Get Backend URL:**
- After deployment, copy the Railway URL (e.g., `https://kidney-stone-ai-production.up.railway.app`)

## Frontend Deployment (Vercel)

1. **Update API URL:**
- Edit `react-frontend/.env.production`
- Replace `your-backend-url.railway.app` with your actual Railway URL

2. **Build Frontend:**
```bash
cd react-frontend
npm run build
```

3. **Deploy on Vercel:**
- Go to [vercel.com](https://vercel.com)
- Sign up with GitHub
- Click "New Project" → Import your repository
- Set root directory to `react-frontend`
- Deploy

## Environment Variables

**Vercel (Frontend):**
- `VITE_API_URL` = Your Railway backend URL

**Railway (Backend):**
- No additional env vars needed

## Files Created for Deployment:

- `Procfile` - Railway startup command
- `runtime.txt` - Python version
- `requirements.txt` - Python dependencies
- `.env.production` - Production API URL

## Testing Deployment:

1. Test backend: `https://your-railway-url.railway.app/health`
2. Test frontend: Upload an image and verify it connects to backend

## Troubleshooting:

- **CORS errors**: Backend already configured for all origins
- **Build fails**: Check Python version in `runtime.txt`
- **API not connecting**: Verify `VITE_API_URL` in Vercel environment variables