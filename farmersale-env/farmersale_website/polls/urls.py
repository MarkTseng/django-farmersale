from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'farmersale_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'index',name='index'),
    url(r'^hello/$', 'hello',name='hello'),
    url(r'^time/$', 'current_datetime', name='current_datetime'),
	# ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', 'detail', name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', 'results', name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', 'vote', name='vote'),

)
