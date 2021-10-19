# Generated by Django 3.2.6 on 2021-08-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PRODUCT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('mainimg', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('img3', models.ImageField(upload_to='pics')),
                ('img4', models.ImageField(upload_to='pics')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('contactnumber', models.CharField(max_length=100)),
            ],
        ),
    ]