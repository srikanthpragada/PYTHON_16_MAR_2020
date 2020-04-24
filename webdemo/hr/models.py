from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id} - {self.title} - {self.author} - {self.price}"
