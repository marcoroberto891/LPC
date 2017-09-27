from django.shortcuts import render

from django.http import HttpResponse
def listaTipos(request):
    retorno = "<h1>Eventos</h1>"
    lista = Tipos.objects.all()
    for tipo in lista:
        retorno += '</br>Nome do Evento:{}</br>'.format(lista.nome)
    return HttpResponse(retorno)
