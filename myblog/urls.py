from django.conf.urls import patterns, include, url

from django.contrib import admin
# import blog.views as bv
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls',namespace='blog')),
)
