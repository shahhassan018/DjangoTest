# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import UserProfile
from .serializers import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
import json

# Create your views here.

#API to create User Profile
@csrf_exempt
@api_view(['POST'])
def User_Profiles(request):

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


#API is used to show and edit the authorized user data
@api_view(['GET','PUT'])
def myData(request, pk):
    print(request)
    if request.method == 'GET':
        profile=UserProfile.objects.all()
        serializer = UserProfileSerialier(profile,many=True)
        return Response(serializer.data)

    elif  request.method == 'PUT':
        user = UserProfile.objects.get(user_id= pk)
        print('userprofile ', user)
        serializer = UserProfileSerialier(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#API facilitates the authorized & Anonymous user to view all the items
@api_view(['GET'])
def View_Items(request):

    if request.method == 'GET':
        items = Items.objects.all()
        serializer = ItemsSerializer(items,many=True)
        return Response(serializer.data)


#Api Faclitates only authorized user to post the items
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def Post_Items(request):

    if request.method == 'POST':

        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Api Faclitates only authorized user to get the items
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def Get_Items(request, pk):

    if request.method == 'GET':
        q = Items.objects.filter(user_id =pk)    #get data against particular user_id\
        print('q',q)
        serializer = ItemsSerializer(q,many=True)
        return Response(serializer.data)


#Api Faclitates only authorized user to edit the items
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def Edit_Items(request, pk):
     if request.method == 'PUT':
        userId = request.data['user']
        item = Items.objects.get(id=pk)
        if request.user != item.user:
            return Response({'message': 'You can only edit your own items', 'status': False},
                            status.HTTP_202_ACCEPTED)
        else:
            get_user = User.objects.get(pk=userId)
            dict.update({"user": get_user.id})
            print(dict)
            serializer = ItemsSerializer(item,data=dict)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)