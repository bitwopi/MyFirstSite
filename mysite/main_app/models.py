from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    rate = models.FloatField()
    is_out = models.BooleanField(default=False)
    out_date = models.DateField(auto_now_add=True)
    cover = models.ImageField(upload_to="covers/%Y/%m/%d", null=True)
    category = models.ManyToManyField('Category')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name