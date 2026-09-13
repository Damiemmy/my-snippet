-python -m pip install scikit-learn : installation
-python -c "import sklearn; print(sklearn.__version__)" : verification of version installed

-mv ~/.docker/config.json ~/.docker/config.json.backup: fix for docker refusing to build image
-docker compose exec frontend printenv INTERNAL_API_URL: to verify frontend container .env vairable

Lessons:
'''
The lesson to never forget
localhost always means "this machine/container."

In Docker:

localhost:3000       → this container
backend:8000         → backend container
nginx:80             → nginx container

So remember this rule:

Browser → use the public URL (/api/... or http://localhost/...).
Container → container → use the Docker service name (http://backend:8000/...).

And you do NOT need to expose port 8000 with ports: for containers to communicate. Docker's internal network handles that.
'''