from books.models import Book, Author
from django.core.management.base import BaseCommand, CommandParser
from random import randint


class Command(BaseCommand):
    help = "Create books with one author associated"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "amount", type=int, help="Indicated the number of books to be created"
        )
        return super().add_arguments(parser)

    def handle(self, *args, **kwargs):
        book_amount = kwargs.get("amount")
        author_names = ["Joao Cezar", "Joao Paulo", "Maria Fernanda"]

        authors = [Author(name=author_name) for author_name in author_names]

        authors_list = Author.objects.bulk_create(authors)
        authors_count = len(authors_list)

        books = [
            Book(
                title=f"Livro {str(index).zfill(3)}",
                pages=randint(30, 500),
                author=authors_list[randint(0, authors_count - 1)],
            )
            for index in range(1, book_amount + 1)
        ]

        Book.objects.bulk_create(books)

        self.stdout.write(self.style.SUCCESS(f"{book_amount} books created!"))
