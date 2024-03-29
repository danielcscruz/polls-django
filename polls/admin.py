from django.contrib import admin
from .models import Question, Choice
# Register your models here.



class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra =3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Informaçõesde Data", {"fields":["pub_date"]}),
    ]
    inlines = [ChoiceInLine]



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)