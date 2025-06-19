from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou um Bot Sagaz que te diz a taxa Selic hoje. Envie /selic para saber a taxa de hoje.")

async def selic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://brasilapi.com.br/api/taxas/v1/selic"
    resposta = requests.get(url)
    dados = resposta.json()
    valor = dados.get('valor')
    nome = dados.get('nome', 'Selic')

    if valor is None:
        mensagem = "! Não consegui obter a taxa Selic no momento."
    else:
        mensagem = f"📊 A taxa {nome} hoje é: {valor}%."

    await update.message.reply_text(mensagem)


Token = "1293602473:AAHw50uQMd9hs-_ueBdzbSs0TerXpiC4Nnk"

app = ApplicationBuilder().token(Token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("selic", selic))
app.run_polling()
