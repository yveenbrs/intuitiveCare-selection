import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print("Erro ao acessar a página: ", response.status_code)
        return None


def localize_files(html):
    analyzer = BeautifulSoup(html, "html.parser")
    return [a["href"] for a in analyzer.find_all("a", href=True) if a["href"].endswith(".pdf") and "Anexo" in a["href"]]
