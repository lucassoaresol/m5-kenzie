from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    estimated_time_to_read = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "pages", "estimated_time_to_read", "author"]
        read_only_fields = ["author"]

    def get_estimated_time_to_read(self, obj: Book):
        time_to_read = 3 * obj.pages

        return f"{time_to_read} minutes"
