from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from . import models
from datetime import date

class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        book = models.Book.objects.create(
            title="Demo",
            description="Description",
            author="Author",
            isbn="1111111111111",
            published_date=date(2023, 1, 1)
        )
        url = reverse('api:books')
        response = self.client.get(url, format='json')

        assert response.status_code == status.HTTP_200_OK

        returned_book = response.json()[0]

        assert returned_book["title"] == book.title
        assert returned_book["description"] == book.description
        assert returned_book["author"] == book.author

    def test_create_and_delete_book(self):
        data = {
            "title": "To Delete",
            "description": "This book will be deleted",
            "author": "Someone",
            "isbn": "1234567890123",
            "published_date": "2024-01-01"
        }

    
        create_response = self.client.post(reverse('api:books'), data, format='json')
        assert create_response.status_code == status.HTTP_201_CREATED
        assert create_response.data['isbn'] == data['isbn']

        delete_response = self.client.delete(reverse('api:books'), data={"isbn": data["isbn"]}, format='json')
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT

class HealthViewTest(APITestCase):
    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'ok'
