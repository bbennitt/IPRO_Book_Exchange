# Generated by Django 4.1.1 on 2022-11-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_exchange', '0008_alter_bookforsale_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookforsale',
            name='cover',
            field=models.ImageField(default='book_exchange/media/covers/default.jpg', upload_to='book_exchange/media/covers/'),
        ),
    ]
