# Generated by Django 4.1.1 on 2022-11-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_exchange', '0005_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]
