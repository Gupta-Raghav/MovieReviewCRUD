from django.db import models
from .movie import Movie

class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    class Meta: 
        db_table = "review"