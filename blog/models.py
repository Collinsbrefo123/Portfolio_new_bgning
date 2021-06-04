from django.db import models


class Blogs(models.Model):
    title: str = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title
