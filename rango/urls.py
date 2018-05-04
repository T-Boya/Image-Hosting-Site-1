from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^tag/(?P<tag_name_slug>[\w\-]+)/$', views.show_tag, name = 'show_tag')
]