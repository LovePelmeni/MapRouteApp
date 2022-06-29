# Generated by Django 3.1.14 on 2022-02-08 11:27

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Image Title')),
                ('image', models.ImageField(storage=django.core.files.storage.FileSystemStorage(), upload_to='', verbose_name='Image')),
            ],
        ),
    ]
