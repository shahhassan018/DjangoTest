# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Phone_No =  models.CharField(max_length=50,null=True)
    Country = models.CharField(max_length=100,null=True)
    First_Name = models.CharField(max_length=50,null=True)
    Last_Name = models.CharField(max_length=50, null=True)
    Deleted = models.BooleanField(default=False)
    CreatedAt = models.DateTimeField(auto_now_add=True,null=True)

    ROLE_CHOICES = (
        ('A','Admin'),
        ('U', 'User'),
        )
    Role = models.CharField(max_length=1,choices=ROLE_CHOICES,default='U',null=True)

    def __str__(self):
        return (self.First_Name)


class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    Name = models.CharField(max_length=50,null=True)
    Price = models.CharField(max_length=100,null=True)
    Color = models.CharField(max_length=50,null=True)
    def __str__(self):
        return (self.Name)

