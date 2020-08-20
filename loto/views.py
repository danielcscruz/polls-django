from django.shortcuts import render
from loto.gen import lotofacil

# Create your views here.

titulo = "Loto - gerador"
subtitulo = "Gerador de números aleatórios"


def loto_generator(request):
    return render(request, 'loto/gerador.html', {'titulo': titulo, 'subtitulo': subtitulo})


def output(request):
    if request.is_ajax():
        py_obj = lotofacil()
        return render(request, 'loto/output.html', {'output': py_obj})