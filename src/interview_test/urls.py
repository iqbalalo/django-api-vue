from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from news.views import NewsViewSet, AuthorViewSet, SourceViewSet, NewsView

router = routers.DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'source', SourceViewSet)


# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    path('html/news', NewsView.as_view()),
]