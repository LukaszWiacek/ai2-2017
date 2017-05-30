from django.db import models
from django.utils import timezone

class Post(models.Model):
    name_hotel = models.CharField(max_length=30)
    release_date = models.DateField()
    how_much = models.IntegerField()

    def publish(self):
        self.release_date = timezone.now()
        self.save()

    def __str__(self):    
        return self.how_much
