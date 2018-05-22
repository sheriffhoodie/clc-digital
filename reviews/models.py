from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete='CASCADE')
    created_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    title = models.CharField(max_length=200, unique=False)
    rating = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'title']
