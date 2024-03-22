from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
# from .serializers import UserSerializer
from users.serializers import CustomUserSerializer

class CustomUserViewSet(UserViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'me':
            return CustomUserSerializer
        return super().get_serializer_class()

