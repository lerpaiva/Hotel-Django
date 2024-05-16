from django.db import models


# Create your models here.

#EM MINUSCULO É O QUE APARECE NA HORA DA INTERFACE, O MAÍUSCULO É O QUE FICARÁ NO BANCO DE DADOS
TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("CONFORTO", "Conforto"),
    ("LUXO", "Luxo")
)

#CLASS HOTEL, DUAS PROPRIEDADES COM TAMANHO MÁXIMO, CHARFIELD ESPERA POUCA COISA E TEXT PERMITE MAIS
class Hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.titulo

class Quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    disponibilidade = models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=255)
    foto = models.ImageField(upload_to="Foto_Quarto/")

    def __str__(self):
        return self.tipo

# class Usuario(models.Model):
#     nome = models.CharField(max_length=20)
#     sobrenome = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     idade = models.IntegerField()
#     endereco = models.CharField(max_length=60)
#     quarto = models.CharField(max_length=15, choices=TIPOS_QUARTOS)

#     def __str__(self):
#         return self.nome