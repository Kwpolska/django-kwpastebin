from django.urls import re_path
from kwpastebin import views

app_name = "kwpastebin"

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^mine/$', views.my_pastes, name='my_pastes'),
    re_path(r'^all/$', views.all_pastes, name='all_pastes'),
    re_path(r'^invalidate_cache/$', views.invalidate_cache, name='invalidate_cache'),
    re_path(r'^(?P<id>.*?)/edit/$', views.edit_paste, name='edit_paste'),
    re_path(r'^(?P<id>.*?)/delete/$', views.delete_paste, name='delete_paste'),
    re_path(r'^(?P<id>.*?)/invalidate_cache/$', views.invalidate_cache_for_paste, name='invalidate_cache_for_paste'),
    re_path(r'^(?P<id>.*?)/raw/$', views.show_paste_raw, name='show_paste_raw'),
    re_path(r'^(?P<id>.*?)/$', views.show_paste, name='show_paste'),
]
