import datetime

import pytest

from django.db import IntegrityError
from tests.events.conftest import TestBase

from events.models import DevNote


class TestEventModels(TestBase):

    @pytest.mark.django_db
    def test_devnote_insert(self):
        devnote = DevNote.objects.create(
            user=self.user(),
            content="Test content",
            date=datetime.datetime.now(datetime.timezone.utc).date()
        )

        devnote = DevNote.objects.get(id=devnote.id)
        assert devnote.content == "Test content"

    @pytest.mark.django_db
    def test_devnote_cannot_be_empty_string(self):
        with pytest.raises(IntegrityError):
            devnote = DevNote.objects.create(
                user=self.user(),
                content="",
                date=datetime.datetime.now(datetime.timezone.utc).date()
            )

    @pytest.mark.django_db
    def test_multiple_devnotes_cannot_exist_for_same_user_and_date(self):
        devnote = DevNote.objects.create(
            user=self.user(),
            content="Test content",
            date=datetime.datetime.now(datetime.timezone.utc).date()
        )

        with pytest.raises(IntegrityError):
            devnote = DevNote.objects.create(
                user=self.user(),
                content="Test content",
                date=datetime.datetime.now(datetime.timezone.utc).date()
            )

        devnote = DevNote.objects.create(
            user=self.user(),
            content="A devnote from a later date",
            date=(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)).date()
        )
