from rest_framework import serializers

class TestingProjectDetailsSerializer(serializers.Serializer):
    id=serializers.CharField(required=True)