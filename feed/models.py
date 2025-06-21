from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feed(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link post to creator
