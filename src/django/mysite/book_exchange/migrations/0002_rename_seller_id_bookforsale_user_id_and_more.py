# Generated by Django 4.1.1 on 2022-10-19 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_exchange', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookforsale',
            old_name='seller_id',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='bookforsale',
            name='ISBN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='book_exchange.book'),
        ),
        migrations.AlterField(
            model_name='pinnedbook',
            name='book_listing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='book_exchange.bookforsale'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='book_listing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book_exchange.bookforsale'),
        ),
        migrations.AlterField(
            model_name='user',
            name='school_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book_exchange.school'),
        ),
    ]