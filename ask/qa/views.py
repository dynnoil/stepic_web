#-*-coding: utf-8-*-

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer

def test(request, *args, **kwargs): 
    # в аргумент *args попадают позиционные параметры роутера
    # в аргумент **kwargs попадают именованные параметры роутера
    return HttpResponse('OK')

def main(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    questions = Question.objects.new()
    limit = 10
    paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/questions.html', {
        'questions': page, 
    })

def popular(request):
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    questions = Question.objects.popular()
    limit = 10
    paginator = Paginator(questions, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'qa/questions.html', {
        'questions': page, 
    })

def question_details(request, id=None):
    try:
        question = Question.objects.get(pk = id)
    except Question.DoesNotExist:
        question = None
    answers = Answer.objects.get_question(question)
    return render(request, 'qa/question_details.html', {
        'question': question,
        'answers': answers,
    })
