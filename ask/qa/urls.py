from django.conf.urls import url
from qa import views

urlpatterns = [
	url(r'^', views.test, name='root'),
	url(r'^signup/$', views.test, name='signup'),
	url(r'^question/([0-9]+)/$', views.test, name='question'),
	url(r'^ask/$', views.test, name='ask'),
	url(r'^popular/$', views.test, name='popular'),
	url(r'^new/$', views.test, name='new'),
]
