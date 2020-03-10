from django_elasticsearch_dsl_drf.viewsets import  DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    CompoundSearchFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    FilteringFilterBackend,
    IdsFilterBackend,
    FacetedSearchFilterBackend,
    SuggesterFilterBackend
)
from elasticsearch_dsl import (
    TermsFacet,
    DateHistogramFacet,
    RangeFacet
)
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_TERM,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
    LOOKUP_QUERY_CONTAINS,
    SUGGESTER_COMPLETION
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from elastic_api.documents import BooksDocument
from elastic_api.serializers import BooksDocumentSerializer

class BooksDocumentViewSet(DocumentViewSet):
    document = BooksDocument
    serializer_class = BooksDocumentSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        CompoundSearchFilterBackend,
        FacetedSearchFilterBackend,
        SuggesterFilterBackend
    ]
    search_fields = (
        'title',
        'description',
        'summary'
    )
    faceted_search_fields = {
        'publisher': {
            'field': 'publisher.raw',
            'facet': TermsFacet,
            'enabled': True
        },
        'publication_date': {
            'field': 'publication_date',
            'facet': DateHistogramFacet,
            'options': {
                'interval' : 'year'
            },
            'enabled': True
        },
        'stock_count':{
            'field': 'stock_count',
            'facet': RangeFacet,
            'options': {
                'ranges':[
                    ("<5",(None, 5)),
                    ("6-20",(6, 20)),
                    ("21-50",(21, 50)),
                    (">50",(50, None)),
                ]
            },
            'enabled': True
        }
    }
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
                LOOKUP_QUERY_CONTAINS,
                LOOKUP_FILTER_TERM,
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

    suggester_fields = {
        'title':{
            'field': 'title.suggest',
            'suggesters': [
                SUGGESTER_COMPLETION,
            ],
        }
    }
    
    ordering_fields = {
        'id': 'id',
        'title': 'title.raw',
        'price': 'price',
        'publication_date': 'publication_date',
    }
    
    ordering = ('id', 'title', 'price')