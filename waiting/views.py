from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shop.models import Shop
from waiting.models import Waiting
from waiting.serializers import WaitingCreateSerializer, WaitingListSerializer
from django.db.models import Q
from rest_framework import filters, status
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
            qs = qs.filter(conditions | Q(shop_id__name__icontains=query))

        shop_id = self.request.query_params.get("shop_id", "")
        shop_id_conditions = Q(shop_id__id__exact=shop_id)
        if shop_id:
            qs = qs.filter(shop_id_conditions)

        user_id = self.request.query_params.get("user_id", "")
        user_id_conditions = Q(user_id__id__exact=user_id)
        if user_id:
            qs = qs.filter(user_id_conditions)

        wait_visit_status = self.request.query_params.get("wait_visit_status", "")
        wait_cancel = self.request.query_params.get("wait_cancel", "")
        wait_visit_status_conditions = \
            Q(wait_visit_status__exact=wait_visit_status) & \
            Q(shop_id__id__exact=shop_id) & \
            Q(wait_cancel__exact=wait_cancel)

        if shop_id and wait_visit_status and wait_cancel:
            qs = qs.filter(wait_visit_status_conditions)

        visit_status_conditions = Q(wait_visit_status__exact=wait_visit_status)
        if wait_visit_status:
            qs = qs.filter(visit_status_conditions)

        return qs

    def create(self, request, *args, **kwargs):
        #??????????????? ???????????? ????????? ?????? shop_id ????????????
        shop_id = request.data["shop_id"]
        #shop_id??? shop??? pk??? id??? ??????
        shop = Shop.objects.get(id=shop_id)
        #?????? ??? shop??? wait_State??? 1?????? 400??????
        if shop.wait_state == "1":
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # waiting??? ?????????????????? ????????????
        serializer = self.get_serializer(data=request.data)
        #???????????????????????? ??????
        if serializer.is_valid():
            serializer.save()
        #??????????????? ??????????????? ??????    
        else:
            return Response(serializer.errors)
        # ?????????????????? ???????????? ????????? ???????????? ?????????
        return Response(serializer.data)



