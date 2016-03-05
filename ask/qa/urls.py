from django.conf.urls import url

from qa.views import test

urlpatterns = [
	url(r'^', qa.views.test, name='root'),
	url(r'^signup/$', qa.views.test, name='signup'),
	url(r'^question/([0-9]+)/$', qa.views.test, name='question'),
	url(r'^ask/$', qa.views.test, name='ask'),
	url(r'^popular/$', qa.views.test, name='popular'),
	url(r'^new/$', qa.views.test, name='new'),
]
