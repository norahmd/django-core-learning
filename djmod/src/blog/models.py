from django.db import models


PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


# Create your models here.
class PostModel(models.Model):
    id          = models.BigAutoField(primary_key=True)
    active      = models.BooleanField(default=True)
    title       = models.CharField(max_length=240, verbose_name='Post title')
    content     = models.TextField(null=True, blank=True)
    publish     = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'