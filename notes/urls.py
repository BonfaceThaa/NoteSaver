from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^notes$', views.note_list, name='note_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<note>[-\w]+)/$',
        views.note_detail,
        name='note_detail'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.note_list, name='note_list_by_tag'),
    url(r'^goals$', views.goal_list, name='goal_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.goal_list, name='goal_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.goal_detail, name='goal_detail'),
    url(r'^goal_tag/(?P<tag_slug>[-\w]+)/$', views.goal_list, name='goal_list_by_tag'),
]
