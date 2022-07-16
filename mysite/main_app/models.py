from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField()
    is_out = models.BooleanField(default=False)
    out_date = models.DateField(auto_now_add=True)
    cover = models.ImageField(upload_to="covers/%Y/%m/%d", null=True)
    genres = models.IntegerField(null=True)