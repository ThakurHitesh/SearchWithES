from django_elasticsearch_dsl_drf.viewsets import  BaseDocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    SearchFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    IdsFilterBackend
)
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
    LOOKUP_QUERY_CONTAINS
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from elastic_api.documents import BooksDocument
from elastic_api.serializers import BooksDocumentSerializer

class BooksDocumentViewSet(BaseDocumentViewSet):
    document = BooksDocument
    serializer_class = BooksDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend
    ]
    search_fields = (
        'title',
        'description',
        'summary'
    )
    filter_fields = {
        'id' : {
            'field' : 'id',
            'lookups' : [
                LOOKUP_FILTER_TERMS,
            ]
        },
        'title': 'title.raw',
        'publisher': 'publisher.raw',
        'publication_date': 'publication_date',
        'state': 'state.raw',
        'isbn': 'isbn.raw',
        'price': {
            'field' : 'price',
            'lookups' : [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ]
        },
        'pages': {
            'field' : 'pages',
            'lookups' : [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ]
        },
        'stock_count': {
            'field' : 'stock_count',
            'lookups' : [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_GT,
                LOOKUP_QUERY_GTE,
                LOOKUP_QUERY_LT,
                LOOKUP_QUERY_LTE,
            ]
        },
        'tags': {
            'field': 'tags.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
                LOOKUP_QUERY_CONTAINS
            ],
        },
        'authors': {
            'field': 'authors.raw',
            'lookups': [
                LOOKUP_FILTER_TERMS,
                LOOKUP_FILTER_PREFIX,
                LOOKUP_FILTER_WILDCARD,
                LOOKUP_QUERY_IN,
                LOOKUP_QUERY_EXCLUDE,
            ],
        },
    }
    
    ordering_fields = {
        'id': 'id',
        'title': 'title.raw',
        'price': 'price',
        'publication_date': 'publication_date',
    }
    
    ordering = ('id', 'title', 'price')