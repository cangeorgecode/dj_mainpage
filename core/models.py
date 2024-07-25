from django.db import models

class Resource(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    cat = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Newsletter(models.Model):
    date_added = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name