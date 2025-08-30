from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage, RawMediaCloudinaryStorage

# Create your models here.
class Info(models.Model):
    title = models.CharField(max_length=255)
    short_intro = models.TextField()
    long_intro = models.TextField()
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', null=True, blank=True, storage=MediaCloudinaryStorage)
    about_image = models.ImageField(upload_to='images', null=True, blank=True, storage=MediaCloudinaryStorage)
    resume = models.FileField(upload_to='resumes', null=True, blank=True, storage=RawMediaCloudinaryStorage)
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Info"
    
class Experience(models.Model):
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company
    

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images', storage=MediaCloudinaryStorage)
    url = models.URLField(null=True, blank=True)
    role = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):        
        return self.name
    
