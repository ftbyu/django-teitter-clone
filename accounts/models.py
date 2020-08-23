from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = "default.jpg", upload_to = "images")

    def __str__(self):
        return self.user.username

class Relationships(models.Model):
    follower = models.ForeignKey(User, related_name = 'follower', on_delete = models.CASCADE)
    followee = models.ForeignKey(User, related_name = 'followee', on_delete = models.CASCADE)
