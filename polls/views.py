from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.shortcuts import render, get_object_or_404

class IndexView(generic.ListView):
    # model=Question
    template_name='polls/index.html'
    context_object_name="latest_questions_list"
    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:3]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # error message 만들기
    # 선택된 choice 항목의 votes 값을 1 증가 시키기
    try:
        choice = Choice.objects.get(pk=request.POST['choice'])
        choice.votes+=1
        #choice.votes = F("votes")+1
        choice.save()
    except Choice.DoesNotExist:      
    # except Exception:      
        question = get_object_or_404(Question, pk=question_id)
        # choice_list = question.choice_set.all()
        context = {
        'question':question, 
        'error_message':"뭔가 잘못됐네요!!!"        
        }
        return render(request,'polls/detail.html', context )

    # 다른 페이지 보여주기
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    # return HttpResponseRedirect("https://www.naver.com")