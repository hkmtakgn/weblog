from django.db import models

class Product (models.Model):
    title = models.CharField (max_length=100)
    media = models.FileField (upload_to="pro-media")
    picture = models.ImageField (upload_to='pic_file')

    def __str__ (self):
        return self.title
    
