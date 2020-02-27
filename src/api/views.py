from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Books, Author, Publisher
from api.serializers import BooksSerializer


class BooksAPIView(APIView):
    serializer_class = BooksSerializer
    model = Books

    def get(self, request):
        queryset = Books.objects.all()
        data = BooksSerializer(queryset, many=True).data
        Response(data, status.HTTP_200_OK)
