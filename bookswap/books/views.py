from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import BookSerializer
from .models import Book
from .permissions import IsOwnerOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def pre_save(self, obj):
        obj.owner = self.request.user

#    def perform_create(self, serializer):
#        serializer.save(owner=self.request.user)


