import pytest

from django.test import TransactionTestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient



class TestBase(TransactionTestCase):
    
    def user(self, username='Test'):
        return User.objects.filter(username=username).first() or \
            User.objects.create(username=username)

    def devnote_body(self, content='Test content', date='2023-02-24'):
        return {
            'content': content,
            'date': date
        }

    def api_client(self, authorized=True):
        """
        APIClient for test purposes
        """
        client = APIClient()
        if authorized:
            token = Token.objects.create(user=self.user())
            client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        return client
