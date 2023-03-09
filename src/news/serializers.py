from rest_framework import serializers

from .models import News, Author, Source


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ["source_id", "name"]


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField()
    source = serializers.ReadOnlyField()

    class Meta:
        model = News
        fields = [
            "id",
            "published_at",
            "title",
            "description",
            "url",
            "url_to_image",
            "content",
            "author",
            "source",
        ]
