import uuid
from django.utils import timezone
from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ('created_at',)
        abstract = True

class Author(TimeStamp):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Publisher(TimeStamp):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    website = models.URLField(blank=True, null=True)

class Tag(TimeStamp):
    name = models.CharField(max_length=100, unique=True)

class Books(TimeStamp):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True, blank=True)
    summary = models.TextField(max_length=2000, null=True, blank=True)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField(default=timezone.now)
    isbn = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.PositiveIntegerField()
    stock_count = models.PositiveIntegerField()
    tags = models.ManyToManyField('Tag', blank=True)

    @property
    def authors_indexing(self):
        return [ author.name for author in self.authors.all()]

    @property
    def publisher_indexing(self):
        if self.publisher is not None:
            return self.publisher.name

    @property
    def tags_indexing(self):
        return [ tag.name for tag in self.tags.all()]