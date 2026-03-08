import requests #Importe a biblioteca caso não tenha instalado
from datetime import datetime

HEADERS_SEGURANCA = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]
def analisar(url):
    resposta = requests.get(url)
    resultado = []
    resultado.append(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    resultado.append(f"URL analisada: {url}\n")

    for header in HEADERS_SEGURANCA:
        if header in resposta.headers:
            resultado.append(f"[OK] {header}: presente")
        else:
            resultado.append(f"[AUSENTE] {header}: ausente")

    for linha in resultado:
        print(linha)

    with open("relatorio.txt", "w") as arquivo:
        arquivo.write("\n".join(resultado))

    print("\nRelatorio salvo em relatorio.txt")

url = input("Digite uma URL: ")
analisar(url)
