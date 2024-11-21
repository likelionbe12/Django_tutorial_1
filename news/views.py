from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, News
# Create your views here.

def index(req):
    companys = Company.objects.all()
    context={'company_list':companys}
    return render(req, 'news/index.html', context)