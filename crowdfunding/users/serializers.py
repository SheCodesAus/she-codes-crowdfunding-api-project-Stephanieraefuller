from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField(max_length=150, blank=False)
    last_name = serializers.CharField(max_length=150, blank=False)
    email = serializers.CharField(max_length=200, blank=False)
    username = serializers.CharField(max_length=200, blank=False)
    password = serializers.CharField(write_only = True, blank=False)

    angel = serializers.BooleanField()
    founder = serializers.BooleanField()


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
