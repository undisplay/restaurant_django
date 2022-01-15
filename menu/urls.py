from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from menu import views


urlpatterns = [

    url(r'^menu/(?P<pk>[0-9]+)/$', views.menu_detail),
    url(r'^menu/$', views.menu_list),

    url(r'^menumeal/(?P<pk>[0-9]+)/$', views.menumeal_detail),
    url(r'^menumeal/$', views.menumeal_list),

    url(r'^menudrink/(?P<pk>[0-9]+)/$', views.menudrink_detail),
    url(r'^menudrink/$', views.menudrink_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
