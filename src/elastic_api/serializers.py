from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from elastic_api.documents import BooksDocument

class BooksDocumentSerializer(DocumentSerializer):
    class Meta:
        document = BooksDocument
        fields = [
            'id',
            'title',
            'description',
            'summary',
            'authors',
            'publisher',
            'publication_date',
            'state',
            'isbn',
            'price',
            'pages',
            'stock_count',
            'tags',
        ]