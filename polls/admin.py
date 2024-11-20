from django.contrib import admin
from .models import Question, Choice
# Register your models here.
admin.site.register([Question, Choice])

# Choice도 넣어보겠습니다!