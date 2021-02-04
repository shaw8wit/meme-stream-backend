from django.db import models


class Meme(models.Model):
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    url = models.CharField(max_length=300)

    def serialize(self):
        return {
            'name': self.name,
            'caption': self.caption,
            'url': self.url,
        }