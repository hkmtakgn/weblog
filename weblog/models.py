from django.db import models

class Product (models.Model):
    title = models.CharField (max_length=100)
    media = models.FileField (upload_to="pro-media")

    def __str__ (self):
        return self.title
    
