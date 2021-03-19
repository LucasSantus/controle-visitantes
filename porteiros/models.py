from django.db import models

class Porteiro(models.Model):
    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=194,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="Telefone de Contato",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now=False,
        auto_now_add=False,
    )