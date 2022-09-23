# Generated by Django 4.0.4 on 2022-07-26 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0007_slidshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Comment Name')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
        ),
    ]
