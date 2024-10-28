# Generated by Django 5.1.2 on 2024-10-28 18:57

from django.db import migrations


def create_another_book(apps, schema_editor):
    Book = apps.get_model('book', 'Book')
    Author = apps.get_model('author', 'Author')
    
    Book.objects.get_or_create(
        title='Moby Dick',
        publication_year=1851,
        author=Author.objects.get_or_create(
            first_name='Herman',
            birth_date='1790-01-01',
            last_name='Melville',
        )[0],
    )


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_author'),
    ]

    operations = [
        migrations.RunPython(create_another_book),
    ]
