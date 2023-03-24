from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import Survivor

from django.contrib import messages

# Create your views here.


def createSurvivor(request):
    if request.method == 'GET':
        survivor = Survivor.objects.raw('SELECT * FROM core_survivor')

        content = {
            'conteudo': survivor
        }

        return render(request, 'tela.html', content)
    else:
        user_name = request.POST['user_name']
        user_age = request.POST['user_age']
        user_sex = request.POST['user_sex']

        if user_sex == 'Masculino':
            user_sex = 'M'
        elif user_sex == 'Feminino':
            user_sex = 'F'
        else:
            user_sex = ''

        exist = Survivor.objects.filter(user_name=user_name)
        if exist:
            messages.error(request, 'Usuário com esse nome já foi resgistrado')
            return redirect('/api/v1/survivor/create/')
        else:
            create = Survivor.objects.create(user_name=user_name, user_age=user_age, user_sex=user_sex)
            create.save()

            messages.success(request, 'Registrado com sucesso')

            return redirect('/api/v1/survivor/create/')

def contaInterna(request):
    if request.method == 'GET':
        return render(request, 'contaInterna.html')
    else:
        user_name = request.POST['user_name']
        user_last_location = request.POST['user_last_location']

        exist = Survivor.objects.filter(user_name=user_name)

        if exist:
            exist.update(user_last_location=user_last_location)
            messages.success(request, 'Usuário atualizado com sucesso.')
            return redirect('/api/v1/survivor/create/')
        else:
            messages.error(request, 'O usuário informado não existe.')
            return redirect('/api/v1/survivor/updateUser/')

def deleteSurvivor(request):
    if request.method == 'GET':
        user_name = request.GET['user']
        print(user_name)
        if user_name == '':
            messages.error(request, 'Sem usuário definido')
            return render(request, 'tela.html')
        else:
            exist = Survivor.objects.filter(user_name=user_name)
            if exist:
                exist.delete()
                messages.success(request, 'Usuário deletado!')
                return redirect('/api/v1/survivor/create/')
            else:
                messages.error(request, 'Usuário não encontrado!')
                return redirect('/api/v1/survivor/create/')
    else:
        message.error('Metodo não encontrado')
        return redirect('/api/v1/survivor/create/')

def views(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return redirect('/api/v1/survivor/login')

def transacoes(request):
    if request.method == 'GET':
        return render(request, 'transacoes.html')
    else:
        return redirect('api/v1/survivor/login')

def antecipacao(request):
    if request.method == 'GET':
        return render(request, 'antecipacao.html')
    else:
        return redirect('api/v1/survivor/login')

def futurepay(request):
    if request.method == 'GET':
        return render(request, 'payment.html')
    else:
        return redirect('api/v1/survivor/login')

def profile(request):
    if request.method == 'GET':
        return render(request, 'profile.html')
    else:
        return redirect('api/v1/survivor/login')

def repasse(request):
    if request.method == 'GET':
        return render(request, 'repasse.html')
    else:
        return redirect('api/v1/survivor/login')

def split(request):
    if request.method == 'GET':
        return render(request, 'split.html')
    else:
        return redirect('api/v1/survivor/login')