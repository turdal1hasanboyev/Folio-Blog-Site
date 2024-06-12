from django.db import models
from apps.user.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, max_length=225, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="BlogPhotos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
            
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Comment(models.Model):    
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=225, null=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name
    

class Portfolio(models.Model):
    image = models.ImageField(upload_to="PortfolioPhotos/")

    def __str__(self):
        return ""
    