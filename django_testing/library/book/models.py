from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=80)
    publication_year = models.PositiveIntegerField()


    author = models.ForeignKey(
        'author.Author',
        on_delete=models.PROTECT,
        related_name='books',
        )
    
    def __str__(self):
        return f'{self.title} ({self.publication_year})'
