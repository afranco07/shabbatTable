from django.conf.urls import url
from frijay import views

#These url patterns are for 'domain.com/frijay/'.
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
    url(r'^signup/',views.signup, name='signup'),
    url(r'^login/',views.login, name="login"),
    url(r'^profile/', views.profile, name="profile"),
]
