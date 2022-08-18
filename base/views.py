from django.shortcuts import render
from django.http import JsonResponse
from .questions import questions

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/questions/',
    ]
    return Response(routes)


@api_view(['GET'])
def getQuestions(request):
    return Response(questions)


@api_view(['GET'])
def getQuestion(request, pk):
    question = None
    for i in questions:
        if i['_id'] == pk:
            question = i
            break
    return Response(question)
