from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes fields from requests: in this case a 'name' field"""
    name = serializers.CharField(max_length=10)