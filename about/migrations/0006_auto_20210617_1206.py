# Generated by Django 2.1.7 on 2021-06-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_aboutpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpicture',
            name='photo',
            field=models.ImageField(upload_to='images/about_picture/', verbose_name='Фото'),
        ),
    ]
