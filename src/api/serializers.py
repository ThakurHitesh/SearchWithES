from rest_framework import serializers
from api.models import Books, Author, Publisher

class BooksSerializer(serializers.ModelSerializer):
    model = Books
    fields = '__all__'