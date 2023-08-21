from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    options = (("draft", "Draft"), ("published", "Published"))
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True, editable=False)
    date_updated = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=options, default="draft")

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title
