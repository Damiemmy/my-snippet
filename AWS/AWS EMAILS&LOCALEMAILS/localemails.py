#EMAIL FEATURES:
email = EmailMessage(
    subject="Report",
    body="Please find attached report",
    from_email="admin@example.com",
    to=["user@example.com"],
)

email.attach_file("report.pdf")
email.send()



#1.EMAIL SETTINGS CONFIGURATION:

import os
from dotenv import load_dotenv

load_dotenv()

# EMAIL BACKEND CONSOLE
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# SMTP CONFIG (Gmail example)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_USE_SSL = True

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


#2.) EMAIL SETUP(CREATING CELERY TASKS):
from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def send_welcome_email(user_email, username):
    email = EmailMessage(
        subject="Welcome!",
        body=f"Hello {username}, welcome to our platform 🚀",
        from_email="your_email@gmail.com",
        to=[user_email],
    )
    email.send()
    return f"Email sent to {to_email}"

                    #ADDING RETRIALS IMPORTANT IN PRODUCTION

@shared_task(bind=True, max_retries=3)
def send_email_task(self, subject, body, to_email):
    try:
        email = EmailMessage(subject, body, None, [to_email])
        email.send()
    except Exception as exc:
        raise self.retry(exc=exc, countdown=5)



#3.CALLING THE TASK ASYNCHRONOUSLY:

from .tasks import send_welcome_email

send_welcome_email.delay(user.email, user.username)

#4.templates:
from django.template.loader import render_to_string

user_email_html = render_to_string("emails/signup_welcome.html", {
                "username": user.username,
                "login_url": login_url,
            })
user_email = EmailMessage(
            subject="Welcome to Johnsonix 🎧",
            body=user_email_html,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email],
        )
        user_email.content_subtype = "html"
        user_email.send(fail_silently=False)
email.content_subtype = "html"  # IMPORTANT
email.send()

#5.) 
#--------------------INDUSTRY STANDARD FOR INDUSTRY UTILY------------------------#
#----------------Render HTML email in Python (industry utility)------------------#
            #------------------(utils/email.py)-----------------------#



from django.template.loader import render_to_string
from django.utils.timezone import now
from django.conf import settings
from django.core.mail import EmailMessage


def send_html_email(subject, template, context, to_email):
    context["year"] = now().year

    html_content = render_to_string(template, context)

    email = EmailMessage(
        subject=subject,
        body=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[to_email],
    )

    email.content_subtype = "html"  # IMPORTANT
    email.send()

#---------------Celery TASK using template system(industry utility)---------------------#

from celery import shared_task
from .utils.email import send_html_email


@shared_task
def send_welcome_email_task(email, username):
    send_html_email(
        subject="Welcome to Our Platform",
        template="emails/welcome_email.html",
        context={"username": username},
        to_email=email
    )


#------------------------Call it from your view----------------------------#

from .tasks import send_welcome_email_task

send_welcome_email_task.delay(
    user.email,
    user.username
)


You can:
    - Add attachments
    - Set headers
    - Send HTML emails
    - Customize everything before sending


