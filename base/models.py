import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(unique=True, null=False)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Topic(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    # One User can have many rooms   1toM relationship
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # one topic can be in many rooms
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name="Participants", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.name


class Message(models.Model):

    body = models.TextField(null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["updated", "created"]

    def __str__(self):
        return self.body[0:50]
