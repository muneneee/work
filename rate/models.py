from django.db import models
from pyuploadcare.dj.models import ImageField



class Project(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    photo =ImageField(blank=True, manual_crop ="")
    link = models.URLField(max_length = 200, null=True)


    def __str__(self):
        return self.title