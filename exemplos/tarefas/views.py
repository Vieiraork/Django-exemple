from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def helloWordl(request):
    return HttpResponse('Hello Wolrd!')

def contas(request):
    return render(request, 'tarefas/contas.html')
