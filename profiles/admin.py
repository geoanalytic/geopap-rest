from django.contrib import admin

# Register your models here.
from profiles.models import Project, Tag, Basemap, Spatialdbs, Otherfiles, Profile, ProfileSet
admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Basemap)
admin.site.register(Spatialdbs)
admin.site.register(Otherfiles)
admin.site.register(Profile)
admin.site.register(ProfileSet)