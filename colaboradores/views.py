from django.shortcuts import render,redirect
from .models import Colaborador

def novo_colaborador(request):
    if request.method == 'GET':
        todos_colaboradores = Colaborador.objects.all()
        return render(request, 'novo_colaborador.html', {'colaboradores':todos_colaboradores})
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome =  request.POST.get('sobrenome')
        email = request.POST.get('email')

        colaborador = Colaborador(
            nome=nome,
            sobrenome=sobrenome,
            email=email
        )

        colaborador.save()

        return redirect('novo_colaborador')


def deletar_colaborador(request, id):
    colaborador_a_ser_deletado = Colaborador.objects.get(id=id)
    colaborador_a_ser_deletado.delete()
    return redirect('novo_colaborador')

def editar_colaborador(request, id):
    colaborador_selecionado = Colaborador.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'editar_colaborador.html', {'colaborador':colaborador_selecionado})
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')

        colaborador_selecionado.nome = nome
        colaborador_selecionado.sobrenome = sobrenome
        colaborador_selecionado.email = email

        colaborador_selecionado.save()

        return redirect('novo_colaborador')