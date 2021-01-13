from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Survey, Choice, Answer


def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    pass
