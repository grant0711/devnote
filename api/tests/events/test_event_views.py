import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from events import views



class TestEventViews():

    @pytest.mark.django_db
    def test_authorized_request(self):
        user = User.objects.create(username='test')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        response = client.get('/')
        assert response.status_code == 200

    def test_unauthorized_request(self):
        response = APIClient().get('/')
        assert response.status_code == 401
