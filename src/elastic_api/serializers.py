from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from elastic_api.documents import BooksDocument

class BooksDocumentSerializer(DocumentSerializer):
    class Meta:
        model = BooksDocument
        fields = [
            'id',
            'title',
            'description',
            'summary',
            'publisher',
            'publication_date',
            'state',
            'isbn',
            'price',
            'pages',
            'stock_count',
            'tags',
        ]