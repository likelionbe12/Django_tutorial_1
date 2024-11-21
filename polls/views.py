from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question, Choice
from django.template import loader
# Create your views here.

def index(request): # request응답을 받는구조
    questions_list = Question.objects.order_by("-pub_date")[:3]
    # questions = Question.objects.order_by("-question_text")[:3]
    # q_text = Question.objects.all()[0].question_text
    # template = loader.get_template('polls/index.html') # polls/templates/polls/index.html
    # return HttpResponse(template.render({}, request))
    context = {"latest_questions_list":questions_list}
    return render(request, 'polls/index.html', context=context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("이거 뭔가 잘못됐는데요???")
    question = get_object_or_404(Question, pk=question_id)
    # choice_list = question.choice_set.all()
    context = {
        'question':question, 
        # 'choice_list':choice_list
    }
    return render(request,'polls/detail.html', context )


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    lion = request.POST['lion']
    tiger = request.POST['tiger']
    return HttpResponse("You're voting on question %s %s." % (lion, tiger))



# def detail(request, question_id):
#     q = Question.objects.get(pk=question_id)
#     return HttpResponse(f"{question_id}번 Question : {q.question_text}")


# def index1(request): # request응답을 받는구조
#     return HttpResponse("장고를 배워볼까요??")

# 함수형 뷰를 하나 추가로 만들어서 응답내용이 웹페이지에 나오는 것 확인하기
# ex) index2 함수(좋은 날이네요 라는 말을 응답) 만들고 127.0.0.1:8000/test 로 접속했을때 "좋은 날이네요" 확인
# def index2(request):
#     return HttpResponse("좋은 날이네요")