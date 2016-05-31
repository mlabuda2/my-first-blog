from django.db import models
from django.utils import timezone

# tagging
from taggit.managers import TaggableManager


class Post(models.Model):

    CATEGORY_CHOICES = (
        ('samo', 'Samochody'),
        ('moto', 'Motocykle'),
        ('nc', 'No Category'),
    )

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    tags = TaggableManager()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
