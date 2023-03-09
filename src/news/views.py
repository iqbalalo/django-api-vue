from django.views.generic import TemplateView
from .models import News, Author, Source
from .serializers import NewsSerializer, AuthorSerializer, SourceSerializer
from rest_framework import viewsets
from rest_framework import pagination


class NewsView(TemplateView):
    template_name = "news/list.html"


class NewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows news to be viewed.
    """

    queryset = News.objects.all().order_by("-published_at")
    serializer_class = NewsSerializer
    pagination.PageNumberPagination.page_size = 100

    def list(self, request, *args, **kwargs):
        page_size = request.GET.get("page_size")
        if page_size:
            pagination.PageNumberPagination.page_size = page_size

        return super().list(request, *args, **kwargs)


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows author to be viewed.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows source to be viewed.
    """

    queryset = Source.objects.all()
    serializer_class = SourceSerializer
