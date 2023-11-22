from django.contrib import admin
from .models import Question, Choice

# Register your models here.

#admin.site.register(Question)

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldset = [(
        None, {"fields": [ "question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]} ),
        ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

#adding a model to admin
#admin.site.register(Choice)
