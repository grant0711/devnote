# Generated by Django 4.1.7 on 2023-02-23 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DevNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date', models.DateField(editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='devnote',
            constraint=models.CheckConstraint(check=models.Q(('content__length__gt', 0)), name='content_cannot_be_empty_string'),
        ),
        migrations.AddConstraint(
            model_name='devnote',
            constraint=models.UniqueConstraint(fields=('user', 'date'), name='devnote_must_be_unique_for_date_and_user'),
        ),
    ]
