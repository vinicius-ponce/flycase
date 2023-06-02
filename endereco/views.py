from django.shortcuts import render, redirect
from .models import lugar
import requests

def home(request):
    lugares = lugar.objects.all()
    return render(request, "index.html", {"lugares": lugares})

def salvar(request):
    cep = request.POST.get("cep")

    def pega_cep():
        busca = cep.replace(".","").replace("-","").replace(" ","")
        link = f'https://viacep.com.br/ws/{busca}/json/'

        erro = requests.get(link)
        dic_erro = erro.json()

        if dic_erro['erro'] == True:
            busca = "9999"

        if len(busca) == 8:
            resultado = requests.get(link)
            dic_resultado = resultado.json()

            lugar.objects.create(cep_lugar=busca, uf_lugar=dic_resultado['uf'],
                                 distrito_lugar=dic_resultado['bairro'],logradouro_lugar=dic_resultado['logradouro'])
            lugares = lugar.objects.all()
            retorno = render(request, "index.html", {"lugares": lugares})

        else:
            lugar.objects.create(cep_lugar= busca, uf_lugar="", distrito_lugar="",logradouro_lugar="")
            lugares = lugar.objects.all()
            retorno = render(request, "index.html", {"lugares": lugares})
        return retorno
    return pega_cep()

def editar(request, id):
    lugares = lugar.objects.get(id=id)
    return render(request, "update.html", {"lugar":lugares})

def update(request, id):
    cep = request.POST.get("cep")
    lugares = lugar.objects.get(id=id)
    lugares.cep_lugar = cep
    lugares.save()
    return redirect(home)

def deletar(request, id):
    lugares = lugar.objects.get(id=id)
    lugares.delete()
    return redirect(home)


