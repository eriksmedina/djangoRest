import string
from django.forms import PasswordInput
from rest_framework import serializers
from django.contrib.auth.models import User

class CalcSerializer(serializers.Serializer):
    #password = serializers.CharField()

    def get(self, validated_data):
        TestInput =''  #validated_data.get('password')       
        return TestInput
