from django.conf.urls import url
from kwpastebin import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mine/$', views.my_pastes, name='my_pastes'),
    url(r'^all/$', views.all_pastes, name='all_pastes'),
    url(r'^invalidate_cache/$', views.invalidate_cache, name='invalidate_cache'),
    url(r'^(?P<id>.*?)/edit/$', views.edit_paste, name='edit_paste'),
    url(r'^(?P<id>.*?)/delete/$', views.delete_paste, name='delete_paste'),
    url(r'^(?P<id>.*?)/invalidate_cache/$', views.invalidate_cache_for_paste, name='invalidate_cache_for_paste'),
    url(r'^(?P<id>.*?)/$', views.show_paste, name='show_paste'),
]
