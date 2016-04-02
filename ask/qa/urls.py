from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^$', views.new_questions, name='base'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^question/(?P<id>\d+)/$', views.full_question, name='question'),
    url(r'^ask/$', views.add_ask, name='ask'),
    url(r'^answer/$', views.add_answer, name='answer'),
    url(r'^popular/$', views.popular_questions, name='popular'),
    url(r'^new/$', views.new_questions, name='new'),
]
