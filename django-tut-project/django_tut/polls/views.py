from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render(request, 'index.htm', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'detail.htm', {'question':question})

def result(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'result.htm', {'question':question})


class IndexView(generic.ListView):
	template_name = 'index.htm'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'detail.htm'

class ResultView(generic.DetailView):
	model = Question
	template_name = 'result.htm'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'detail.htm', {'question':question, 'error_message':"You didn't select a choice."})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
