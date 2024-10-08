# Generated by Django 5.0.7 on 2024-07-21 16:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0010_alter_card_owner_alter_cardcomment_card_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cardcomment',
            name='related_user',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
