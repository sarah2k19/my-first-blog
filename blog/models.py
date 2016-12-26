from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name='snippets')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #added after REST API implementation
    #created = models.DateTimeField(auto_now_add=True)
    #title = models.CharField(max_length=100, blank=True, default='')
    #code = models.TextField()
    #linenos = models.BooleanField(default=False)
    #language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    #style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
