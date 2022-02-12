from django.db import models

class Hof(models.Model):
    name = models.CharField(max_length=254)
    quote = models.CharField(max_length=254)
    quotee = models.CharField(max_length=254)
    description = models.TextField()
    app_head = models.CharField(max_length=254)
    goals_head = models.CharField(max_length=254)
    assists_head = models.CharField(max_length=254)
    titles_head = models.CharField(max_length=254)
    appearances = models.CharField(max_length=254)
    goals = models.CharField(max_length=254)
    assists = models.CharField(max_length=254)
    titles = models.CharField(max_length=254)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name