from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'', include('blog.urls')),
    url(r'^about/$', TemplateView.as_view(template_name="aboutpage2.html"), name='about'),
    url(r'^contactus/$', TemplateView.as_view(template_name="indexcontact.html"), name='contactus'),
    url(r'^submittous/$', TemplateView.as_view(template_name="submitdaft.html"), name='submit'),
    url(r'^news/$', TemplateView.as_view(template_name="news.html"), name='news'),
    url(r'^advice/$', TemplateView.as_view(template_name="advice.html"), name='advice'),
    url(r'^home/$',TemplateView.as_view(template_name="base.html"), name='home'),

]
