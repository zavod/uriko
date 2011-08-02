# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    #url(r'^$', 'cms.views.page_by_id', {'id': 1}, name='index'),
    (r'^', include('cms.urls')),
)
