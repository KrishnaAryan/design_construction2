from rest_framework import serializers

class TestingProjectDetailsSerializer(serializers.Serializer):
    id=serializers.CharField(required=True)

class EmailValidationSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)

# class OtpVerifyValidationSerializer(serializers.Serializer):
#     email=serializers.CharField(required=True)
#     otp=serializers.IntegerField(required=True)

class ResetPasswordValidationSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True)
    confirm_password=serializers.CharField(required=True)
