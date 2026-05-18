import requests
from bs4 import BeautifulSoup   

url = "https://store.steampowered.com/app/495420/State_of_Decay_2_Juggernaut_Edition/"


# Faz requisição da página e retorna HTML
def get_html(url):
    response = requests.get(url)
    html = response.text 

    return html


# Extrai informações principais do jogo
def extract_game_data():
    html = get_html(url)

    soup = BeautifulSoup(html, "html.parser")

    title = soup.find('div', class_="apphub_AppName")
    price = soup.find('div', class_="game_purchase_price price")

    # Retorna apenas se os dois elementos existirem
    if title and price:
        return title.text, price.text.strip()
    else:
        return None


# Organiza os dados em formato de dicionário
def create_game_dict():
    result = extract_game_data()

    # Evita erro caso não exista resultado
    if not result:
        return None

    title, price = result

    game_dict = {
        'title': title,
        'price': price
    }
    
    return game_dict


# Exibe informações do jogo no terminal
def show_info():
    game_dict = create_game_dict()

    if game_dict:
        print("\nGame information:")
        print(f"Title: {game_dict['title']}")
        print(f"Price: {game_dict['price']}")
    else:
        print("No data found.")


# Execução principal
show_info()