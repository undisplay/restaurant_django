from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ordered import views


urlpatterns = [

    url(r'^ordered/(?P<pk>[0-9]+)/$', views.ordered_detail),
    url(r'^ordered/$', views.ordered_list),

    url(r'^drinkorderedline/(?P<pk>[0-9]+)/$', views.drinkorderedline_detail),
    url(r'^drinkorderedline/$', views.drinkorderedline_list),

    url(r'^mealorderedline/(?P<pk>[0-9]+)/$', views.mealorderedline_detail),
    url(r'^mealorderedline/$', views.mealorderedline_list),

    url(r'^menuorderedline/(?P<pk>[0-9]+)/$', views.menuorderedline_detail),
    url(r'^menuorderedline/$', views.menuorderedline_list),

    url(r'^washorderedline/(?P<pk>[0-9]+)/$', views.washorderedline_detail),
    url(r'^washorderedline/$', views.washorderedline_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
