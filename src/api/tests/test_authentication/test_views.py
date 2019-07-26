from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.tests.testingutils.factory.users import create_user


class AuthenticationViewsAPITestCase(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_signin_views_success(self):
        url = reverse('signin')
        data = {
            'username': self.user.username,
            'password': '123456',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_signin_views_email_not_informed(self):
        url = reverse('signin')
        data = {
            'username': '',
            'password': '123456',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_views_password_not_informed(self):
        url = reverse('signin')
        data = {
            'username': self.user.username,
            'password': '',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signin_views_wrong_password(self):
        url = reverse('signin')
        data = {
            'username': self.user.username,
            'password': '654321',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_signup_views_success(self):
        url = reverse('signup')
        data = {
            'username': 'mauro',
            'email': 'mauro@activesoft.com',
            'password': '123456',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_views_password_not_informed(self):
        url = reverse('signup')
        data = {
            'username': 'mauro',
            'email': 'mauro@activesoft.com',
            'password': '',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_views_username_not_informed(self):
        url = reverse('signup')
        data = {
            'username': '',
            'email': 'mauro@activesoft.com',
            'password': '123456',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_signup_views_username_already_exists(self):
        url = reverse('signup')
        data = {
            'username': self.user.username,
            'email': 'mauro@activesoft.com',
            'password': '123456',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
