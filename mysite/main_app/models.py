from django.db import models
from django.urls import reverse


class Anime(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    discription = models.TextField(verbose_name="Discription")
    rate = models.FloatField(verbose_name="Rating")
    is_out = models.BooleanField(default=False, verbose_name="Is out")
    out_date = models.DateField(auto_now_add=True, verbose_name="Release date")
    cover = models.ImageField(upload_to="covers/%Y/%m/%d", null=True, verbose_name="Cover")
    category = models.ManyToManyField('Category', verbose_name="Categories")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
