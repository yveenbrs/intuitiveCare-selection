import requests

def download_pdf(path, url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(path, "wb") as f:
            f.write(response.content)
        print(f"""Salvando o arquivo: {url} 
    Local: {path}""")
    except requests.RequestException as e:
        print(f"Falha ao baixar o arquivo: {url}")
