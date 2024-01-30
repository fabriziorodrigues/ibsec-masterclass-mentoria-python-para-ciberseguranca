import requests

def verificar_url_virustotal(url, api_key):
    # URL da API do VirusTotal
    url_api = 'https://www.virustotal.com/vtapi/v2/url/report'

    # Parâmetros da requisição
    params = {'apikey': api_key, 'resource': url}

    # Enviando a requisição GET
    response = requests.get(url_api, params=params)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return f"Erro na requisição: {response.status_code}"

# Sua chave de API do VirusTotal
api_key = 'SUA_CHAVE_DE_API_AQUI'

# URL para verificar
url_teste = 'http://www.exemplo.com'

# Chamando a função e imprimindo o resultado
resultado = verificar_url_virustotal(url_teste, api_key)
print(resultado)
