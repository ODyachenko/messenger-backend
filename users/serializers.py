from djoser.serializers import UserCreateSerializer, UserSerializer

class UserRegistrationSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')

class UserInfoSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('first_name', 'last_name', 'username')
