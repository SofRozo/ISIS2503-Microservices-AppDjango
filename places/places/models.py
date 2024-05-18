from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
   
    def __str__(self):
        return '%s %s' % (self.value, self.unit)
