from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import requests
import os

load_dotenv()
Token = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "👋 Olá, meu caro! Sou um Bot Econômico Sagaz.\n"
        "Posso te dizer várias informações econômicas sensacionais\n"
        "Veja em /ajuda. Tamo junto, já é."
    ) 
    await update.message.reply_text(mensagem)
    

async def selic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://brasilapi.com.br/api/taxas/v1/selic"
    resposta = requests.get(url)
    dados = resposta.json()
    valor = dados.get('valor')
    nome = dados.get('nome', 'Selic')

    if valor is None:
        mensagem = "Erro, não consegui obter a taxa Selic no momento."
    else:
        mensagem = f"📊 A taxa {nome} hoje é: {valor}%."

    await update.message.reply_text(mensagem)

async def dolar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    valor = float(dados['USDBRL']['bid'])

    if valor is None:
        mensagem = "Erro, não consegui obter o valor do dólar no momento."
    else:
        mensagem = f"💵 A cotação atual do dólar é: R$ {valor:.2f}"
    
    await update.message.reply_text(mensagem)

async def ipca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://brasilapi.com.br/api/taxas/v1/ipca"
    resposta = requests.get(url)
    dados = resposta.json()
    valor = dados.get('valor', 'Indisponível')

    if valor is None:
        mensagem = "Erro, não consegui obter a taxa IPCA no momento."
    else:
        mensagem = f"📊 O IPCA acumulado é: {valor:.2f}%"
    
    await update.message.reply_text(mensagem)

async def cdi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://brasilapi.com.br/api/taxas/v1/cdi"
    resposta = requests.get(url)
    dados = resposta.json()
    valor = dados.get('valor')

    if valor is None:
        mensagem = "Erro, não consegui obter a taxa CDI no momento."
    else:
        mensagem = f"📊 O valor do CDI hoje é: {float(valor):.2f}%"
    
    await update.message.reply_text(mensagem)


async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "📌 *Comandos disponíveis:*\n"
        "/start – Mensagem de boas-vindas\n"
        "/selic – Taxa Selic do dia\n"
        "/dolar – Cotação atual do dólar\n"
        "/ipca – Inflação IPCA acumulada\n"
        "/cdi – Valor da taxa CDI\n"
        "/ajuda – Esta lista de comandos"
    )
    await update.message.reply_text(mensagem, parse_mode="Markdown")

app = ApplicationBuilder().token(Token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("selic", selic))
app.add_handler(CommandHandler("dolar", dolar))
app.add_handler(CommandHandler("ipca", ipca))
app.add_handler(CommandHandler("cdi", cdi))
app.add_handler(CommandHandler("ajuda", ajuda))

app.run_polling()
