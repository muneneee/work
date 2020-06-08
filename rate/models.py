from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User



class Project(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    photo =ImageField(blank=True, manual_crop ="")
    link = models.URLField(max_length = 200, null=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account')
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    votes = models.IntegerField(default=0)



    def __str__(self):
        return self.title


    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()



    @classmethod
    def search_by_title(cls,search_term):
        posts = cls.objects.filter(title__icontains=search_term)
        return posts



class Profile(models.Model):
    photo = ImageField(blank = True, manual_crop="")
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.user.username} Profile'


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


