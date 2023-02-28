from django.urls import path
from .views import AuthorView, BookDetailView, ListBookView, AuthorDetailView

urlpatterns = [
    path("books/", ListBookView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
    path("authors/", AuthorView.as_view()),
    path("authors/<str:pk>/books/", AuthorDetailView.as_view()),
]
