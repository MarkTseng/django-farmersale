import datetime
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext, loader
from polls.models import Question, Choice
from django.core.urlresolvers import reverse

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template = loader.get_template('polls/index.html')
	#context = RequestContext(request, {
	#	'latest_question_list': latest_question_list,
	#	})
	#return HttpResponse(template.render(context))
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

# Create your views here.
#def index(request):
#   return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

#def detail(request, question_id):
#	try:
#		question = Question.objects.get(pk=question_id)
#	except Question.DoesNotExist:
#		raise Http404
#	return render(request,'polls/detail.html',{'question':question})
	#return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})
	#return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	return render(request, "polls/result.html", {'question':question})

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
				'question':p,
				'error_message':"you didn't select a choice.",
			})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

