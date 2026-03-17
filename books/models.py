from django.db import models
from authors.models import Author
from categories.models import Category 

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="books")
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    book_pages = models.PositiveIntegerField()
    publish_year = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to="books-images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title