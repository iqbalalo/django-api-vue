from django.db import models


class Source(models.Model):
    source_id = models.CharField(null=True, blank=True, max_length=100)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class News(models.Model):
    published_at = models.DateTimeField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    url_to_image = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    _author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, blank=True
    )
    _source = models.ForeignKey(
        Source, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.title} published on {self.published_at}"

    @property
    def author(self):
        return self._author.name

    @property
    def source(self):
        return {"id": self._source.source_id, "name": self._source.name}
