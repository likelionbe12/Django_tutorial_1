from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin
# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=200) # table id serial, name varchar(10)
    pub_date=models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):        
        now = timezone.now()
        if self.pub_date > now:
            is_valid = False  # pub_date가 미래면 False
        else:
            is_valid = self.pub_date >= now - datetime.timedelta(days=1)  # 1일 이내일 경우 True
        return is_valid
    
    def text_length(self):
        return len(self.question_text)

# polls에 model.py에 위 내용 입력
# config에 settings.py에 installed app에 'polls'항목 추가
# 터미널에서 python manage.py makemigrations 실행 -> polls에 migrations 디렉토리 파일이 생기는 것 확인
# python manage.py migrate 를 통해서 polls_questions 테이블 생성 확인

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.choice_text}_투표수:{self.votes}_질문:{self.question.question_text}"
    # 초이스텍스트_투표수:1_질문:가장인상깊은...