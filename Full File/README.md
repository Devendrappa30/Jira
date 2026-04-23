# Devendrappa Portfolio — Render.com Deployment Guide

## Project Structure
```
devendrappa_portfolio/
├── app.py               # Flask backend
├── requirements.txt     # Python dependencies
├── Procfile             # Tells Render how to start the app
├── render.yaml          # Render service config (optional)
├── templates/
│   └── index.html       # Main portfolio page
└── README.md
```

## Local Development

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run locally
```bash
python app.py
```
Visit http://localhost:5000

---

## Deploy to Render.com — Step by Step

### Step 1: Push to GitHub
1. Create a new GitHub repository (e.g. `devendrappa-portfolio`)
2. Upload all project files to the repository
3. Make sure `app.py`, `requirements.txt`, `Procfile`, and the `templates/` folder are at the root level

### Step 2: Create Render Account
1. Go to https://render.com and sign up (free tier available)
2. Connect your GitHub account

### Step 3: Create a New Web Service
1. Click **"New +"** → **"Web Service"**
2. Select your GitHub repository
3. Fill in these settings:
   - **Name:** `devendrappa-portfolio` (or anything you like)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app.app`
   - **Plan:** Free (for testing) or Starter ($7/mo for always-on)

### Step 4: Deploy
1. Click **"Create Web Service"**
2. Render will build and deploy automatically
3. Your site will be live at: `https://devendrappa-portfolio.onrender.com`

---

## Adding a Profile Photo

Replace the `D` placeholder in the hero section:

1. Add your photo to a hosting service (e.g. Cloudinary, GitHub raw, ImgBB)
2. In `templates/index.html`, find the `profile-placeholder` div and replace with:
```html
<img src="YOUR_PHOTO_URL" alt="Devendrappa" class="profile-placeholder" style="font-size:unset;">
```

---

## Customizing Your Email in Contact Section

In `templates/index.html`, find this line and update:
```html
<a href="mailto:devendrappa@example.com" class="contact-link">
```

---

## Contact Form Submissions

Contact form submissions are currently logged to Render's console logs.
To view them:
1. Go to your Render dashboard
2. Open your web service
3. Click **"Logs"** tab

### To save to a database (optional upgrade):
Install `flask-sqlalchemy` and set up a PostgreSQL database (Render offers free PostgreSQL).

---

## Custom Domain (Optional)
1. In Render dashboard → your service → **"Settings"**
2. Scroll to **"Custom Domains"**
3. Add your domain (e.g. `devendrappa.com`)
4. Update your DNS records as instructed by Render
