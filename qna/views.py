from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
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
            qs = qs.filter(title__icontains=query)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return QnaCreateSerializer
        else:
            return QnaSerializer
