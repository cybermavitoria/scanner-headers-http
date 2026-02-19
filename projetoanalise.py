import requests
# Lista principais headers
HEADERS_SEGURANCA = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
]
url = input("Digite uma URL: ")
resposta = requests.get(url)

print("\n--- Analise de Seguranca ---\n")
for header in HEADERS_SEGURANCA:
    if header in resposta.headers:
        print(f"[OK] {header}: presente")
    else:
        print(f"[AUSENTE] {header}: ausente")

