
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^tags/$', views.tags, name='tags'),
    re_path(r'^tags/(?P<tag_id>\d+)/$', views.tag, name='tag'),
    re_path(r'^posts/(?P<post_id>\d+)/$', views.post, name='post'),
    re_path(r'^themes/$', views.themes, name='themes'),
    re_path(r'^tags/new$', views.new_tag, name='new_tag'),
    re_path(r'^themes/new_theme$', views.new_theme, name='new_theme'),
    re_path(r'^edit_tag/(?P<tag_id>\d+)/$', views.edit_tag, name='edit_tag'),
    re_path(r'^edit_post/(?P<post_id>\d+)/$',
            views.edit_post, name='edit_post'),
]



