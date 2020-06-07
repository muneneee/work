from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User



class Project(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    photo =ImageField(blank=True, manual_crop ="")
    link = models.URLField(max_length = 200, null=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return self.title



class Profile(models.Model):
    photo = ImageField(blank = True, manual_crop="")
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.user.username} Profile'