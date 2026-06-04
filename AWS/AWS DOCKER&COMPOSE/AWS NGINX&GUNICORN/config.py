#1.install gunicorn
python3 install gunicorn

#2.test gunicorn

gunicorn Backend.wsgi:application --bind 0.0.0.0:8000

#3. add introduce nginx  and add gunicorn requirements.txt file
pip freeze > requirements.txt

#4. upgrade your system and add nginx to docker compose file

nginx:
  image: nginx:latest
  ports:
    - "80:80"
  volumes:
    - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
  depends_on:
    - web

#5. create a folder called "nginx" in root directory and add file to directory
run: mkdir nginx
run: nano nginx/default.conf
paste:
server {
    listen 80;

    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /app/static/;
    }
}

#🧠 WHAT JUST HAPPENED
    You just created:
        - reverse proxy layer
        - traffic routing system
        - production entry point

#6.UPDATE DJANGO FOR PRODUCTION STATIC FILES
STATIC_URL = "/static/"
STATIC_ROOT = "/app/static"
python manage.py collectstatic

#7. FULL SYSTEM START
docker compose up --build

#EXPECTED RESULT

Your system now has:
    ✔ Django
    ✔ PostgreSQL
    ✔ Redis
    ✔ Celery
    ✔ Gunicorn (inside web container)
    ✔ Nginx (reverse proxy)

#WHAT YOU JUST BECAME:
You now understand:
    - backend architecture
    - container orchestration
    - asynchronous systems
    - production deployment layers

Most developers NEVER reach this stage.