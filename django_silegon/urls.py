from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('articles.urls')),
    url(r'', 'articles.views.blog_index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT, 'show_indexes':True}),
    #url(r'^favicon\.ico$','django.views.generic.simple.redirect_to',{'url':'/static/articles/img/favicon.ico'}),
)
