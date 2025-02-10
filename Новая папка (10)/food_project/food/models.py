from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
