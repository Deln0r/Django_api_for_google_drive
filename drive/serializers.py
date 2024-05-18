from rest_framework import serializers

class UploadFileSerializer(serializers.Serializer):
    data = serializers.CharField()
    name = serializers.CharField()