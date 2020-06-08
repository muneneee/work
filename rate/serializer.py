from rest_framework import serializers
from .models import Project,Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','description','link','votes')



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('photo','bio')