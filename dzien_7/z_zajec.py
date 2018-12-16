import pickle
import smtplib
import pprint
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def otworz_dziennik(plik_dziennika):
    """
    Funkcja która otwiera plik dzinnika i zwraca handler do pliku w trybie zapis/odczyt
    :param plik_dziennika:
    :return:
    """
    dziennik = open(plik_dziennika, 'rb+')
    return dziennik

def zamknij_dziennik(plik_dz):
    """
    Funkcja która zamyka plik dzinnika
    :param plik_dz:
    :return:
    """
    plik_dz.close()

def dodaj_wpis(plik_dz):
    """
    Funkcja, która pyta użytkownika o dane do nowego wpisu i dodaje go do aktualnej listy plików
    :param plik_dz:
    :return:
    """
    data = input("Podaj datę: ")
    tresc = input("Podaj treść: ")
    nowy_wpis = {"data": data, "tresc": tresc}

    stare_wpisy = przeczytaj_plik(plik_dz)
    nowe_wpisy = stare_wpisy

    try:
        nowe_wpisy.append(nowy_wpis)
    except:
        print('Nie było żadnego wpisu. Dodaje pierwszy wpis :)')
        nowe_wpisy = []
        nowe_wpisy.append(nowy_wpis)

    plik_dz.seek(0)
    pickle.dump(nowe_wpisy, plik_dz)
    print("Wpis został dodany prawidłowo.")

def wyswietl_menu():
    """
    Proste wyświtlanie
    :return:
    """
    print("Mój dziennik v0.1 alpha\n"
          "1. Wyświetlanie\n"
          "2. Dodawanie\n"
          "3. Usuwanie\n"
          "4. Szukanie\n"
          "5. Wyjscie")

def przeczytaj_plik(plik_dz):
    """
    Funckja która z otwartego pliku czyta dane i zwraca nam w naszym przypadku w postaci listy słowników
    czyli dokłądnie tak jak je zapisujemy (użycie picka)
    :param plik_dz:
    :return:
    """
    try:
        dane = pickle.load(plik_dz)
        return dane
    except:
        print('Błąd')

def usun_wpis(plik_dz):
    """
    Funckaj usuwa wpis z dziennika na podstawie numeru podanego przez użytkownika
    Dodatkowo po usunięciu wysyła mail informacyjnego
    :param plik_dz:
    :return:
    """
    wpisy = przeczytaj_plik(plik_dz)
    ilosc_wpisow = len(wpisy)
    print("Ilość wpisów w dzienniczku to: {}".format(ilosc_wpisow))
    wpis_do_usuniecia = int(input("Proszę podaj wpis"))

    if wpis_do_usuniecia <= ilosc_wpisow and wpis_do_usuniecia > 0:
        indeks_do_usuniecia = wpis_do_usuniecia-1
        del(wpisy[indeks_do_usuniecia])
        plik_dz.seek(0)

        temat = "Ktoś usunął wpis"
        tresc = "Usunięto wpis o indeksie: {}".format(indeks_do_usuniecia)
        tresc = tresc + "\na dla użytkownika jest to wpis numer: {}".format(wpis_do_usuniecia)

        wyslij_mail(temat, tresc)
        pickle.dump(wpisy, plik_dz)
        print("Właśnie usunąłem wpis")
    else:
        print("Nie ma takiego wpisu")

def wyslij_mail(temat, tresc):
    """
    Funkcaj która wysła maila o określonym temacie i treści do "isapy@o2.pl"
    :param temat: temat maila
    :param tresc: tresc maila
    :return:
    """

    mail = MIMEMultipart()
    mail["Subject"] = temat
    mail["To"] = 'damianseredyn@gmail.com'
    mail["From"] = 'isapy@int.pl'

    body = MIMEText(tresc)
    mail.attach(body)

    serwer = smtplib.SMTP('poczta.int.pl')
    serwer.login('isapy@int.pl', 'isapython;')
    serwer.send_message(mail)
    serwer.quit()

    print("Wysłano mail!")

def wyszukaj(plik_dz):
    """
    Funkcja w otwartym dzienniku szuka wpisu zawierającego w tresc zadaną przez użytkownika fraze
    Wyświetla też podsumowanie wyszukiwania
    :param plik_dz:
    :return:
    """
    wpisy = przeczytaj_plik(plik_dz)
    fraza = input("Podaj szukaną treść: ")

    znaleziono_cos = False
    ilosc_wynikow = 0
    for index, wpis in enumerate(wpisy):
        if fraza in wpis["tresc"]:
            znaleziono_cos = True
            ilosc_wynikow += 1
            print(wpis["tresc"])
            print('Na indeksie: {}'.format(index))

    if ilosc_wynikow == 0:
        print("W całym dzienniku nie ma takiej frazy")
    else:
        print("Ilość wpisów: {}".format(ilosc_wynikow))

    # if znaleziono_cos is False:
    #     print("W całym dzienniku nie ma takiej frazy")

def zapytaj():
    """
    Nasz pseudo "controler" do zarządzania flow w programie
    :return:
    """
    decyzja = input("Co wybierasz?")
    if decyzja == "1":
        print("Oto twoje wpisy:")

        plik_dz = otworz_dziennik(plik_dziennika)
        wpisy = przeczytaj_plik(plik_dz)
        pprint.pprint(wpisy)
        zamknij_dziennik(plik_dz)
    if decyzja == "2":
        print("Dodawanie wpisu:")

        plik_dz = otworz_dziennik(plik_dziennika)
        dodaj_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == "3":
        print("Usuń wpis:")

        plik_dz = otworz_dziennik(plik_dziennika)
        usun_wpis(plik_dz)
        zamknij_dziennik(plik_dz)
    if decyzja == "4":
        print("Wyszukiwarka:")

        plik_dz = otworz_dziennik(plik_dziennika)
        wyszukaj(plik_dz)
        zamknij_dziennik(plik_dz)
    elif decyzja == "5":
        exit()

plik_dziennika = 'dziennik.dz'

while True:
    wyswietl_menu()
    zapytaj()