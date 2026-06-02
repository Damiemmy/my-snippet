🌐 STEP 3 — INTRODUCE NGINX

Nginx is responsible for:

handling internet traffic
serving static files
forwarding requests to Gunicorn
improving performance
securing backend


Gunicorn is:A production WSGI server that runs Django efficiently
It handles:
    - multiple requests
    - worker processes
    - concurrency
    - stability


🧠 WHY NGINX IS IMPORTANT

Without Nginx:
Users → Direct Django server (bad, slow, insecure)

With Nginx:
Users → Nginx → Gunicorn → Django