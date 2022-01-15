from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from wash import views


urlpatterns = [

    url(r'^wash/(?P<pk>[0-9]+)/$', views.wash_detail),
    url(r'^wash/$', views.wash_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
