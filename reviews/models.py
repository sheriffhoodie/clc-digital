from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete='CASCADE')
    title = models.CharField(max_length=200, unique=False)
    rating = models.IntegerField(default=3, validators=[MaxValueValidator(5), MinValueValidator(0)])
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reviews:all')

    class Meta:
        ordering = ['-created_at']
