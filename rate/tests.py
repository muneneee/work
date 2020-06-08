from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile,Project

class ProfileTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_profile = Profile(id=1,user=self.new_user,bio='Test Bio')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_user = User.objects.create_user(username='user',password='password')
        self.new_project = Project(id=1,title='title',description='description',link='www.link.com',account=self.new_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_instance(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_profile(self):
        self.new_project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)