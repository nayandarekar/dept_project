from django.db import models

# Create your models here.
class Book(models.Model):
    """A Book Model"""

    name = models.CharField(max_length=255, blank=False, null=False, help_text="Enter Book Name")
    description = models.CharField(max_length=255, blank=False, null=False, help_text="Enter Book Description")

    def __str__(self):
        """SELF"""
        return self.name

# Create your models here.
class Author(models.Model):
    """A Author Model"""

    name = models.CharField(max_length=255, blank=False, null=False, help_text="Enter Author Name")
    description = models.CharField(max_length=255, blank=False, null=False, help_text="Enter Author Description")
    book = models.ManyToManyField(Book, through='BookAuthor')

    def __str__(self):
        """SELF"""
        return self.name

#
class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    extra_live = models.BooleanField(default=False)

    def __str__(self):
        return "{}_{}".format(self.author.__str__(), self.book.__str__())