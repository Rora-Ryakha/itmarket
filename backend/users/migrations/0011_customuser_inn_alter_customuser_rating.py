# Generated by Django 5.0.7 on 2024-07-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_contacts_alter_customuser_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='inn',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='rating',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
