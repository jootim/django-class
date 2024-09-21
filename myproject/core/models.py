from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User

# Create your models here.


class Toppic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Toppic, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250)

    description = models.TextField(null=True, blank=True)
    # partipants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-updated", "-created"]


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


