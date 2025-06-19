import requests

url = "https://brasilapi.com.br/api/taxas/v1/selic"
resposta = requests.get(url)
dados = resposta.json()

print(f"A taxa Selic de hoje é {dados['valor']}%")

