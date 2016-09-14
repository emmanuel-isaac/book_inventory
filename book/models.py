from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.name)


class Book(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    author = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category)

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
