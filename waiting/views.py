from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from waiting.models import Waiting
from waiting.serializers import WaitingCreateSerializer, WaitingListSerializer
from django.db.models import Q
from rest_framework import filters
from waiting.paginations.WaitingPagination import WaitingPagination

class WaitingViewSet(ModelViewSet):
    queryset = Waiting.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['wait_date']
    pagination_class = WaitingPagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "PUT" or method == "POST" or method == "PATCH":
            return WaitingCreateSerializer
        else:
            return WaitingListSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        conditions = Q(user_id__username__icontains=query) | Q(user_id__telephone__icontains=query)
        if query:
            qs = qs.filter(conditions)

        shop_id = self.request.query_params.get("shop_id", "")
        shop_id_conditions = Q(shop_id__id__exact=shop_id)
        if shop_id:
            qs = qs.filter(shop_id_conditions)

        user_id = self.request.query_params.get("user_id", "")
        user_id_conditions = Q(user_id__id__exact=user_id)
        if user_id:
            qs = qs.filter(user_id_conditions)

        return qs

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     return [IsAuthenticated()]


