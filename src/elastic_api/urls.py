from django.urls import path
from elastic_api.views import BaseDocumentViewSet

urlpatterns = [
    path('', BaseDocumentViewSet.as_view(), name='elastic')
]
