from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from food import views


urlpatterns = [

    url(r'^meal/(?P<pk>[0-9]+)/$', views.meal_detail),
    url(r'^meal/$', views.meal_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
