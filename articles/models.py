from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # TODO:
    # add in thumbnail
    # add in author

    def __str__(self):
        return self.title
    
    def snippet(self):
        if len(self.body) > 0:
            snippet = self.body[:50] + '...'
        else:
            snippet = self.body[:50]
        return snippet