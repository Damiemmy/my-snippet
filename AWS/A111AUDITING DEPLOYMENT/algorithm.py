#THIS 5 FILES ARE IMPORTANT TO UNDERSTAND THE PROJECT STRUCTURE AND HOW IT WORKS AND BELOW IS THE STATUS OF THE CURRENT DIRECTORY

#1. Project structure cmd:
    tree -L 2
    # Or if tree isn't installed run:
    find . -maxdepth 2 -type f | sort

#2. Backend Dockerfile
    #Understand: 
    backend/Dockerfile

#3. frontend Dockerfile
    #Understand: 
    frontend/Dockerfile

#4. Nginx configuration

    #Understand:
    nginx/default.conf

#5. #Docker-compose file:
    #understand:
    -ochestration
    -volumes(shared "static_volumes and media_volumes between nginx and backend", they must have same values to load effectively)


#CHECK .status(review) to acces this files and their current status and what I see in them
🚦Current assessment

| Component         | Status | What I see                   |
| ----------------- | ------ | ---------------------------- |
| Frontend          | 🟢     | Good multi-stage Vite build  |
| Backend           | 🟡     | Dockerfile has a CMD typo    |
| Nginx             | 🟢     | Routing structure is correct |
| PostgreSQL        | 🟢     | Port correctly removed       |
| Docker Compose    | 🟡     | Production cleanup needed    |
| Static files      | 🟢/🟡  | Architecture looks correct   |
| Media             | 🟡     | Backup strategy still needed |
| Disaster recovery | 🔴     | Not implemented yet          |
| AWS               | ⏳      | Don't deploy yet             |



#6.)Verify "config.settings.production" actually reads those variables and configures PostgreSQL.

Before we waste time deploying to AWS, 

- run: docker compose build

- Then: docker compose up -d

- Then: docker compose exec backend python manage.py shell

- Inside Django:

from django.conf import settings
settings.DATABASES


#6. confirm deployment is production ready by running:
docker compose ps
docker compose exec backend python manage.py check --deploy

#7. note:docker compose logs backend

We want to see:

Waiting for database...
Running migrations...
Roles seeded successfully.
Collecting static files...
[INFO] Starting gunicorn

And importantly: Database unavailable should not appear at the end.


#8. hierachy of the project:
        PostgreSQL
            ↓
          Django
            ↓
        Gunicorn
            ↓
          Nginx
            ↓
         Frontend

#9.) our checklist:
    Our critical-path checklist
    We're now down to this:

    [✓] seed_roles idempotent
    [✓] PostgreSQL Docker service
    [✓] PostgreSQL internal network
    [✓] Nginx reverse proxy
    [✓] Frontend Docker build
    [✓] Backend Docker build
    [✓] Gunicorn
    [✓] Static volume
    [✓] Media volume
    [✓] DB persistence volume

    [ ] Remove production bind mount
    [ ] Remove backend public port
    [ ] Remove duplicate entrypoint
    [ ] Fix backend Dockerfile CMD
    [ ] Verify Django actually uses PostgreSQL
    [ ] docker compose up
    [ ] manage.py check --deploy
    [ ] Test login
    [ ] Test upload/download
    [ ] Create DB + media backup
    [ ] AWS EC2
    [ ] HTTPS/domain

    #Final Instruction:
    - Don't send me another giant collection of files.
    - Do those Compose/Dockerfile cleanup changes, then run these four commands:
        - docker compose build
        - docker compose up -d
        - docker compose ps
        - docker compose exec backend python manage.py check --deploy

    Send me the output.

    Then we immediately move to AWS. No rabbit holes, no unnecessary architecture, no Redis/Celery/RDS/ECS nonsense. We are getting FUTMxStore in front of the students. 🔥

#10.) 
#in production settings.py
    DEBUG= False 
#and run this command for secret key generation and paste it:
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

#11.)create a .env.local file  for frontend and .env.example:
    '''
    the .env.local file illustrates and tells the frontend this is running on a development server  and it
    wouldn't use const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? '/api', the question becomes why "/api" and not "http://localhost:8000/api"? reasons are because the backend port on docker-composed file was removed for security reasons, note if .env.local file is push to production it would cause a problem by forcing production file to operate locally that why it must be committed  number 12 below illustrates how this would be done
    ''' 
    #important note: 
    '''
    when you are testing production .env.local should be renamed:reasons are ,.env.local would always be stubbon and wouln't allow you to test locally. 
        mental map(
            -.env.local 
                → development
            
            -no VITE_API_BASE_URL
                → Docker production
                → /api
        )
    '''
#12.).env.local:
    '''
    .env.local
    .env.*.local
    '''
#13.)🚨 Next: BACKUP BEFORE AWS

This is especially important because of your 2–3 hour recovery goal.
We're going to create two backups:

FUTMxStore Backup
├── PostgreSQL database
└── media/

Your code is already protected by GitHub.

#14.) Backup Algorithm:
    i -  mkdir -p backups
    ii - docker compose exec -T db pg_dump -U futmxstore_user -d futmxstore > backups/futmxstore_database.sql
         then to check: run
        -ls -lh backups/
    iii -Step 3 — Backup uploaded media,Your media is stored in a Docker volume, so we need to copy it out.First find the volume:
        -docker volume ls | grep media
    iv -media command :run this command to copy the media volume to a local directory:
    cmd(wsl):'''
    
    mkdir -p backups/media
docker run --rm \
  -v futmxstore_media_volume:/source:ro \
  -v "$(pwd)/backups/media:/backup" \
  alpine \
  sh -c "cp -a /source/. /backup/" 
  
  ''' 
  or 
cmd(wsl)'''
  docker compose cp backend:/app/media/. ./backups/media/"
'''
# read algorithm(backup) for future use:

#15.)create ec2 instance with 20GB and run
    ssh -i "pem_key.pem" ubuntu@public_ip_address
    sudo apt update && sudo apt install -y docker.io docker-compose-v2 git
    sudo systemctl enable --now docker
    sudo usermod -aG docker $USER
    
#16.) Check installed versions:
    - docker --version
    - docker compose version
    - git --version
#17.) before cloning repo, go to local directory and check:
    - git diff -- .gitignore
    - printf '\nbackups/\nbackups2/\n' >> .gitignore
    - tail -10 .gitignore
    - git add .gitignore README.md backend/Dockerfile backend/config/settings/production.py docker-compose.yml frontend/src/api/client.ts backend/.dockerignore frontend/.dockerignore
    -git commit -m "Prepare FUTMxStore for AWS production deployment"
    -git push -u origin main

#18.)create and elastic ip,connect it to ec2 and then add a sub-domain via netlify dns for futmxstore

#19.) integrate ssl:
    #first check if anything is running on port 443: 
        -sudo ss -ltnp | grep ':443' : we expect to see nothing running on port 443, if there is something running on port 443
    #secondly then:
    -run this command in the root directory : mkdir -p certbot/conf certbot/www
    #thridly then run these commands:
    -docker compose stop nginx and
    #fourthly then run these commands:
docker run --rm -p 80:80 \
  -v "$(pwd)/certbot/conf:/etc/letsencrypt" \
  certbot/certbot certonly --standalone \
  -d futmxstore.codemantsolutions.com \
  --email YOUR_EMAIL \
  --agree-tos \
  --no-eff-email
  #do not restart nginx yet, we will do that after editing the default.conf file below,

#20. After success edit default.conf file and add the following lines to the server block:


    listen 443 ssl; this is change from #listen 80; to listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/futmxstore.codemantsolutions.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/futmxstore.codemantsolutions.com/privkey.pem;
#21.) run docker compose up -d

#new_commandlines:
- docker compose config: print all settings in docker compose file and ensure that they are no errors
- docker compose exec nginx nginx -t: this could be used after adding a name server or other configuration and want to check nginx configuration file if it in good condition
- find . -name "default.conf" -o -name "nginx.conf": to check and find nginx configuration file location ,i did this when i want to assign a server_name: futmxstore.codemantsolutions.com  because it the best approach without reconfiguring frontend and backend file
- docker compose exec nginx nginx -t: You want to get "syntax is ok test is successful"


#finally you can check 

#1.)debugging ec2 crash

'''
A.)first SSH into it and we'll check what happened.

Run:df -h

then:free -h

then:docker system df

and:sudo systemctl status docker

The first two are especially important because a Docker build can consume a lot of disk space and RAM, particularly when you're building both Django and your frontend.


B.)Let's first confirm whether the kernel actually killed something because of insufficient memory.

Run this:sudo dmesg -T | grep -Ei 'oom|out of memory|killed process'

Then run:docker images

And:docker compose version

Then:cd rootdirectory and run :
docker compose ps


C.)Most importantly, let's add swap
Because your instance has 14 GB free, we can safely give Linux a 2 GB swap file.

Run these commands one at a time:

sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

Then verify: free -h

You should see something similar to:
Swap:2.0Gi

Finally, make the swap survive an EC2 reboot: echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

Why I'm recommending this

Think of RAM as your desk.
Your t3.micro has a very small desk:

RAM ≈ 1 GB

When Docker/Node/Django builds need more workspace, Linux has nowhere else to put temporary data because:

Swap = 0 GB

Adding:

Swap = 2 GB

doesn't turn the machine into a 3 GB machine—the swap is slower than RAM—but it gives the system breathing room and can prevent an OOM crash during a build.

D.)After finishing the swap commands then run 
- docker compose build backend --progress=plain :    and for backend
- docker compose build frontend --progress=plain : for frontend the run the whole container


'''


#docker cmd for nginx check
docker exec nginx_proxy nginx -t