from rest_framework import viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OrigTokenObtainPairView,
    TokenRefreshView as OrigTokenRefreshView,
)
from user.serializers import TokenObtainPairSerializer, UserCreationSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from user.models import User
from user.serializers import UserSerializer

# User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class= UserSerializer
    permission_classes = [AllowAny]   # DRF 디폴트 설정



class UserSingupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]

class TokenObtainPairView(OrigTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(OrigTokenRefreshView):
    pass
