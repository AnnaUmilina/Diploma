from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=200)
    topics = models.ManyToManyField(Topic, blank=True)
    image = models.ImageField(upload_to='media/articles/', default='default.jpg')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
