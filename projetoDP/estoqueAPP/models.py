from django.db import models


class EstoqueModel(models.Model):
    nome = models.CharField(max_length=65)
    descricao = models.TextField(max_length=100, null=True, blank=True)
    em_estoque = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
