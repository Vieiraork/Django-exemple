from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def helloWordl(request):
    return HttpResponse('Hello Wolrd!')

@csrf_exempt
def contas(request):
    num1 = request.POST['numero1']
    num2 = request.POST['numero2']
        
    soma = int(num1) + int(num2)
        
    return render(request, 'tarefas/contas.html', {'soma': soma, 'n1': num1, 'n2': num2})
