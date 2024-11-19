from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): # request응답을 받는구조
    return HttpResponse("Hello, Lion!!!")


def index1(request): # request응답을 받는구조
    return HttpResponse("장고를 배워볼까요??")

# 함수형 뷰를 하나 추가로 만들어서 응답내용이 웹페이지에 나오는 것 확인하기
# ex) index2 함수(좋은 날이네요 라는 말을 응답) 만들고 127.0.0.1:8000/test 로 접속했을때 "좋은 날이네요" 확인
def index2(request):
    return HttpResponse("좋은 날이네요")