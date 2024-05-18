from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class UploadFileTests(APITestCase):
    def test_upload_file(self):
        url = reverse('upload-file')
        data = {'data': 'Hello, World!', 'name': 'test.txt'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('file_id', response.data)