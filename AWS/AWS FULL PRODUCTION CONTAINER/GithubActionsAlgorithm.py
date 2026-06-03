#1. Required EC2 setup (ONE TIME):
    ✔ Install Docker & Compose:
        sudo apt update
        sudo apt install docker.io docker-compose -y
        sudo systemctl enable docker
        sudo systemctl start docker

    ✔ Add your user to docker group
        sudo usermod -aG docker ubuntu
    ✔ Clone your project on EC2
        git clone https://github.com/your-username/your-repo.git
        cd your-repo
    ✔ Test run manually once
        docker-compose up -d --build

#2. Create SSH Key for GitHub Actions On your LOCAL machine:
    ssh-keygen -t ed25519 -C "github-actions"

    #You get:
    private key → id_ed25519
    public key → id_ed25519.pub

    ✔ Add PUBLIC key to EC2:
        cat id_ed25519.pub >> ~/.ssh/authorized_keys
    ✔ Copy PRIVATE key (important):You will add it to GitHub Secrets.
        cat id_ed25519

#3. Add GitHub Secrets
Go to: GitHub Repo → Settings → Secrets and Variables → Actions
Add:

| Key         | Value                     |
| ----------- | ------------------------- |
| EC2_HOST    | your-ec2-public-ip        |
| EC2_USER    | ubuntu                    |
| EC2_SSH_KEY | (your private key)        |
| EC2_PATH    | /home/ubuntu/your-project |



#4. GitHub Actions Workflow
Create: .github/workflows/deploy.yml

#FULL CI/CD PIPELINE:
name: Deploy Django to EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to EC2
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ${{ secrets.EC2_USER }}
          key: ${{ secrets.EC2_SSH_KEY }}

          script: |
            cd ~/Backend_Ecommerce_Store

            echo "Pulling latest code..."
            git pull origin main

            echo "Rebuilding images..."
            docker compose up -d --build
            docker image prune -f

            echo "Deployment complete!"



#5. What happens now (flow)

Every push to main:

1. GitHub detects push
2. Starts workflow
3. Connects to EC2 via SSH
4. Pulls latest code
5. Stops old containers
6. Rebuilds Docker images
7. Starts new containers



#⚠️ 6. Production improvements (important)
✔ Instead of full rebuild every time (optional upgrade)

Replace:

docker-compose up -d --build

With:

docker-compose pull
docker-compose up -d --no-deps --build web


#7. ✔ Add zero-downtime (advanced level)

You can later upgrade to:
    blue/green deployment
    rolling updates
    nginx upstream switching
✔ Add migrations safety
Better deploy step:
    docker-compose exec web python manage.py migrate
✔ Add static collection
docker-compose exec web python manage.py collectstatic --noinput

#8. Real-world mental model

You are now building:

GitHub = CI/CD trigger
Actions = automation engine
EC2 = runtime server
Docker Compose = process manager

This replaces:

manual SSH deploys
systemd updates
manual restarts


🚀 8. If you want next upgrade (VERY powerful)

I can help you build:

💥 Production-level CI/CD
run tests before deploy
linting (flake8 / black)
build Docker images in GitHub
push to Docker Hub / ECR
EC2 only pulls images (no build on server)
zero downtime deploy (blue-green)

Just tell me 👍







The progression I would suggest
Level 1 (what you're doing now)
GitHub Actions
      ↓
SSH
      ↓
EC2
      ↓
Docker Compose

Master this first.



Level 2
GitHub Actions
      ↓
Build Docker Image
      ↓
Docker Hub / ECR
      ↓
EC2 pulls image

This is where many mid-level engineers move next.




Level 3
GitHub Actions
      ↓
Kubernetes
      ↓
Rolling Deployments
      ↓
Zero Downtime

This is senior/cloud-native territory.