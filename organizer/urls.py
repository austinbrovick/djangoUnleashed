from django.conf.urls import url

from .views import tag_list, tag_detail, startup_list, startup_detail, TagCreate, StartupCreate, NewsLinkCreate, NewsLinkUpdate, TagUpdate, StartupUpdate, NewsLinkDelete, TagDelete, StartupDelete

urlpatterns = [

  url(r'^startup/$', startup_list, name='organizer_startup_list'),
  url(r'^startup/create/$', StartupCreate.as_view(), name='organizer_startup_create'),
  url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
  url(r'^startup/(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(), name='organizer_startup_update'),
  url(r'^startup/(?P<slug>[\w\-]+)/delete/$', StartupDelete.as_view(), name='organizer_startup_delete'),
]
