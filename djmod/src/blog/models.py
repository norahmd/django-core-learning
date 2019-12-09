from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from .validators import  validate_norah
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.utils.timesince import timesince
from datetime import date, datetime, timedelta


PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)
class PostModelQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def post_title_items(self, value):
        return self.filter(title__icontains=value)


class PostModelManager(models.Manager):
    def get_queryset(self):
        return PostModelQuerySet(self.model, using=self._db)
    
    # def active(self):
    #     return self.get_queryset().active()

    def all(self, *args, **kwargs):
        qs = super(PostModelManager, self).all(*args, **kwargs).active()
        return qs

    def get_timeframe(self, date1, date2):
        qs = self.get_queryset()
        qs_time_1 = qs.filter(publish_date__gte=date1)
        qs_time_2 = qs.filter(publish_date__lt=date2)
        final_qs = (qs_time_1 | qs_time_2).distinct()
        return final_qs

# Create your models here.
class PostModel(models.Model):
    id              = models.BigAutoField(primary_key=True)
    active          = models.BooleanField(default=True)
    title           = models.CharField(
                            max_length=240, 
                            verbose_name='Post title',
                            unique=True,
                            error_messages={
                            "unique": "This title is not unique"
                            },
                            help_text='Must be a unique title.')
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.EmailField(max_length=240, validators=[validate_norah], null=True, blank=True)
    updated         = models.DateField(auto_now=True)
    timestamp       = models.DateField(auto_now_add=True)


    objects = PostModelManager()
    def save(self, *args, **kwargs):
        # print("hello there")
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return smart_text(self.title)
    @property
    def age(self):
        return timesince(self.publish_date)


def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("before save")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)

pre_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)


def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("after save")
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(blog_post_model_post_save_receiver, sender=PostModel)
    