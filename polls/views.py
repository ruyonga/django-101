from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Daiki, You're at the polls index")


def detail(request, question_id):
    response  = "You're looking at the results of questions %s"
    return HttpResponse(response%question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voiting on question %s." % question_id)