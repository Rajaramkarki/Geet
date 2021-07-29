from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Manager
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager


# Create your models here.

class Querymanager(models.Manager):
    def get_queryset(self):
        return super(Querymanager, self).get_queryset().filter(status='published')


class Postmodel(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),
                      )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='publish', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='author_posts')
    body = models.TextField()
    image = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    object = models.Manager()
    published = Querymanager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('community:post_detail',
                            kwargs={'pk': self.pk})

         #class meta:

    #    ordering = ('-publish',)  # sort post according to the publish date

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Postmodel, self).save(*args, **kwargs)


class comment(models.Model):
    post=models.ForeignKey(Postmodel,on_delete=models.CASCADE,related_name='comments')
    user= models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    email=models.EmailField()
    body=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class meta:
        ordering = 'created'

    def __str__(self):
        return f'comment by {self.user} on {self.post}'