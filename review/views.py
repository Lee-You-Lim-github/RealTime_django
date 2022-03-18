from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from review.models import Review
from review.serializers import ReviewSerializer, ReviewCreateSerializer


class ReviewPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1

    def paginate_queryset(self, queryset, request, view=None):
        if "all" in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ReviewCreateSerializer
        else:
            return ReviewSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        user_id = self.request.query_params.get("user_id", "")
        conditions = Q(book_id__user_id__id=user_id) | Q(wait_id__user_id__id=user_id)
        if user_id:
            qs = qs.filter(conditions)

        return qs

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [AllowAny()]
    #     return [IsAuthenticated()]




