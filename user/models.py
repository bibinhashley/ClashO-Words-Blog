from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150)
    image = models.ImageField(default='defualt.png',
                              upload_to='profile_pics', blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):

    title = models.CharField(max_length=150)
    content = models.TextField()
    date_created = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    date_published = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_draft(self):
        self.date_published = None
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
