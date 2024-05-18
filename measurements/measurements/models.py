from django.db import models

class Measurement(models.Model):
    variable = models.IntegerField(null=False, default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=50)
    place = models.IntegerField(null=False, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)