from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=500)
    image = models.ImageField(upload_to="authors-images/")

    def __str__(self):
        return self.name