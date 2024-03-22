from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'avatar')

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'avatar')


# class UserRegistrationSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')

# class UserInfoSerializer(UserSerializer):
#     class Meta(UserSerializer.Meta):
#         fields = ('id', 'first_name', 'last_name', 'username')
