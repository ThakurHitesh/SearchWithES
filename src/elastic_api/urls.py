from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from elastic_api.views import BooksDocumentViewSet

router = DefaultRouter()
books = router.register(r'books', BooksDocumentViewSet, basename='bookdocument')

urlpatterns = [
    url(r'^', include(router.urls)),
]
