# Generated by Django 4.0.3 on 2022-05-28 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0002_alter_service_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='user',
        ),
    ]
