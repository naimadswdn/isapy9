import requests
from bs4 import BeautifulSoup
import os
import errno

try:
    os.makedirs('obrazki')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

adres_strony = 'https://wallpaperlist.com'

# pobieramy źródło strony do zmiennej
zrodlo_strony = requests.get(adres_strony).content

# tworzymy parser BeautifulSoup z podanego źródła strony dzięki temu będziemy mieli łatwy dostęp do znaczników HTML
parser = BeautifulSoup(zrodlo_strony, 'html.parser')

# wyszukujemy wszystkie znaczniki <img> w źródle strony
obrazki = parser.find_all('img')

for obraz in obrazki:
    # w każdym pojedynczym znaczniki <img> odczytujemy wartość atrybutu "src" - jest tam link do danego obrazka
    # dodajemy do linku domene bo link ten jest linkiem względnym (nie zaczyna się od https)
    adres_obrazka = adres_strony + obraz["src"]
    print(adres_obrazka)
    nazwa_obrazka = adres_obrazka.split("/")[-1]
    print(nazwa_obrazka)

    # pobieramy zawartość obrazka za pomocą znanego już nam modułu i metody :)
    dane_obrazka = requests.get(adres_obrazka).content

    # Algorytm
    # 1. Utwórz katalog "obrazki"
    # 2. Przeczytaj dane pierwszego/kolejnego obrazka
    # 3. Z adresu obrazka pobież nazwę pliku (to co jest po ostatnim znaku "/")
    # 4. Zapisz plik o nazwie z pkt.3 w katalogu z pkt.1 i z zawartością danego obrazka
    # 5. Przejdź do pkt.2
    # 6. Wyświetl komunikat że udało się zapisać wszystkie obrazki ze strony na dysku :)