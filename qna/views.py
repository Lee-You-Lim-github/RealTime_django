from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from qna.models import Qna
from qna.serializers import QnaSerializer, QnaCreateSerializer

#페이징 10개씩
class QnaPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1



class QnaViewSet(viewsets.ModelViewSet):
    queryset = Qna.objects.all()
    serializer_class = QnaSerializer
    pagination_class = QnaPagination




#제목으로 검색
    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(qna_title__icontains=query)

        user_id = self.request.query_params.get("user_id", "")
        user_id_conditions = Q(user_id__id__exact=user_id)
        if user_id:
            qs = qs.filter(user_id_conditions)

        authority = self.request.query_params.get("authority", "")
        authority_conditions = Q(user_id__authority__exact=authority)
        if authority:
            qs = qs.filter(authority_conditions)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST' or method == 'PATCH':
            return QnaCreateSerializer
        else:
            return QnaSerializer

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     return [IsAuthenticated()]
    #
