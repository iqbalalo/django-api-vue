import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from news.models import Author, Source, News
import os


class Command(BaseCommand):

    """
    Save the record to DB
    """

    def handle(self, *args, **options):
        try:
            API_KEY = os.environ.get("API_KEY", None)
            f_string = "apple"
            from_date = "2023-03-01"
            url = f"https://newsapi.org/v2/everything?q={f_string}&from={from_date}&sortBy=publishedAt&apiKey={API_KEY}"
            response = requests.get(url=url)
            json_data = response.json()
            articles = json_data.get("articles", [])

            # Bulk save
            with transaction.atomic():
                bulk_list = []
                for a in articles:
                    source = a.get("source", {})
                    author = a.get("author", None)

                    if author:
                        author, _ = Author.objects.get_or_create(name=author)

                    if source:
                        s_name = source.get("name", "")
                        s_id = source.get("id", None)
                        source, _ = Source.objects.get_or_create(
                            source_id=s_id, name=s_name
                        )

                    n = News()
                    n.title = a.get("title", None)
                    n.description = a.get("description", None)
                    n.content = a.get("content", None)
                    n.url = a.get("url", None)
                    n.url_to_image = a.get("urlToImage", None)
                    n.published_at = a.get("publishedAt", None)
                    n._author = author if author else None
                    n._source = source if source else None

                    bulk_list.append(n)
                _ = News.objects.bulk_create(bulk_list)

                print("News data was imporeted to DB")
        except Exception as err:
            print(f"ERROR: {err}")
