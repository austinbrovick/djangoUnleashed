from django.conf.urls import url

from ..views import tag_list, tag_detail, TagCreate, TagDelete, TagUpdate

urlpatterns = [
    url(r'^create/$', TagCreate.as_view(), name='organizer_tag_create'),
    url(r'^$', tag_list, name='organizer_tag_list'),
    url(r'^(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$', TagUpdate.as_view(), name='organizer_tag_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', TagDelete.as_view(), name='organizer_tag_delete'),
]
