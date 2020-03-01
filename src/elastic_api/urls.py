from django.urls import include, path
from rest_framework.routers import DefaultRouter
from elastic_api.views import BooksDocumentViewSet

router = DefaultRouter()
router.register('books', BooksDocumentViewSet, basename='bookdocument')

urlpatterns = [
    path('', include(router.urls)),
]
