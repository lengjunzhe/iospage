# coding:utf-8
from django.conf.urls import patterns, include, url
from isopage.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'isopage.views.home', name='home'),
    # url(r'^isopage/', include('isopage.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', simplechinese),
    url(r'^simple/$', simple),
    url(r'^simplechinese/$', simplechinese),
    url(r'^tem/$',tem),
    url(r'^page5302/$', page5302),
    url(r'^page5303/$', page5303),
    url(r'^page5303english/$', page5303english),
    url(r'^page5308/$', page5308),
    url(r'^page5308english/$', page5308english),
)
