from django.contrib import admin
from django.urls import path
#from polls import views
#from . import views
# from .views import index, detail
from . import views
app_name = "polls"
urlpatterns = [   
        # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),

    # path('', index),
    # path('<int:question_id>/', detail), # < 이 자료형이 들어오면 : 이 변수로 다음단계로 전달할게>
    # path('django/', index1),
    # path('new/', index2),
    
]

