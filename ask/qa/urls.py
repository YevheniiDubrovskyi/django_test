from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^$', views.new_questions, name='base'),
    url(r'^login/$', views.test, name='login'),
    url(r'^signup/$', views.test, name='signup'),
    url(r'^question/(?P<id>\d+)/$', views.full_question, name='question'),
    url(r'^ask/$', views.test, name='ask'),
    url(r'^popular/$', views.popular_questions, name='popular'),
    url(r'^new/$', views.test, name='new'),
]
