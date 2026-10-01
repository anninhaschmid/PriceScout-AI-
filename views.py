from django.http import JsonResponse
from django.core.mail import send_mail
from .models import Produto, AnaliseProduto
from .services import extrair_dados_loja, analisar_sentimento_gemini

def processar_rastreamento(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
        
        # 1. Coleta os dados novos
        preco_atual, avaliacoes = extrair_dados_loja(produto.url_loja)
        
        # 2. Processa com a IA
        resultado_ia = analisar_sentimento_gemini(avaliacoes)
        
        # 3. Salva no banco de dados
        analise = AnaliseProduto.objects.create(
            produto=produto,
            preco_registrado=preco_atual,
            score_confianca=resultado_ia['score_confianca'],
            alerta_defeito_lote=resultado_ia['alerta_defeito_lote'],
            resumo_geral=resultado_ia['resumo_geral']
        )
        
        # 4. Lógica de Disparo
        if preco_atual <= produto.preco_alvo and analise.score_confianca >= 70:
            if not analise.alerta_defeito_lote:
                send_mail(
                    subject=f"Alerta de Preço: {produto.nome}",
                    message=f"O preço caiu para R${preco_atual}! \nAnálise da IA: {analise.resumo_geral}",
                    from_email="alertas@seuprojeto.com",
                    recipient_list=["usuario@email.com"],
                )
                return JsonResponse({"status": "Alerta enviado", "dados": resultado_ia})
        
        return JsonResponse({"status": "Preço alto ou risco detectado", "dados": resultado_ia})

    except Exception as e:
        return JsonResponse({"erro": str(e)}, status=400)
