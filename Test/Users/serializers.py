from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

class UserProfileSerialier(serializers.ModelSerializer):
    user = UserSerialier(read_only= True, many=False)   #Nested Serializers
    class Meta:
        model = UserProfile
        fields = ('Phone_No', 'Country' , 'First_Name', 'Last_Name', 'Role', 'user')

    def create(self, validated_data):
        user = validated_data.pop('user')
        print('user',user)
        profile = UserProfile.objects.create(**validated_data)
        for user_data in user:
            User.objects.create(profile = profile , **user_data)
        return profile


    def update(self, instance, validated_data):
        print('validated_data ... ',validated_data)
        instance.First_Name = validated_data.get('First_Name', instance.First_Name)
        instance.Last_Name = validated_data.get('Last_Name', instance.Last_Name)
        instance.Phone_No = validated_data.get('Phone_No', instance.Phone_No)
        instance.Country = validated_data.get('Country', instance.Country)
        instance.Role = validated_data.get('Role', instance.Role)
        instance.save()
        return instance


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('user', 'Name', 'Color', 'Price', 'id')

        def update(self, instance, validated_data):

            instance.Name = validated_data.get('Name', instance.Name)
            instance.Color = validated_data.get('Color', instance.Color)
            instance.Price = validated_data.get('Price', instance.Price)
            instance.save()
            return instance
