from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from api.models import Books

index = Index('books')

index.settings(number_of_shards=1, number_of_replicas=1)

html_strip = analyzer(
    'html_strip',
    tokenizer = 'standard',
    filter = ['lowercase', 'snowball', 'stop'],
    char_filter = ["html_strip"] 
)

@index.doc_type
class BooksDocument(Document):
    
    id = fields.KeywordField(attr='id')
    title = fields.TextField(
        analyzer = html_strip,
        fields = {
            'raw': fields.KeywordField(),
            'suggest': fields.CompletionField()
        }
    )
    description = fields.TextField(
        analyzer = html_strip,
        fields = {
            'raw': fields.KeywordField(),
        }
    )
    summary = fields.TextField(
        analyzer = html_strip,
        fields = {
            'raw': fields.KeywordField(),
        }
    )
    authors = fields.TextField(
        attr = 'authors_indexing',
        analyzer = html_strip,
        fields = {
            'raw': fields.KeywordField()
        },
    )
    publisher = fields.TextField(
        attr = 'publisher_indexing',
        analyzer = html_strip,
        fields = {
            'raw': fields.KeywordField()
        }
    )
    publication_date = fields.DateField()
    isbn = fields.TextField(
        analyzer = html_strip,
        fields = {
            'raw': fields.KeywordField(),
        }
    )
    price = fields.FloatField()
    pages = fields.IntegerField()
    stock_count = fields.IntegerField()
    tags = fields.TextField(
        attr='tags_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.KeywordField(),
            }
        )
    class Django():
        model = Books