import pytest

from tests.events.conftest import TestBase
from events import views



class TestEventViews(TestBase):

    @pytest.mark.django_db
    def test_authorized_request(self):
        client = self.api_client()
        response = client.get('/')
        assert response.status_code == 200

    def test_unauthorized_request(self):
        client = self.api_client(authorized=False)
        response = client.get('/')
        assert response.status_code == 401

    def test_post_devnote(self):
        client = self.api_client()
        response = client.post('/event', json=self.devnote_body())

        assert response.status_code == 200
