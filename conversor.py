import requests

def currency_converter(amount, from_currency, to_currency):
    API_KEY = "bf5651db87f988a3d13f6c5f"
    url = f"https://v6.exchangerate-api.com/v6/{bf5651db87f988a3d13f6c5f/latest/USD}/pair/{from_currency}/{to_currency}/{amount}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        return result["conversion_result"]
    else:
        return "Erro ao consultar a API"

amount = float(input("Digite o valor que deseja converter: "))
from_currency = input("Digite a moeda de origem: ")
to_currency = input("Digite a moeda de destino: ")
converted_amount = currency_converter(amount, from_currency.upper(), to_currency.upper())
print(f"{amount:.2f} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")