from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.

def index(request):
    #Latest 5 questions
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'Polls/index.html', context)
    # template = loader.get_template('Polls/index.html')
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # return HttpResponse(template.render(context,request))

    # questionslist = ""
    # #u=0

    # #Loop to refer each question
    # for q in latest_question_list:
    #     questionslist += "\n" +  q.question_text 
    #    # u += 1

    # output =  questionslist
    # return HttpResponse(output)

# def index(request):
#     return HttpResponse("Hello! This is the index page.")

# def aboutus(request):
#     return HttpResponse("This about us page.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'Polls/detail.html', {'question' : question})
    # return HttpResponse("You are looking at question number %s. " %question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'Polls/results.html', {'question' : question})
    #  return HttpResponse("You are looking at the results of question number %s. " %question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'Polls/details.html', {'question' : question, 'error_message' : "You didnt select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))