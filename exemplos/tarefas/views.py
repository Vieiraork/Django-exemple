from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def helloWordl(request):
    return HttpResponse('Hello Wolrd!')

@csrf_exempt
def contas(request):
    num1 = request.POST.get('numero1')
    num2 = request.POST.get('numero2')
        
    if num1 != None and num2 != None:
        soma = int(num1) + int(num2)
    else:
        soma = 0
    return render(request, 'tarefas/contas.html', {'soma': soma})
