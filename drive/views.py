from rest_framework.views import APIView  # Базовый класс для представлений DRF
from rest_framework.response import Response  # Объект для формирования ответа API
from rest_framework import status  # Коды статусов HTTP
from .serializers import UploadFileSerializer  # Сериализатор для валидации входных данных
from .utils import upload_file_to_drive  # Функция для загрузки файла в Google Drive

class UploadFileView(APIView):
    """
    Представление для загрузки файлов в Google Drive через API.

    Обрабатывает POST-запросы с данными файла и его именем.
    Валидирует входные данные с помощью сериализатора.
    Загружает файл в Google Drive и возвращает ID загруженного файла.
    """

    def post(self, request, *args, **kwargs):
        """
        Обработчик POST-запроса.

        Args:
            request: Объект запроса Django.

        Returns:
            Response: Ответ API с ID загруженного файла или ошибками валидации.
        """

        # Сериализация входных данных для валидации
        serializer = UploadFileSerializer(data=request.data) 
        
        if serializer.is_valid():  # Если данные прошли валидацию
            data = serializer.validated_data['data']  # Извлекаем содержимое файла
            name = serializer.validated_data['name']  # Извлекаем имя файла

            # Загружаем файл в Google Drive и получаем его ID
            file_id = upload_file_to_drive(data, name)  

            # Возвращаем успешный ответ с ID загруженного файла
            return Response({'file_id': file_id}, status=status.HTTP_201_CREATED)  
        
        # Возвращаем ответ с ошибками валидации, если данные некорректны
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 