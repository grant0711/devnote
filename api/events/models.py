import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Length


models.TextField.register_lookup(Length)


class DevNote(models.Model):
    id             = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user           = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=False)
    content        = models.TextField(null=False)
    date           = models.DateField(null=False, editable=False)
    created_at     = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
    last_updated   = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="content_cannot_be_empty_string",
                check=models.Q(content__length__gt=0),
            ),
            models.UniqueConstraint(
                name="devnote_must_be_unique_for_date_and_user",
                fields=['user', 'date']
            )
        ]


