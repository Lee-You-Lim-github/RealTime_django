from django.db.models import Q
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from booking.models import Booking
from booking.paginations.BookPagination import BookPagination
from booking.serializers import BookingCreateSerializer, BookingListSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    pagination_class = BookPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['day', "time"]

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST' or method == 'PATCH':
            return BookingCreateSerializer
        else:
            return BookingListSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        user_id = self.request.query_params.get("user_id", "")
        shop_id = self.request.query_params.get("shop_id", "")
        visit_status = self.request.query_params.get("visit_status", "")
        query = self.request.query_params.get("query", "")

        conditions = Q(user_id__username__icontains=query) | Q(user_id__telephone__icontains=query)
        if query:
            qs = qs.filter(conditions | Q(shop_id__name__icontains=query))

        user_id_conditions = Q(user_id__id__exact=user_id)
        shop_id_conditions = Q(shop_id__id__exact=shop_id)
        visit_status_conditions = Q(user_id__id__exact=user_id) & Q(visit_status__exact=visit_status)

        if user_id:
            qs = qs.filter(user_id_conditions)

        if shop_id:
            qs = qs.filter(shop_id_conditions)

        if visit_status:
            qs = qs.filter(visit_status_conditions)

        return qs






