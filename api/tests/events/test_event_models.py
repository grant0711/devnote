import datetime

import pytest

from django.contrib.auth.models import User
from django.test import TransactionTestCase
from django.db import IntegrityError

from events.models import DevNote


class TestEventModels(TransactionTestCase):

    @pytest.mark.django_db
    def test_devnote_insert(self):
        user = User.objects.create(username='Test')
        devnote = DevNote.objects.create(
            user=user,
            content="Test content",
            date=datetime.datetime.now(datetime.timezone.utc).date()
        )

        devnote = DevNote.objects.get(id=devnote.id)
        assert devnote.content == "Test content"

    @pytest.mark.django_db
    def test_devnote_cannot_be_empty_string(self):
        user = User.objects.create(username='Test')
        with pytest.raises(IntegrityError):
            devnote = DevNote.objects.create(
                user=user,
                content="",
                date=datetime.datetime.now(datetime.timezone.utc).date()
            )

    @pytest.mark.django_db
    def test_multiple_devnotes_cannot_exist_for_same_user_and_date(self):
        user = User.objects.create(username='Test')

        devnote = DevNote.objects.create(
            user=user,
            content="Test content",
            date=datetime.datetime.now(datetime.timezone.utc).date()
        )

        with pytest.raises(IntegrityError):
            devnote = DevNote.objects.create(
                user=user,
                content="Test content",
                date=datetime.datetime.now(datetime.timezone.utc).date()
            )

        devnote = DevNote.objects.create(
            user=user,
            content="A devnote from a later date",
            date=(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1)).date()
        )
