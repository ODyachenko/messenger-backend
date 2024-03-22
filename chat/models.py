from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser

class Room(models.Model):
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="rooms")
    current_users = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="current_rooms", blank=True, null=True)

    def __str__(self):
        return f"Room({self.host}) -> {self.current_users}"


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    text = models.TextField(max_length=500)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message({self.user} {self.room})"
    
