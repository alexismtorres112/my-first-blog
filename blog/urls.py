from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

    url(r'^category$', views.category_list, name='category_list'),
    url(r'^category/(?P<pk>\d+)/$', views.category_detail, name='category_detail'),
    
    url(r'^news-page/$', views.post_list_news, name='post_list_news'),
    url(r'^advice-page/$', views.post_list_advice, name='post_list_advice'),
    url(r'^writing-page/$', views.post_list_writing, name='post_list_writing'),
    url(r'^art-page/$', views.post_list_art, name='post_list_art'),


]
