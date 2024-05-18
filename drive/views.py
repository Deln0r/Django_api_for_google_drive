from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadFileSerializer
from .utils import upload_file_to_drive

class UploadFileView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            name = serializer.validated_data['name']
            file_id = upload_file_to_drive(data, name)
            return Response({'file_id': file_id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
