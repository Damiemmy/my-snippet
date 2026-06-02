#1.) create a folder and file path on root directory
.github/workflows/deploy.yml



#2.) paste this file  on this directory to test Deployement
name: Django Tests

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Check Django
        run: |
          python manage.py check



#3.) professionally add github secrete

#Repo → Settings → Secrets → Actions

#----------------or----------------#

#follow the right practice to afford github action error

import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')



#4. Add env in workflows

- name: Check Django
  env:
    SECRET_KEY: ${{ secrets.SECRET_KEY }}
    ALLOWED_HOSTS: ${{ secrets.ALLOWED_HOSTS }}
    DEBUG: ${{ secrets.DEBUG }}
  run: |
    python manage.py check



