# Generated by Django 4.0.3 on 2022-08-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0009_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_quote',
            field=models.TextField(null=True, verbose_name='Blog Quote'),
        ),
    ]