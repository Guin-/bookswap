from rest_framework import serializers

from .models import User
from bookswap.books.models import Book

class UserSerializer(serializers.ModelSerializer):
#    book = serializers.HyperlinkedRelatedField(view_name='book-detail',
#                                                many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'username')
