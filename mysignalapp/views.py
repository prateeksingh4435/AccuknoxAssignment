from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.models import User
import threading
from django.db import transaction

def index(request):
    print(f"Creating user in thread: {threading.get_ident()}")
    User.objects.create_user(username='test987', password='pass123')
    return HttpResponse("User created and thread ID printed.")


def create_user(request):
    try:
        with transaction.atomic():  
            User.objects.create_user(username='error_user', password='password123')
            return HttpResponse("User created successfully.")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")