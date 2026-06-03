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



#5. Phase 2: Connect GitHub to EC2(for deployement)
 ssh into ec2

#6. Generate Key:
ssh-keygen -t ed25519 #press Enter repeatedly

#output:
id_ed25519 → PRIVATE KEY (secret, stays on EC2)
id_ed25519.pub → PUBLIC KEY (safe to share)

#7. run command:
cat ~/.ssh/id_ed25519.pub 

#output Public Key:
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILz8/YeTlun9b843S6joChHzbEZOik28p/15i0V9bw8U ubuntu@ip-172-31-46-29

#8. Add it to EC2 authorized keys (IMPORTANT CHECK)
#run command:
cat ~/.ssh/authorized_keys

#check if public key is inside most times is not by default so run :
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILz8/YeTlun9b843S6joChHzbEZOik28p/15i0V9bw8U ubuntu@ip-172-31-46-29" >> ~/.ssh/authorized_keys
#this command above adds public key to authorized keys


#9. CONFIGURE EC2_HOST,EC2_USER,EC2_SSH_KEY in github action
EC2_USER=ubuntu
EC2_HOST=my-public ip
EC2_SSH_KEY= run command "cat ~/.ssh/id_ed25519" to get EC2_SSH_KEY


