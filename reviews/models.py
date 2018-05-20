from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete='CASCADE')
    created_at = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.body
