from django.contrib import admin
from .models import Question, Answer

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['answer_text']


class AnswerInline(admin.StackedInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
   search_fields = ['question_name']
   fields = ["question_name", "question_text"]
   inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
