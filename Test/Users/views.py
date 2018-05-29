# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
# from. serializers import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def UserProfiles(request):

    if request.method =='POST':
        try:
            user = User.objects.create_user(username=request.data['username'],
                                            email=request.data['email'],
                                            password=request.data['password'])
        except:
            return Response('Data exists already', status=status.HTTP_400_BAD_REQUEST)

        if user !='':
            user_profile = UserProfile(
                user=user,
                First_Name=request.data['First_Name'],
                Last_Name = request.data['Last_Name'],
                Phone_No = request.data['Phone_No'],
                Country = request.data['Country'],
                Role = request.data['Role']
            )
            user_profile.save()
        else:
            return Response({"message":"Try Again"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message":"User Profile Created Successfully"}, status=status.HTTP_200_OK)