from django.conf.urls import patterns, include, url
from aspc.senate.views import DocumentList

urlpatterns = patterns('',
    url(r'^documents/$', DocumentList.as_view(), name="document_list"),
    url(r'^documents/(?P<page>[0-9]+)/$', DocumentList.as_view(), name="document_list_page"),
)