from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, default='0000000000000')
    published_date = models.DateField()

    def __str__(self):
        return self.title
