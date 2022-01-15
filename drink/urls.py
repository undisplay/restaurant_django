from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from drink import views


urlpatterns = [

    url(r'^drink/(?P<pk>[0-9]+)/$', views.drink_detail),
    url(r'^drink/$', views.drink_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
