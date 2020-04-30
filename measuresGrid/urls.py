from django.conf.urls import url
from measuresGrid import views

urlpatterns = [

    # URL for API CRUD ( CREATE , READ ALL )    
    url(r'^measuresGrid/$', views.measure_list),
    # URL for API CRUD ( DELETE, UPDATE, READ ONE )    
    url(r'^measuresGrid/(?P<pk>[0-9]+)/$', views.measure_detail),
    # URL for index view with measures grid
    url(r'^measuresGrid/index', views.index, name='index')
]