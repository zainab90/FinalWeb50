# Generated by Django 4.0.3 on 2022-08-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0011_blog_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_vid_content',
            field=models.TextField(null=True, verbose_name='Blog Video Content'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_vid_url',
            field=models.URLField(null=True),
        ),
    ]
