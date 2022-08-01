from django.db import models

class News(models.Model):
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title