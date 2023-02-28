from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from django.shortcuts import get_object_or_404


class ListBookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        route_parameter = self.request.query_params.get("author")

        if route_parameter:
            queryset = Book.objects.filter(author__name__icontains=route_parameter)
            return queryset

        return super().get_queryset()


class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, pk=self.kwargs["pk"])
        return serializer.save(author=author)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
