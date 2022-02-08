from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import TokenObtainPairView, TokenRefreshView, UserViewSet, UserSingupAPIView

app_name = 'user'

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/signup/', UserSingupAPIView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]