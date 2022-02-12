from django.db import models

class Hof(models.Model):
    name = models.CharField(max_length=254)
    quote = models.CharField(max_length=254)
    quotee = models.CharField(max_length=254)
    description = models.TextField()
    appearances = models.CharField(max_length=254, null=True, blank=True)
    goals = models.CharField(max_length=254, null=True, blank=True)
    assists = models.CharField(max_length=254, null=True, blank=True)
    titles = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name