# Generated by Django 5.0.7 on 2024-07-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_userfiles_userfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
