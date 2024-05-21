from django.shortcuts import render, HttpResponse
from .models import Hotel, Quarto, Usuario
from .forms import FormNome, FormCadastro, FormLogin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login




def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render (request, 'homepage.html', context)

def quarto(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    print(dados_quarto)
    return render(request, "quarto.html", context)

def cadastro(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    
    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_first_name = form.cleaned_data['first_name']
            var_last_name = form.cleaned_data['last_name']
            var_user = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_password = form.cleaned_data['password']
            user = User.objects.create_user( username=var_user,  email=var_email, password=var_password )
            user.first_name = var_first_name
            user.last_name = var_last_name
            user.save()
            return redirect('login')

    else:
        form = FormCadastro()
        context['form'] = form
    return render(request, "cadastro.html", context)

def login(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto

    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            var_user = form.cleaned_data['user']
            var_password = form.cleaned_data['password']
            user = authenticate(username=var_user, password=var_password)
            if user is not None:
                
                return redirect('quarto')
            else:
                context['error_message'] = "Usuário ou senha incorretos"
    else:
        form = FormLogin()
    context['form'] = form
    return render(request, "login.html", context)

def reserva(request):
    if not request.user.is_authenticated:
        form = FormLogin()
        return render(request, 'login.html', {'form': form})

def reservar(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    
    if request.method == "POST":
        form = FormNome(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_sobrenome = form.cleaned_data['sobrenome']
            int_idade = form.cleaned_data['idade']
            var_endereco = form.cleaned_data['endereco']
            choice_quarto = form.cleaned_data['quarto']
            var_data = form.cleaned_data['data']
            user = Usuario( nome= var_nome, sobrenome=var_sobrenome, email=var_email, idade = int_idade, endereco = var_endereco, quarto = choice_quarto, data = var_data )
            user.save()
            return HttpResponse("<h1>thanks</h1>")

    else:
        form = FormNome()
    context['form'] = form
    return render(request, "reserva.html", context)
