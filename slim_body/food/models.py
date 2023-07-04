from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/articles/', default='default.jpg')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


