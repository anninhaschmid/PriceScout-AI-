import json
import requests
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
from django.conf import settings

def extrair_dados_loja(url):
    # Simulação de scraping (ajuste as classes CSS conforme o e-commerce real)
    headers = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    
    # Exemplo genérico de extração
    preco_str = soup.find('span', class_='price-tag').text.replace('R$', '').replace(',', '.')
    avaliacoes = [div.text for div in soup.find_all('p', class_='review-text')[:15]]
    
    return float(preco_str), avaliacoes

def analisar_sentimento_gemini(avaliacoes):
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    
    prompt = """
    Analise as avaliações e retorne um JSON com:
    - score_confianca (0 a 100)
    - alerta_defeito_lote (bool - true se houver muitas queixas do mesmo problema)
    - resumo_geral (string)
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=f"Avaliações:\n{json.dumps(avaliacoes, ensure_ascii=False)}",
        config=types.GenerateContentConfig(
            system_instruction=prompt,
            response_mime_type="application/json",
            temperature=0.1
        )
    )
    return json.loads(response.text)
