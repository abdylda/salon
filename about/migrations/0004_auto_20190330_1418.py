# Generated by Django 2.1.7 on 2019-03-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20190330_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation',
            name='info',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='partnership',
            name='about',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]