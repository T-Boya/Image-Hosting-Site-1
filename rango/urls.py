from django.conf.urls import url
from rango import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^add_tag/$', views.add_tag, name='add_tag'),
    # url(r'^tag/(?P<tag_name_slug>[\w\-]+)/add_photo/', views.add_photo, name='add_photo'),
    url(r'^tag/(?P<tag_name_slug>[\w\-]+)/$', views.show_tag, name = 'show_tag'),
    url(r'^$', views.index, name="index"),
    url(r'^search/', views.search, name="search"),
]