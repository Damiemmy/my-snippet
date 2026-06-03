#1 Simple architecture of your new setup

                ┌──────────────┐
Internet ─────▶ │ Nginx (Docker)│
                └──────┬───────┘
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   Django + Gunicorn          Static/media
   (Docker container)

          │
          ▼
     Redis (container)

          │
          ▼
   Celery worker (container)

          │
          ▼
     Postgres (container)


#2. Project Structure (clean production layout)

project/
│
├── backend/
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── requirements.txt
│   └── manage.py
│
├── nginx/
│   └── default.conf
│
├── docker-compose.yml
├── .env
└── .dockerignore



#3. Docker Compose (Production Grade)

version: "3.9"

services:
  web:
    build: ./backend
    command: gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 4
    volumes:
      - ./backend:/app
    env_file:
      - .env
    depends_on:
      - db
      - redis
    restart: always

  celery:
    build: ./backend
    command: celery -A core worker -l info
    volumes:
      - ./backend:/app
    env_file:
      - .env
    depends_on:
      - db
      - redis
      - web
    restart: always

  celery-beat:
    build: ./backend
    command: celery -A core beat -l info
    volumes:
      - ./backend:/app
    env_file:
      - .env
    depends_on:
      - db
      - redis
      - web
    restart: always

  redis:
    image: redis:7-alpine
    restart: always
    ports:
      - "6379:6379"

  db:
    image: postgres:15
    restart: always
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

  nginx:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
      - ./backend:/app
    depends_on:
      - web
    restart: always

volumes:
  postgres_data:


#4. Django Dockerfile (backend/Dockerfile)

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]



#5. Entrypoint Script (VERY IMPORTANT)

#!/bin/sh
echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL started"

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"



#6 Nginx Config (Reverse Proxy)
server {
    listen 80;

    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /app/static/;
    }

    location /media/ {
        alias /app/media/;
    }
}



#7. .env File (IMPORTANT)

DEBUG=0
SECRET_KEY=your-secret-key

POSTGRES_DB=app_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=strongpassword
POSTGRES_HOST=db
POSTGRES_PORT=5432

REDIS_URL=redis://redis:6379/0


#8. Key Production Concepts (VERY IMPORTANT)

    #i. Gunicorn replaces Django runserver
        gunicorn core.wsgi:application
    #ii. Docker replaces systemd,Instead of:
            gunicorn.service
            nginx.service

        #You now have:
            docker-compose up -d

    #iii. Restart policy = system resilience
        restart: always
        This replaces systemd auto-restart.

    #iv. Service communication (VERY IMPORTANT)
        Inside Docker:
                      
            Services    .     How it is accessed
            ..............................
            Django	    .     web:8000
            Postgres    .     db:5432
            Redis	    .     redis:6379

            No localhost anymore.



#9. How everything flows:

User
 ↓
Nginx (port 80)
 ↓
Django (Gunicorn container)
 ↓
Postgres (db container)
Redis ← Celery worker
Redis ← Celery beat


#10. Run everything:
docker-compose up -d --build

#check logs:
docker-compose logs -f


#11. What makes this “production-grade”

✔ Gunicorn (not runserver)
✔ Nginx reverse proxy
✔ Celery worker + beat separation
✔ Persistent Postgres volume
✔ Redis broker
✔ Restart policies
✔ Entry-point wait-for-db logic
✔ Environment variables (.env)
✔ Container isolation