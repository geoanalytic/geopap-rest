from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from profiles import views

urlpatterns = [
    url(r'^myprofiles/$', views.MyProfiles.as_view()),
    url(r'^profiles/$', views.ProfileList.as_view()),
    url(r'^profiles/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()),
    url(r'^basemaps/$', views.BasemapList.as_view()),
    url(r'^basemaps/(?P<pk>[0-9]+)/$', views.BasemapDetail.as_view()),
    url(r'^tags/$', views.TagList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),
    url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
    url(r'^spatialitedbs/$', views.SpatialitedbsList.as_view()),
    url(r'^spatialitedbs/(?P<pk>[0-9]+)/$', views.SpatialitedbsDetail.as_view()),
    url(r'^otherfiles/$', views.OtherfilesList.as_view()),
    url(r'^otherfiles/(?P<pk>[0-9]+)/$', views.OtherfilesDetail.as_view()),  
#    url(r'^users/$', views.UserList.as_view()),
#    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),    
]

urlpatterns = format_suffix_patterns(urlpatterns)