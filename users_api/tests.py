from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UploadCSVTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_valid_csv(self):
        csv_data = "name,email,age\nRose Grace,rose@example.com,30\nJack John,jack@example.com,25"
        csv_file = SimpleUploadedFile("test.csv", csv_data.encode(), content_type="text/csv")

        response = self.client.post('/api/upload/', {'file': csv_file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)

    def test_upload_invalid_csv(self):
        csv_data = "name,email,age\n,invalid_email,150"
        csv_file = SimpleUploadedFile("test.csv", csv_data.encode(), content_type="text/csv")

        response = self.client.post('/api/upload/', {'file': csv_file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('failed', response.data)
