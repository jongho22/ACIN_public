from django.db import models

# Create your models here.
class SEND_DATA(models.Model):
    #title = models.CharField(max_length=50)
    text = models.CharField(max_length=10)
    start_day = models.CharField(max_length=8)
    end_day = models.CharField(max_length=8)
    def __str__(self):
        return self.text
