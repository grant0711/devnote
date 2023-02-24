import pytest

from tests.events.conftest import TestBase
from events import views
from events.models import DevNote



class TestEventViews(TestBase):

    def test_authorized_request(self):
        client = self.api_client()
        response = client.get('/')
        assert response.status_code == 200

    def test_unauthorized_request(self):
        client = self.api_client(authorized=False)
        response = client.get('/')
        assert response.status_code == 401

        response = client.post('/event', self.devnote_body(), format='json')
        assert response.status_code == 401

    def test_post_devnote(self):
        client = self.api_client()
        response = client.post('/event', self.devnote_body(), format='json')
        assert response.status_code == 200

        devnote = DevNote.objects.filter(user=self.user()).first()
        assert devnote

    def test_expected_failure_malformed_devnote(self):
        client = self.api_client()
        response = client.post('/event', {'malformed': 'data'}, format='json')
        assert response.status_code == 400
        assert b'ValidationError' in response.content

        devnote = DevNote.objects.filter(user=self.user()).first()
        assert not devnote

    def test_expected_failure_empty_string_devnote(self):
        body = self.devnote_body(content="")
        client = self.api_client()
        response = client.post('/event', body, format='json')
        assert response.status_code == 400
        assert b'IntegrityError' in response.content

        devnote = DevNote.objects.filter(user=self.user()).first()
        assert not devnote

    def test_update_existing_devnote(self):
        client = self.api_client()
        body = self.devnote_body()
        response = client.post('/event', body, format='json')
        assert response.status_code == 200

        devnote = DevNote.objects.filter(user=self.user(), date=body['date']).first()
        assert devnote.content == body['content']

        updated_body = body.copy()
        updated_body['content'] = "Here is some updated body content"

        response = client.post('/event', updated_body, format='json')
        assert response.status_code == 200

        devnote = DevNote.objects.filter(user=self.user(), date=body['date']).first()
        assert devnote.content == updated_body['content']

    def test_create_multiple_devnotes_different_days(self):
        client = self.api_client()
        response = client.post('/event', self.devnote_body(date='2023-02-24'), format='json')
        assert response.status_code == 200
        response = client.post('/event', self.devnote_body(date='2023-02-25'), format='json')
        assert response.status_code == 200

        devnotes = DevNote.objects.filter(user=self.user())
        assert len(devnotes) == 2
