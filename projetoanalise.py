import requests #Importe requests
from datetime import datetime
from urllib.parse import urlparse #Importar biblioteca
HEADERS_SEGURANCA = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]
def normalizar_url(url): #definir a função normalizar
    url = url.strip()
    endereco = urlparse(url)
    if not endereco.scheme: #condicionais feitas
        return f"https://{url}"
    return url
def separar_urls(entrada): #definir
    return [url.strip() for url in entrada.split(",") if url.strip()]
def analisar(url):
    url = normalizar_url(url)
    resposta = requests.get(url)
    resultado = []
    resultado.append(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    resultado.append(f"URL analisada: {url}\n")

    for header in HEADERS_SEGURANCA: #loops e condicionais
        if header in resposta.headers:
            resultado.append(f"[OK] {header}: presente")
        else:
            resultado.append(f"[AUSENTE] {header}: ausente")

    return resultado
entrada = input("Digite uma ou mais URLs separadas por virgula: ") #interção com o usuário
urls = separar_urls(entrada)
relatorio_completo = []

for url in urls:
    resultado = analisar(url)
    for linha in resultado:
        print(linha)
    print("-" * 40)
    relatorio_completo.extend(resultado)

with open("relatorio.txt", "w") as arquivo:
    arquivo.write("\n".join(relatorio_completo))

print("\nRelatorio salvo em relatorio.txt")
