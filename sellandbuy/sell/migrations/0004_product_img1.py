# Generated by Django 3.2.6 on 2021-08-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0003_auto_20210816_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img1',
            field=models.FileField(default=None, upload_to='pictures/'),
        ),
    ]