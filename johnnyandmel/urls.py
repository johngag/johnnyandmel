from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'johnnyandmel.views.home', name='home'),
    url(r'^wedding/', 'johnnyandmel.views.wedding', name='wedding'),
    url(r'^gallery/', 'johnnyandmel.views.gallery', name='gallery'),
    url(r'^contact/', 'johnnyandmel.views.contact', name='contact'),
    # url(r'^johnnyandmel/', include('johnnyandmel.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
