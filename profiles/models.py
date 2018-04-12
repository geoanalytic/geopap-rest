from django.db import models
from django.contrib.postgres.fields import ArrayField
# Geopaparrazi profiles model

class Project(models.Model):
    path = models.CharField(max_length=100, blank=True, default='')
    modifieddate = models.DateTimeField(auto_now_add=True)    
    url = models.URLField(blank=True)
    uploadurl = models.URLField(blank=True)
    profile = models.ForeignKey("Profile", on_delete = models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.path    

class Tag(models.Model):
    path = models.CharField(max_length=100, blank=True, default='')    
    modifieddate = models.DateTimeField(auto_now_add=True) 
    url = models.URLField(blank=True)

    def __str__(self):
        return self.path

class Basemap(models.Model):
    path = models.CharField(max_length=100, blank=True, default='')    
    modifieddate = models.DateTimeField(auto_now_add=True) 
    url = models.URLField(blank=True)
    size = models.CharField(max_length=30)
    
    def __str__(self):
        return self.path

class Spatialdbs(models.Model):
    path = models.CharField(max_length=100, blank=True, default='')    
    modifieddate = models.DateTimeField(auto_now_add=True) 
    url = models.URLField(blank=True)
    size = models.CharField(max_length=30)
    uploadurl = models.URLField(blank=True)
    visible = ArrayField(models.CharField(max_length=30))

    def __str__(self):
        return self.path
    
class Otherfiles(models.Model):
    path = models.CharField(max_length=100, blank=True, default='')    
    modifieddate = models.DateTimeField(auto_now_add=True) 
    url = models.URLField(blank=True)

    def __str__(self):
        return self.path
        
class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    creationdate = models.DateTimeField(auto_now_add=True)    
    modifieddate = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=30, default="#FBC02D")
    active = models.BooleanField(default=False)
    sdcardPath = models.CharField(max_length=100, default="MAINSTORAGE")
    mapView = models.CharField(max_length=100, default="52.02025604248047,-115.70208740234375,10.0")
    tags = models.ForeignKey(Tag, on_delete = models.SET_NULL, blank=True, null=True)
    basemaps = models.ManyToManyField(Basemap, blank=True)
    spatialdbs = models.ManyToManyField(Spatialdbs, blank=True)
    otherfiles = models.ManyToManyField(Otherfiles, blank=True)

    def __str__(self):
        return self.name
            
    class Meta:
        ordering = ('modifieddate', 'name', )

class ProfileSet(models.Model):
    owner = models.ForeignKey('users.user', related_name='profilesets', on_delete=models.CASCADE)
    profiles = models.ManyToManyField(Profile, blank=True)
    formatVersion = models.FloatField(default=1.1)

    def __str__(self):
        return self.owner.username
