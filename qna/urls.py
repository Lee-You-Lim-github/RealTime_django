from django.urls import path, include
from rest_framework.routers import DefaultRouter
from qna import views

app_name = "Qna"

router = DefaultRouter()
router.register("qna", views.QnaViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]