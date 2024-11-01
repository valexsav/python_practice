# Generated by Django 5.1.2 on 2024-10-25 11:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('book', '0003_alter_book_publication_year_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(help_text='Author of the book', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='author.author'),
        ),
    ]
