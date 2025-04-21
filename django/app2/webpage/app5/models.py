from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} by {self.author}"
