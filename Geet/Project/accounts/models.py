from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max

# Create your models here.
class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    song_name=models.CharField(max_length=1000)
    singer_name=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='documents/')
    song_genre = models.CharField(max_length=1000, default="")
    song = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_name


class Listenlater(models.Model):
    listen_id=models. AutoField (primary_key=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    later_id = models. CharField(max_length=10000000, default="")
    added_at = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    history_id =models. AutoField (primary_key=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    music_id = models. CharField(max_length=10000000, default="")
    done_at = models.DateTimeField(auto_now_add=True)