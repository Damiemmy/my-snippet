# Complete Beginner-to-Production Guide: Deploying a Django Project to AWS EC2 for Free

## Introduction

This guide explains how to deploy a Django project to Amazon Web Services (AWS) using the AWS Free Tier.

By the end of this guide, you will understand:

* What AWS EC2 is
* How Django runs in production
* How to connect to a Linux server
* How to install Python and dependencies
* How to configure Gunicorn and Nginx
* How to serve static files
* How to use HTTPS/SSL
* How to configure Google OAuth after deployment
* How to debug common deployment errors
* How real-world Django deployment works

This is a production-style deployment process that can be used in portfolio projects.

---

# SECTION 1 — UNDERSTANDING THE DEPLOYMENT ARCHITECTURE

Before deploying, it is important to understand how production Django works.

## Development Mode

When developing locally, you usually run:

```bash
python manage.py runserver
```

This is only meant for development.

Django's development server:

* is not secure enough for production
* is not optimized for handling many users
* should never be used publicly

---

# Production Architecture

In production, the stack usually looks like this:

```text
Browser
   ↓
Nginx
   ↓
Gunicorn
   ↓
Django Application
```

## Role of Each Component

### Browser

The user visits your website.

Example:

```text
https://mywebsite.com
```

---

### Nginx

Nginx acts as:

* reverse proxy
* static file server
* request manager

Responsibilities:

* receives requests from users
* forwards requests to Gunicorn
* serves CSS/JS/images
* handles HTTPS
* improves performance

---

### Gunicorn

Gunicorn is a Python WSGI server.

Responsibilities:

* runs your Django app
* communicates with Nginx
* manages Django processes

---

### Django

Your actual application.

Handles:

* database
* APIs
* templates
* authentication
* business logic

---

# SECTION 2 — CREATE AWS ACCOUNT

Go to:

AWS Free Tier:

[https://aws.amazon.com/free](https://aws.amazon.com/free)

Create an AWS account.

Requirements:

* Email address
* Debit/Credit card
* Phone verification

AWS uses the card for identity verification.

---

# SECTION 3 — UNDERSTANDING EC2

EC2 means:

```text
Elastic Compute Cloud
```

An EC2 instance is simply:

```text
A virtual computer running in the cloud
```

You can:

* install software
* host websites
* run databases
* deploy APIs
* run Linux commands

---

# SECTION 4 — LAUNCHING AN EC2 INSTANCE

## Step 1 — Open AWS Console

Visit:

[https://console.aws.amazon.com](https://console.aws.amazon.com)

Search:

```text
EC2
```

Open EC2 Dashboard.

---

## Step 2 — Launch Instance

Click:

```text
Launch Instance
```

---

## Step 3 — Configure Instance

### Name

Example:

```text
django-production-server
```

---

### Choose Operating System

Select:

```text
Ubuntu Server 24.04 LTS
```

Ubuntu is beginner friendly and widely used.

---

### Choose Instance Type

Select:

```text
t2.micro
```

This is free-tier eligible.

---

### Create Key Pair

Click:

```text
Create new key pair
```

Example:

```text
django-key
```

Choose:

* RSA
* .pem format

Download the file.

IMPORTANT:

Do not lose this file.

This file allows you to connect to the server.

---

### Configure Security Group

Allow:

* SSH
* HTTP
* HTTPS

Ports:

| Port | Purpose |
| ---- | ------- |
| 22   | SSH     |
| 80   | HTTP    |
| 443  | HTTPS   |

---

## Step 4 — Launch Instance

Click:

```text
Launch Instance
```

Your server will be created.

---

# SECTION 5 — CONNECTING TO YOUR SERVER

## What is SSH?

SSH means:

```text
Secure Shell
```

It allows you to control a remote Linux server.

---

## Step 1 — Open Terminal

If using:

* Ubuntu → Terminal
* Windows → PowerShell or WSL
* Mac → Terminal

---

## Step 2 — Move to Key Location

Example:

```bash
cd Downloads
```

---

## Step 3 — Set File Permission

```bash
chmod 400 django-key.pem
```

Why?

Linux blocks insecure private keys.

---

## Step 4 — Connect to EC2

```bash
ssh -i django-key.pem ubuntu@YOUR_PUBLIC_IP
```

Example:

```bash
ssh -i django-key.pem ubuntu@13.60.xx.xx
```

If successful:

You are now inside your cloud server.

---

# SECTION 6 — UPDATE THE SERVER

Always update packages first.

```bash
sudo apt update && sudo apt upgrade -y
```

Explanation:

| Command     | Meaning                |
| ----------- | ---------------------- |
| apt update  | refresh package list   |
| apt upgrade | install latest updates |
| -y          | auto confirm           |

---

# SECTION 7 — INSTALL REQUIRED SOFTWARE

Install:

```bash
sudo apt install python3-pip python3-venv nginx git -y
```

What each package does:

| Package      | Purpose                    |
| ------------ | -------------------------- |
| python3-pip  | install Python packages    |
| python3-venv | create virtual environment |
| nginx        | web server                 |
| git          | clone GitHub repositories  |

---

# SECTION 8 — CLONE YOUR DJANGO PROJECT

## Step 1 — Copy GitHub Repository URL

Example:

```text
https://github.com/username/myproject.git
```

---

## Step 2 — Clone Repository

```bash
git clone https://github.com/username/myproject.git
```

---

## Step 3 — Enter Project Folder

```bash
cd myproject
```

---

# SECTION 9 — CREATE VIRTUAL ENVIRONMENT

## What is a Virtual Environment?

A virtual environment isolates project dependencies.

Without virtual environments:

* packages conflict
* projects interfere with each other

---

## Create Environment

```bash
python3 -m venv venv
```

---

## Activate Environment

```bash
source venv/bin/activate
```

If successful:

You will see:

```text
(venv)
```

---

# SECTION 10 — INSTALL PROJECT DEPENDENCIES

## Install Requirements

```bash
pip install -r requirements.txt
```

If you do not have requirements.txt:

Generate it locally:

```bash
pip freeze > requirements.txt
```

Commit and push to GitHub.

---

# SECTION 11 — CONFIGURE DJANGO SETTINGS

Open:

```text
settings.py
```

---

## Configure Allowed Hosts

Example:

```python
ALLOWED_HOSTS = [
    "13.60.xx.xx",
    "localhost",
    "127.0.0.1"
]
```

If using a domain:

```python
ALLOWED_HOSTS = [
    "mywebsite.com",
    "www.mywebsite.com"
]
```

---

## Configure Static Files

Add:

```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

Why?

Django must collect CSS/JS/images into one folder.

---

## Collect Static Files

Run:

```bash
python manage.py collectstatic
```

Type:

```text
yes
```

---

# SECTION 12 — RUN DATABASE MIGRATIONS

Apply migrations:

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

Enter:

* username
* email
* password

---

# SECTION 13 — TEST DJANGO LOCALLY ON SERVER

## Install Gunicorn

```bash
pip install gunicorn
```

---

## Start Gunicorn

```bash
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

Replace:

```text
config
```

with your Django project folder name.

Example:

```bash
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

---

## Test Website

Visit:

```text
http://YOUR_PUBLIC_IP:8000
```

If the app opens:

Gunicorn is working.

Press:

```text
CTRL + C
```

to stop Gunicorn.

---

# SECTION 14 — CREATE GUNICORN SERVICE

## Why Systemd Service?

Without systemd:

* Gunicorn stops when terminal closes
* server dies after reboot

Systemd keeps your app running permanently.

---

## Create Service File

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Paste:

```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/myproject
ExecStart=/home/ubuntu/myproject/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/ubuntu/myproject/gunicorn.sock \
          config.wsgi:application

[Install]
WantedBy=multi-user.target
```

IMPORTANT:

Replace:

| Replace   | With                      |
| --------- | ------------------------- |
| myproject | your project folder       |
| config    | your Django config folder |

---

## Reload Systemd

```bash
sudo systemctl daemon-reload
```

---

## Start Gunicorn

```bash
sudo systemctl start gunicorn
```

---

## Enable Gunicorn on Boot

```bash
sudo systemctl enable gunicorn
```

---

## Check Status

```bash
sudo systemctl status gunicorn
```

If successful:

You should see:

```text
active (running)
```

---

# SECTION 15 — CONFIGURE NGINX

## Create Nginx Config

```bash
sudo nano /etc/nginx/sites-available/myproject
```

Paste:

```nginx
server {
    listen 80;
    server_name YOUR_PUBLIC_IP;

    location = /favicon.ico {
        access_log off;
        log_not_found off;
    }

    location /static/ {
        root /home/ubuntu/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/myproject/gunicorn.sock;
    }
}
```

---

## Enable Nginx Config

```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
```

---

## Test Nginx Configuration

```bash
sudo nginx -t
```

Expected output:

```text
syntax is ok
```

---

## Restart Nginx

```bash
sudo systemctl restart nginx
```

---

# SECTION 16 — OPEN FIREWALL PORTS

Go to:

```text
EC2 → Security Groups
```

Edit inbound rules.

Allow:

| Type  | Port |
| ----- | ---- |
| HTTP  | 80   |
| HTTPS | 443  |
| SSH   | 22   |

---

# SECTION 17 — VISIT YOUR LIVE WEBSITE

Visit:

```text
http://YOUR_PUBLIC_IP
```

Your Django project should now be live.

---

# SECTION 18 — UNDERSTANDING STATIC FILES

Static files include:

* CSS
* JavaScript
* images
* icons

In production:

Django does NOT serve static files automatically.

Nginx serves them instead.

---

# SECTION 19 — HTTPS/SSL CONFIGURATION

## Why HTTPS Matters

HTTPS:

* encrypts traffic
* secures login sessions
* protects OAuth
* improves trust
* required by many APIs

---

# Install Certbot

```bash
sudo apt install certbot python3-certbot-nginx -y
```

---

# Run Certbot

```bash
sudo certbot --nginx
```

Follow prompts.

Certbot automatically:

* installs SSL certificate
* configures Nginx
* redirects HTTP to HTTPS

---

# SECTION 20 — CONFIGURE DOMAIN NAME

Instead of using an IP address, use a domain.

Example:

```text
mywebsite.com
```

Popular domain providers:

* Namecheap
* GoDaddy
* Cloudflare

---

## Point Domain to AWS

In DNS settings:

Create:

```text
A Record
```

Point it to:

```text
YOUR_PUBLIC_IP
```

---

# SECTION 21 — GOOGLE OAUTH CONFIGURATION

If your project uses Google OAuth:

Open:

```text
Google Cloud Console
```

Add your production URLs.

---

## Authorized JavaScript Origins

Example:

```text
https://mywebsite.com
```

---

## Authorized Redirect URIs

Example:

```text
https://mywebsite.com/accounts/google/login/callback/
```

IMPORTANT:

Production URLs must exactly match.

---

# SECTION 22 — ENVIRONMENT VARIABLES

Never expose:

* SECRET_KEY
* API keys
* database passwords
* OAuth secrets

---

# Install python-decouple

```bash
pip install python-decouple
```

---

# Create .env File

```bash
nano .env
```

Example:

```env
SECRET_KEY=mysecretkey
DEBUG=False
```

---

# Use in settings.py

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
```

---

# SECTION 23 — COMMON DEPLOYMENT ERRORS

## Error 1 — DisallowedHost

Cause:

```python
ALLOWED_HOSTS not configured
```

Fix:

Add server IP/domain.

---

## Error 2 — Static Files Not Loading

Cause:

* forgot collectstatic
* incorrect STATIC_ROOT
* Nginx config wrong

Fix:

```bash
python manage.py collectstatic
```

---

## Error 3 — Gunicorn Failed

Check logs:

```bash
sudo journalctl -u gunicorn
```

---

## Error 4 — Nginx Error

Check:

```bash
sudo nginx -t
```

---

## Error 5 — Permission Errors

Fix:

```bash
sudo chmod -R 755 projectfolder
```

---

# SECTION 24 — USEFUL COMMANDS

## Restart Gunicorn

```bash
sudo systemctl restart gunicorn
```

---

## Restart Nginx

```bash
sudo systemctl restart nginx
```

---

## Check Gunicorn Logs

```bash
sudo journalctl -u gunicorn
```

---

## Reload Nginx

```bash
sudo systemctl reload nginx
```

---

## Stop Gunicorn

```bash
sudo systemctl stop gunicorn
```

---

# SECTION 25 — HOW TO UPDATE YOUR WEBSITE AFTER CHANGES

After editing code locally:

## Step 1 — Push to GitHub

```bash
git add .
git commit -m "updated project"
git push
```

---

## Step 2 — Pull on Server

SSH into server.

Then:

```bash
git pull
```

---

## Step 3 — Activate Virtual Environment

```bash
source venv/bin/activate
```

---

## Step 4 — Install New Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5 — Migrate Database

```bash
python manage.py migrate
```

---

## Step 6 — Collect Static Files

```bash
python manage.py collectstatic
```

---

## Step 7 — Restart Gunicorn

```bash
sudo systemctl restart gunicorn
```

---

# SECTION 26 — DATABASE OPTIONS

## SQLite

Good for:

* portfolio projects
* small apps
* testing

Not ideal for high traffic.

---

## PostgreSQL

Best for production.

Advantages:

* scalable
* reliable
* professional
* secure

---

# Install PostgreSQL

```bash
sudo apt install postgresql postgresql-contrib
```

---

# SECTION 27 — SECURITY BEST PRACTICES

## Disable Debug Mode

```python
DEBUG = False
```

Never use:

```python
DEBUG = True
```

in production.

---

## Use Strong Passwords

Use strong:

* admin passwords
* database passwords
* secret keys

---

## Keep Packages Updated

Regularly run:

```bash
sudo apt update && sudo apt upgrade
```

---

# SECTION 28 — WHAT YOU LEARNED

By completing this deployment, you learned:

* Linux basics
* SSH
* cloud servers
* EC2
* Gunicorn
* Nginx
* static files
* HTTPS
* production deployment
* systemd services
* real backend deployment workflow

These are real-world backend engineering skills.

---

# SECTION 29 — NEXT THINGS TO LEARN

After mastering EC2 deployment, learn:

1. Docker
2. Docker Compose
3. PostgreSQL deeply
4. Redis
5. Celery
6. CI/CD pipelines
7. GitHub Actions
8. Kubernetes
9. AWS S3
10. AWS RDS
11. Load balancing
12. Caching
13. Monitoring and logging

---

# FINAL WORDS

Deploying a Django project is one of the biggest milestones in backend development.

Most beginners can build projects locally.

Far fewer developers can:

* deploy applications
* configure Linux servers
* manage production environments
* secure applications
* debug deployment issues

Learning deployment makes you significantly stronger as a backend engineer.

Continue practicing until deployment becomes second nature.
