from __future__ import unicode_literals

import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.ImageField()

    def get_absolute_url(self):
        return reverse("music:detail",kwargs={"pk": self.pk})

    def __unicode__(self):
        return self.album_title+"-"+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favorite=models.BooleanField(default=False)

    def __unicode__(self):
        return self.song_title

class Comment(models.Model):
    song=models.ForeignKey(Song,on_delete=models.CASCADE)
    comment=models.CharField(max_length=250)

    user=models.SET(User.username)
    date = models.DateTimeField

    def __str__(self):
        return  self.comment

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    favorite = models.BooleanField(default=False)
