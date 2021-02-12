from django.db import models


class Meme(models.Model):
    """
    The Meme Model to hold all the data about the memes
    """
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
