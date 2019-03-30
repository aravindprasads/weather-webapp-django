from django.conf.urls import url,include                                                            
from . import views

urlpatterns = [                                                                                     
    url('^$', views.index, name='index'),                                                              
    url('add/', views.addCity, name='add'),
    url('del/', views.delCity, name='del'),

]                                                                                                   
