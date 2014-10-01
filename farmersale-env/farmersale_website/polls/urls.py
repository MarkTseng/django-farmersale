from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'farmersale_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', 'hello',name='hello'),
    url(r'^time/$', 'current_datetime', name='current_datetime'),
)
