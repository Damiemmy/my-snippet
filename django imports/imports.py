#LMS PLATFORM

#views.py
from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny,IsAuthenticated
from api import models as api_model
from rest_framework import generics,status
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from decimal import Decimal
from rest_framework.decorators import api_view,permission_classes
import stripe
import requests

import random

from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

//
//
#serializer.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

#models.py

from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from moviepy.editor import VideoFileClip
import math

#customUser

from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

#admin /snippet
from django.contrib import admin
from userauth.models import User,Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','full_name','date']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(User)




#ECOMMERCE PLATFORM
#views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,parser_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.conf import settings
from decimal import Decimal
import uuid
import requests
from rest_framework import status
import paypalrestsdk
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

#custom_user models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

#model.py
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
User=get_user_model()

#admin.py/snippet_admin:
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    # Add your custom fields to the default fieldsets (used when editing users)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("state", "city", "address", "phone")}),
    )

    # Add your custom fields to add_fieldsets (used when creating users in admin)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("state", "city", "address", "phone")}),
    )

    # Display your custom fields in the list view
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "city",
        "state",
        "phone",
    )


# Register the custom user model with custom admin
admin.site.register(CustomUser, CustomUserAdmin)
