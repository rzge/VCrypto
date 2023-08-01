from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    friends = models.ManyToManyField('CustomUser', blank=True, symmetrical=True)
    bitcoin_address = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username


class FriendRequest(models.Model):
    sender = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='receiver')
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.username

# Create your models here.
