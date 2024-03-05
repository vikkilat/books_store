import json
import os
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from books.models import Book

FILE_DIR = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(FILE_DIR, 'books.json')) as f:
            data = json.load(f)

            for book_data in data:
                published_date_str = book_data['publishedDate']['$date']
                published_date_obj = datetime.strptime(
                    published_date_str, '%Y-%m-%dT%H:%M:%S.%f%z')
                if 'categories' not in data:
                    book_data['category'] = 'News'

            book = Book(
                title=book_data['title'],
                isbn=book_data['isbn'],
                pageCount=book_data['pageCount'],
                publishedDate=published_date_obj,
                thumbnailUrl=book_data['thumbnailUrl'],
                shortDescription=book_data['shortDescription'],
                longDescription=book_data['longDescription'],
                status=book_data['status'],
                authors=book_data['authors'],
                categories=book_data['categories']
            )
            book.save()
        print('finished')
