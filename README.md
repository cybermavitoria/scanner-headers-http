# Scanner de Headers de Segurança HTTP
Ferramenta em Python que analisa os headers de segurança de um site e identifica quais estão ausentes.
NOVIDADE: Salva o resultado automaticamente em relatorio.txt com data e hora da analise
Como usar
1. Instale a dependência:
pip install requests
2. Rode o script:
python projetoanalise.py
3. Digite a URL que deseja analisar
- Headers verificados
- Strict-Transport-Security
- Content-Security-Policy
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy
