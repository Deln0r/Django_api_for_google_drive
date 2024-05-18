from django.urls import reverse  # Импортируем функцию для получения URL по имени маршрута
from rest_framework.test import APITestCase  # Импортируем базовый класс для тестирования представлений DRF
from rest_framework import status  # Импортируем коды статусов HTTP

class UploadFileTests(APITestCase):
    """
    Класс, содержащий тесты для проверки функциональности загрузки файла.
    """

    def test_upload_file(self):
        """
        Тестирует успешную загрузку файла через API.
        """

        # Получаем URL для вызова представления по имени маршрута ('upload-file').
        url = reverse('upload-file') 

        # Создаем словарь с данными, которые будут отправлены в запросе.
        # 'data' - содержимое файла, 'name' - имя файла.
        data = {'data': 'Hello, World!', 'name': 'test.txt'} 

        # Выполняем POST-запрос к API.
        # 'url' - адрес представления, 'data' - данные для отправки, 'format' - формат данных ('json').
        response = self.client.post(url, data, format='json')

        # Проверяем, что код ответа соответствует успешному созданию ресурса (201 Created).
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

        # Проверяем, что в ответе от сервера есть поле 'file_id'.
        self.assertIn('file_id', response.data) 
