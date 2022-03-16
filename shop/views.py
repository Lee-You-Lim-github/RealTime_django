from django.db.models import Q
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from shop.models import Shop
from shop.paginations.ShopPagination import ShopPagination
from shop.serializers import ShopCreateSerializer, ShopListSerializer


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    pagination_class = ShopPagination

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST' or method == 'PATCH':
            return ShopCreateSerializer
        else:
            return ShopListSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        conditions = Q(name__icontains=query) | Q(shop_num__icontains=query)
        if query:
            qs = qs.filter(conditions)

        return qs

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


