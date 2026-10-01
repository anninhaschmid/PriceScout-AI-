# PriceScout AI 🛒🧠
**Preditor de Preços com Análise de Sentimento via IA**

Este repositório contém o Minimum Viable Product (MVP) desenvolvido para o **Projeto A3** do curso de **INTELIGENCIA ARTIFICIAL**. O sistema evolui o conceito tradicional de monitoramento de e-commerce ao integrar processamento de linguagem natural (NLP) para analisar o sentimento das avaliações recentes de consumidores, garantindo que descontos reais não sejam confundidos com lotes defeituosos.

## 🎯 O Problema
Muitas vezes, uma queda brusca de preço indica uma excelente promoção, mas também pode ser o reflexo de avaliações negativas recentes, falsificações ou queimas de estoque de produtos com falhas estruturais. O SmartAlerta cruza a métrica financeira com a opinião qualitativa dos compradores para aprovar ou reprovar a oferta.

## ✨ Funcionalidades
* **Web Scraping Dinâmico:** Extração automatizada do preço atual e dos últimos comentários deixados pelos compradores na página do produto.
* **Motor de Decisão (NLP):** Processamento das avaliações para identificar queixas repetitivas sobre o mesmo componente.
* **Score de Confiança:** Classificação algorítmica de 0 a 100 baseada na gravidade dos defeitos relatados.
* **Alertas Inteligentes:** Notificação ao usuário apenas quando o preço atinge o valor desejado e a inteligência artificial valida a integridade do lote.

## 🛠️ Stack Tecnológica
* **Back-end:** Python, Django
* **Inteligência Artificial:** Google Gemini API (Structured Outputs)
* **Banco de Dados & Autenticação:** Supabase (PostgreSQL)
* **Deploy da Aplicação Web:** Vercel

## 🚀 Arquitetura e Fluxo de Dados
1. O módulo de coleta (`services.py`) varre a URL cadastrada.
2. O prompt de sistema força a API da IA a retornar um modelo JSON estrito contendo o *Score de Confiança* e flags de *Alerta de Defeito*.
3. O histórico financeiro e analítico é persistido no banco relacional hospedado no Supabase.
4. O front-end, via Vercel, consome esses dados para renderizar os gráficos de viabilidade de compra.

## ⚙️ Como Executar Localmente

### Pré-requisitos
* Python 3.10 ou superior
* Conta e projeto configurado no Supabase
* Chave ativa da API do Google Gemini

### Passo a Passo

1. Clone este repositório e acesse o diretório:
```bash
git clone [https://github.com/seu-usuario/smartalerta.git](https://github.com/seu-usuario/smartalerta.git)
cd smartalerta
