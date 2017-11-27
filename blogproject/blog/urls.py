from django.conf.urls import url
from . import views

app_name = 'blog' # 通过这行告诉django这个urls.py模块是属于blog应用的
urlpatterns = [
    # url(r'^$', views.index, name='index'),# name给这些视图函数取个别名
    url(r'^$', views.IndexView.as_view(), name='index'),# name给这些视图函数取个别名
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^search/$', views.search, name='search'),
]