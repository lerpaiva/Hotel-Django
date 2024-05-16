from django.shortcuts import render, HttpResponse
from .models import Hotel, Quarto




def homepage(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    return render(request, "homepage.html", context)

def quarto(request):
    context = {}
    dados_hotel = Hotel.objects.all()
    context["dados_hotel"] = dados_hotel
    dados_quarto = Quarto.objects.all()
    context["dados_quarto"] = dados_quarto
    print(dados_quarto)
    return render(request, "quarto.html", context)

# def nome(request):
#     context = {}
#     dados_hotel = Hotel.objects.all()
#     context["dados_hotel"] = dados_hotel
#     dados_quarto = Quarto.objects.all()
#     context["dados_quarto"] = dados_quarto

#     if request.method == "POST":
#         form = FormNome(request.POST)
#         if form.is_valid():
#             var_nome = form.cleaned_data['nome']
#             var_email = form.cleaned_data['email']
#             var_sobrenome = form.cleaned_data['sobrenome']
#             int_idade = form.cleaned_data['idade']
#             var_endereco = form.cleaned_data['endereco']
#             choice_quarto = form.cleaned_data['quarto']
#             user = Usuario( nome= var_nome, sobrenome=var_sobrenome, email=var_email, idade = int_idade, endereco = var_endereco, quarto = choice_quarto )
#             user.save()
#             return HttpResponse("<h1>thanks</h1>")

#     else:
#         form = FormNome()
#     context['form'] = form
#     return render(request, "nome.html", context)

# Create your views here.
