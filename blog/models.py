from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

import readtime
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    # body = models.TextField()
    body = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_post", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_read_time(self):
        result = readtime.of_text(self.body)
        return result.text

    class Meta:
        ordering = ["-date"]
