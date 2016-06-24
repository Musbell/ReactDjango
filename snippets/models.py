from django.db import models


class Snippet(models.Model):
    author = models.ForeignKey('auth.User', related_name='snippets')
    text = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.author

    class Meta:
        ordering = ['author']
