from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from autoslug import AutoSlugField
import datetime


class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(default='This is the body of the article')
    date = models.DateField(default=datetime.date.today)
    author = models.CharField(max_length=30, default="author name")
    slug = AutoSlugField(populate_from=['title'], default=title, unique=True)

    def get_absolute_url(self):
        return reverse('blog:article_details', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

