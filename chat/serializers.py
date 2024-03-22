from .models import User, Room, Message
from rest_framework import serializers
from users.serializers import CustomUserSerializer


class MessageSerializer(serializers.ModelSerializer):
    created_at_formatted = serializers.SerializerMethodField()
    user = CustomUserSerializer()

    class Meta:
        model = Message
        exclude = []
        depth = 1

    def get_created_at_formatted(self, obj:Message):
        # return obj.created_at.strftime("%d-%m-%Y %H:%M:%S")
        return obj.created_at.strftime("%H:%M")

class RoomSerializer(serializers.ModelSerializer):
    last_message = serializers.SerializerMethodField()
    messages = MessageSerializer(many=True, read_only=True)
    host = CustomUserSerializer()
    current_users = CustomUserSerializer()

    class Meta:
        model = Room
        fields = ["id", "host", "messages", "current_users", "last_message"]
        depth = 1
        read_only_fields = ["messages", "last_message"]

    def get_last_message(self, obj:Room):
        return MessageSerializer(obj.messages.order_by('created_at').last()).data
