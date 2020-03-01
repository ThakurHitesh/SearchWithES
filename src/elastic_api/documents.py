from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from api.models import Books

index = Index('books')

index.settings(number_of_shards=1, number_of_replicas=1)

html_strip = analyzer(
    'html_strip',
    tokenizer = 'standard',
    filter = ['lowercase', 'snowball', 'stop', 'standard'],
    char_filter = ["html_strip"] 
)

@index.doc_type
class BooksDocument(Document):
    
    id = fields.IntegerField(attr=id)
    title = fields.StringField(
        analyzer = html_strip,
        fields = {
            'raw': fields.StringField(analyzer = 'keyword'),
        }
    )
    description = fields.StringField(
        analyzer = html_strip,
        fields = {
            'raw': fields.StringField(analyzer = 'keyword'),
        }
    )
    summary = fields.StringField(
        analyzer = html_strip,
        fields = {
            'raw': fields.StringField(analyzer = 'keyword'),
        }
    )
    authors = fields.StringField(
        attr = 'authors_indexing'
        analyzer = html_strip,
        fields = {
            'raw': fields.StringField(analyzer = 'keyword', multi = True)
        },
        multi = True
    )
    publisher = fields.StringField(
        attr = 'publisher_indexing'
        analyzer = html_strip,
        fields = {
            'raw': fields.StringField(analyzer = 'keyword')
        }
    )
    publication_date = fields.DateField()
    isbn = fields.StringField(
        analyzer = html_strip,
        fields = {
            'raw': fields.StringField(analyzer = 'keyword'),
        }
    )
    price = fields.FloatField()
    pages = fields.IntegerField()
    stock_count = models.IntegerField()
    tags = fields.StringField(
        attr='tags_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.StringField(analyzer='keyword', multi=True),
            },
        multi=True
        )