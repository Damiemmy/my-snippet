Docker Media Backup — Two Approaches
#Approach 1 — Temporary Alpine container

This approach mounts the Docker volume into a temporary Alpine Linux container and copies the files out to your local backups/media directory.

- mkdir -p backups/media

- docker run --rm \
  -v futmxstore_media_volume:/source:ro \
  -v "$(pwd)/backups/media:/backup" \
  alpine \
  sh -c "cp -a /source/. /backup/"
What is happening?

futmxstore_media_volume
        │
        │ mounted read-only
        ▼
   /source
   [Alpine container]
        │
        │ cp -a
        ▼
backups/media/


futmxstore_media_volume = your Docker production media volume.
/source:ro = mount it read-only, so the backup process cannot accidentally modify your production files.
backups/media = where the backup is stored on your computer.
--rm = delete the temporary Alpine container after the backup finishes.
cp -a = copy the media while preserving the directory structure and file metadata.

This is a nice generic Docker-volume backup technique because it doesn't depend on your Django container.

#Approach
 2 — Docker Compose

Your second approach uses the already-running Django container:

mkdir -p backups/media

docker compose cp backend:/app/media/. ./backups/media/

Your Compose configuration already mounts:

volumes:
  - media_volume:/app/media

So:

Docker volume
     │
     ▼
backend container
/app/media
     │
     │ docker compose cp
     ▼
backups/media/

You're essentially saying:

"Docker Compose, take everything inside /app/media in my backend container and copy it to my computer."

This is arguably the simpler approach for your current FUTMxStore project because your backend container already has access to the media volume.

#Which one should you use?

For FUTMxStore right now, I'd use:

docker compose cp backend:/app/media/. ./backups/media/

It's simpler and doesn't require pulling another image.

But keep the Alpine method in your documentation because it's an excellent general-purpose Docker volume backup technique.

Your complete FUTMxStore backup

You now have two different types of production data to protect:

1. PostgreSQL database
- mkdir -p backups

- docker compose exec -T db \
  pg_dump -U futmxstore_user -d futmxstore \
  > backups/futmxstore_database.sql

This protects things like:

Users
Courses
Materials metadata
Roles
Authentication data
Database relationships
Other PostgreSQL records

2. Uploaded media
- mkdir -p backups/media

- docker compose cp backend:/app/media/. ./backups/media/

This protects the actual uploaded files.

That's important because your database might know:

Material: Mathematics Past Questions
File: materials/math_past_questions.pdf

but the PDF itself lives in your media volume.

Database backup without media backup = incomplete recovery.

One important thing before AWS

Your backup directory should NOT go to GitHub.

Add this to your root .gitignore:

backups/

And make sure your production environment file is also ignored:

backend/.env.production

You don't want your database dump or production secrets sitting inside a public GitHub repository.

And honestly, today's little Docker episode is worth remembering. 😂

You didn't just learn Docker backup strategies today.

You learned another engineering principle:

When your brain is overloaded, adding more debugging time doesn't necessarily increase productivity.

Sometimes the most productive command is:

shutdown