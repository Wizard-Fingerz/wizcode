from django.db import models
from PIL import Image

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=270)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=270)
    message = models.TextField()
    
    def __str__(self):
        return str(self.full_name)

class Project(models.Model):
    project_name = models.CharField(max_length=270)
    url = models.URLField(max_length=300)
    image = models.ImageField(upload_to ='project_images')
    desc = models.TextField()
    
    def __str__(self):
        return str(self.project_name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

