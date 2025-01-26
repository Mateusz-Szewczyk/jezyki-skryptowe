# Zadanie 1
def zbierz_dane_osobowe():
    dane = {}
    dane['imie'] = input("Podaj imię: ")
    dane['nazwisko'] = input("Podaj nazwisko: ")
    dane['wiek'] = int(input("Podaj wiek: "))
    return dane


# Zadanie 2
def zwroc_wieksza(a, b):
    return max(a, b)


# Zadanie 3
def suma_listy(lista):
    return sum(lista)


# Zadanie 4
def znajdz_minimum(*args):
    return min(args) if args else None


# Zadanie 5
lista_studentow = []


def dodaj_studenta():
    imie = input("Podaj imię studenta: ")
    nazwisko = input("Podaj nazwisko studenta: ")
    grupa = input("Podaj grupę studenta: ")
    obecny = input("Czy student jest obecny? (T/N): ").upper() == 'T'

    student = {
        'imie': imie,
        'nazwisko': nazwisko,
        'grupa': grupa,
        'obecny': obecny
    }
    lista_studentow.append(student)


# Zadanie 6
def operacja_na_liczbie(liczba, lista=None):
    if lista is None:
        lista = []
    lista.append(liczba)
    print("Aktualna zawartość listy:", lista)


# Zadanie 7
import random

dostepne_taksowki = []
zajete_taksowki = []


def menu():
    print("\nSystem TAXI")
    print("1. Dodaj taksówkę")
    print("2. Zarejestruj przejazd")
    print("3. Zwolnij taksówki")
    print("4. Wyświetl informacje")
    print("5. Zakończ program")


def dodaj_taksowke():
    rejestracja = input("Podaj numer rejestracyjny taksówki: ")
    dostepne_taksowki.append(rejestracja)
    print(f"Taksówka {rejestracja} dodana do floty!")


def zarejestruj_przejazd():
    if not dostepne_taksowki:
        print("Brak dostępnych taksówek!")
        return

    pasazer = input("Podaj nazwisko pasażera: ")
    start = input("Podaj miejsce odbioru: ")
    cel = input("Podaj miejsce docelowe: ")

    taksowka = dostepne_taksowki.pop(0)
    czas = random.randint(1, 5)

    zajete_taksowki.append({
        'taksowka': taksowka,
        'pasazer': pasazer,
        'start': start,
        'cel': cel,
        'czas': czas
    })
    print(f"Przejazd zarejestrowany! Taksówka {taksowka} w trasie.")


def aktualizuj_czas():
    for przejazd in zajete_taksowki:
        przejazd['czas'] -= 1

    do_zwolnienia = [p for p in zajete_taksowki if p['czas'] <= 0]

    for przejazd in do_zwolnienia:
        dostepne_taksowki.append(przejazd['taksowka'])
        zajete_taksowki.remove(przejazd)
        print(f"Taksówka {przejazd['taksowka']} wróciła do floty!")


def wyswietl_informacje():
    print("\nDostępne taksówki:", dostepne_taksowki)
    print("\nAktualne przejazdy:")
    for przejazd in zajete_taksowki:
        print(f"Taksówka: {przejazd['taksowka']}, Pasażer: {przejazd['pasazer']}")
        print(f"Trasa: {przejazd['start']} -> {przejazd['cel']}")
        print(f"Pozostały czas: {przejazd['czas']} jednostek\n")


# Główna pętla programu TAXI
def system_taxi():
    while True:
        menu()
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            dodaj_taksowke()
        elif wybor == '2':
            zarejestruj_przejazd()
        elif wybor == '3':
            aktualizuj_czas()
        elif wybor == '4':
            wyswietl_informacje()
        elif wybor == '5':
            print("Zamykanie systemu...")
            break
        else:
            print("Nieprawidłowy wybór!")


# Wywołanie przykładowych funkcji
if __name__ == "__main__":
    # Testowanie Zadania 6
    operacja_na_liczbie(5)
    operacja_na_liczbie(3, [1, 2])
    operacja_na_liczbie(7)

    # Uruchomienie systemu TAXI
    system_taxi()