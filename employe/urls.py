from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from employe import views


urlpatterns = [

    url(r'^employe/(?P<pk>[0-9]+)/$', views.employe_detail),
    url(r'^employe/$', views.employe_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
