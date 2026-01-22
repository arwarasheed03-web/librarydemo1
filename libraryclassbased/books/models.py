from django.db import models

#Table definition
class Book(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    pages=models.IntegerField()
    price = models.IntegerField()
    language=models.CharField()
    image=models.ImageField(upload_to='books')
