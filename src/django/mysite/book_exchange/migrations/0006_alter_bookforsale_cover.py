# Generated by Django 4.1.1 on 2022-11-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_exchange', '0005_bookforsale_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookforsale',
            name='cover',
            field=models.ImageField(default='covers/default.jpg', upload_to='covers/'),
        ),
    ]
