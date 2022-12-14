# Generated by Django 4.1.1 on 2022-10-19 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('edition', models.IntegerField(default=0)),
                ('author_first_name', models.CharField(max_length=100)),
                ('author_last_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookForSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_condition', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('comment', models.TextField()),
                ('available', models.BooleanField(default=True)),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.book')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=0)),
                ('major', models.CharField(max_length=100)),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.school')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sold', models.DateField(verbose_name='Transaction Date')),
                ('book_listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.bookforsale')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.user')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolUsesBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('ISBN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.book')),
                ('school_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.school')),
            ],
        ),
        migrations.CreateModel(
            name='PinnedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_listing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.bookforsale')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.user')),
            ],
        ),
        migrations.AddField(
            model_name='bookforsale',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_exchange.user'),
        ),
        migrations.AddConstraint(
            model_name='transaction',
            constraint=models.UniqueConstraint(fields=('buyer_id', 'book_listing_id'), name='unique_buyer_book_listing_combination'),
        ),
        migrations.AddConstraint(
            model_name='schoolusesbook',
            constraint=models.UniqueConstraint(fields=('school_name', 'ISBN'), name='unique_school_ISBN_combination'),
        ),
        migrations.AddConstraint(
            model_name='pinnedbook',
            constraint=models.UniqueConstraint(fields=('user_id', 'book_listing_id'), name='unique_user_book_listing_combination'),
        ),
    ]
