from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class post(models.Model):
    title = models.CharField (max_length=110)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    #I don't get this func, its role?
    #I guess it only return the url named post-create, if no redirect is provided
    
    def get_absolute_url(self):
        return reverse("post-create")
    
    
    