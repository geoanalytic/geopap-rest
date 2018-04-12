from rest_framework import serializers
from profiles.models import Project, Tag, Basemap, Spatialdbs, Otherfiles, Profile, ProfileSet
from django.contrib.auth import get_user_model

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('path', 'modifieddate', 'url', 'uploadurl' )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('path', 'modifieddate', 'url' )

class BasemapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basemap
        fields = ('path', 'modifieddate', 'url', 'size' )

class SpatialdbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spatialdbs
        fields = ('path', 'modifieddate', 'url', 'size', 'uploadurl', 'visible' )

class OtherfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otherfiles
        fields = ('path', 'modifieddate', 'url' )

class ProfileSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(read_only=True)
    tags = TagSerializer(read_only=True)
    basemaps = BasemapSerializer(many=True, read_only=True)
    spatialdbs = SpatialdbsSerializer(many=True, read_only=True)
    otherfiles = OtherfilesSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('name', 'description', 'creationdate', 'modifieddate', 'color', 'active',
                  'sdcardPath', 'mapView', 'projects', 'tags', 'basemaps', 'spatialdbs', 'otherfiles' )

class ProfileSetSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(read_only=True, many=True)
    class Meta:
        model = ProfileSet
        fields = ('formatVersion', 'profiles')
