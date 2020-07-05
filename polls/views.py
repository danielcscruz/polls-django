from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Choice, Question


titulo = "Enquetes"
subtitulo = "Django Project"
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, 'titulo': titulo, 'subtitulo': subtitulo}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):

    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/polls_detail.html', {'question': question, 'titulo': titulo, 'subtitulo': subtitulo})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/polls_results.html', {'question': question, 'titulo': titulo, 'subtitulo': subtitulo})


def vote(request, question_id):
    return render(request, "polls/polls_vote.html", {"question_id":question_id, 'titulo': titulo, 'subtitulo': subtitulo})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/polls_detail.html', {
            'question': question,
            'error_message': "Você não escolheu uma opção",
             'titulo': titulo, 'subtitulo': subtitulo
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))