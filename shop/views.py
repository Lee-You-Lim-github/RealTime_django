from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from shop.models import Shop, Review
from shop.serializers import ShopCreateSerializer, ReviewSerializer, ShopReadSerializer


class ShopCreateViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopCreateSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class ShopReadViewSet(ModelViewSet):
    queryset = Shop.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST' or method == 'PATCH':
            return ShopCreateSerializer
        else:
            return ShopReadSerializer

    # def get_queryset(self):
    #     qs= super().get_queryset()
    #
    #     query=self.request.query_params.get("query","")
    #     if query:
    #         qs=qs.filter(champion__icontains=query)
    #
    #     return qs


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]