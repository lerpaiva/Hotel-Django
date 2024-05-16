
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name = "home"),
    path('quarto', views.quarto , name= "quarto"),
    # path('nome', views.nome, name="nome")
]