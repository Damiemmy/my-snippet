#1.) @docker-compose file: 
    - entrypoint: ["sh", "/app/entrypoint.sh"]  is unnecessary because Dockerfile has it already

#2.) gunicorn at docker and docker-compose file should listen at port 8000  not 800 e.g
    - CMD ["gunicorn","config.wsgi:application","--bind","0.0.0.0:8000"]  not "0.0.0.0:800"

#3.) remove source code mount on docker for development:
        '''
        i.) Development Compose
        volumes:
        - ./backend:/app
        - static_volume:/app/staticfiles
        - media_volume:/app/media

        Good for:

        "I'm actively developing."

        ii.)Production Compose
        volumes:
        - static_volume:/app/staticfiles
        - media_volume:/app/media

        Good for:

        "This is an immutable application image running in production."
        '''
    # IN SUMMARY:
        Development mounts your source code into Docker for convenience; production runs the tested code packaged inside the Docker image.

#4.) Don't expose django ports publicly:
    #remove:
    - "8000:8000"