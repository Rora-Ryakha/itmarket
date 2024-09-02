# Generated by Django 5.0.7 on 2024-07-31 08:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0014_card_properties'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='is_approved',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='num_of_views',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='card',
            name='rating',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='cardcomment',
            name='card',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='publications.card'),
        ),
        migrations.AlterField(
            model_name='cardcomment',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cardcomment',
            name='related_user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
