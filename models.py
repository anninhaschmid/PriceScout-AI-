from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    url_loja = models.URLField(unique=True)
    preco_alvo = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class AnaliseProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='analises')
    preco_registrado = models.DecimalField(max_digits=10, decimal_places=2)
    score_confianca = models.IntegerField()
    alerta_defeito_lote = models.BooleanField(default=False)
    resumo_geral = models.TextField()
    data_analise = models.DateTimeField(auto_now_add=True)
