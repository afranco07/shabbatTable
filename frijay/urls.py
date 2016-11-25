'''Url patterns for 'domain.com/frijay/'.'''
from django.conf.urls import url
from frijay import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^login/*', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^profile/', views.profile, name='profile'),
    #reservations page
    #temp\/
    url(r'^reservation/', views.reservation, name='reservation'),
    url(r'^events/', views.events, name='events'),
    #specific reservation view
    url(r'^(?P<event_id>[0-9]+)/$', views.reservationsEvent, name='reservationsEvent'),
]
