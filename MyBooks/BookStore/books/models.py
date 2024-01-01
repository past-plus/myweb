from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=32)
    author=models.TextField()
    publication_date=models.DateTimeField(auto_now=True)
