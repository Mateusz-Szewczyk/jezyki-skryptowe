# Zadanie 1
def zbierz_dane_osobowe():
    dane = {}
    dane['imie'] = input("Podaj imię: ")
    dane['nazwisko'] = input("Podaj nazwisko: ")
    while True:
        try:
            dane['wiek'] = int(input("Podaj wiek: "))
            break
        except ValueError:
            print("Proszę podać prawidłowy wiek (liczba całkowita).")
    print("Zebrane dane:", dane)
    return dane


# Zadanie 2
def zwroc_wieksza(a, b):
    wynik = max(a, b)
    print(f"Większa liczba z {a} i {b} to {wynik}.")
    return wynik


# Zadanie 3
def suma_listy(lista):
    wynik = sum(lista)
    print(f"Suma listy {lista} wynosi {wynik}.")
    return wynik


# Zadanie 4
def znajdz_minimum(*args):
    if args:
        wynik = min(args)
        print(f"Minimum z {args} to {wynik}.")
        return wynik
    else:
        print("Brak argumentów do znalezienia minimum.")
        return None


# Zadanie 5
lista_studentow = []


def dodaj_studenta():
    imie = input("Podaj imię studenta: ")
    nazwisko = input("Podaj nazwisko studenta: ")
    grupa = input("Podaj grupę studenta: ")
    while True:
        obecny_input = input("Czy student jest obecny? (T/N): ").strip().upper()
        if obecny_input in ['T', 'N']:
            obecny = obecny_input == 'T'
            break
        else:
            print("Proszę wpisać 'T' lub 'N'.")
    student = {
        'imie': imie,
        'nazwisko': nazwisko,
        'grupa': grupa,
        'obecny': obecny
    }
    lista_studentow.append(student)
    print(f"Dodano studenta: {student}")


# Zadanie 6
def operacja_na_liczbie(liczba, lista=None):
    if lista is None:
        lista = []
    lista.append(liczba)
    print("Aktualna zawartość listy:", lista)
    return lista


# Zadanie 7
import random

dostepne_taksowki = []
zajete_taksowki = []


def menu_taxi():
    print("\nSystem TAXI")
    print("1. Dodaj taksówkę")
    print("2. Zarejestruj przejazd")
    print("3. Aktualizuj czas przejazdów")
    print("4. Wyświetl informacje")
    print("5. Wyjdź z systemu TAXI")


def dodaj_taksowke():
    rejestracja = input("Podaj numer rejestracyjny taksówki: ").strip().upper()
    if rejestracja in dostepne_taksowki or any(t['taksowka'] == rejestracja for t in zajete_taksowki):
        print(f"Taksówka {rejestracja} już istnieje w systemie.")
    else:
        dostepne_taksowki.append(rejestracja)
        print(f"Taksówka {rejestracja} dodana do floty!")


def zarejestruj_przejazd():
    if not dostepne_taksowki:
        print("Brak dostępnych taksówek!")
        return

    pasazer = input("Podaj nazwisko pasażera: ").strip().title()
    start = input("Podaj miejsce odbioru: ").strip().title()
    cel = input("Podaj miejsce docelowe: ").strip().title()

    taksowka = dostepne_taksowki.pop(0)
    czas = random.randint(1, 5)

    zajete_taksowki.append({
        'taksowka': taksowka,
        'pasazer': pasazer,
        'start': start,
        'cel': cel,
        'czas': czas
    })
    print(f"Przejazd zarejestrowany! Taksówka {taksowka} w trasie do {cel}.")


def aktualizuj_czas():
    for przejazd in zajete_taksowki:
        przejazd['czas'] -= 1

    do_zwolnienia = [p for p in zajete_taksowki if p['czas'] <= 0]

    for przejazd in do_zwolnienia:
        dostepne_taksowki.append(przejazd['taksowka'])
        zajete_taksowki.remove(przejazd)
        print(f"Taksówka {przejazd['taksowka']} wróciła do floty!")


def wyswietl_informacje():
    print("\nDostępne taksówki:", dostepne_taksowki if dostepne_taksowki else "Brak dostępnych taksówek.")
    print("\nAktualne przejazdy:")
    if zajete_taksowki:
        for przejazd in zajete_taksowki:
            print(f"Taksówka: {przejazd['taksowka']}, Pasażer: {przejazd['pasazer']}")
            print(f"Trasa: {przejazd['start']} -> {przejazd['cel']}")
            print(f"Pozostały czas: {przejazd['czas']} jednostek\n")
    else:
        print("Brak aktualnych przejazdów.")


def system_taxi():
    while True:
        menu_taxi()
        wybor = input("Wybierz opcję: ").strip()

        if wybor == '1':
            dodaj_taksowke()
        elif wybor == '2':
            zarejestruj_przejazd()
        elif wybor == '3':
            aktualizuj_czas()
        elif wybor == '4':
            wyswietl_informacje()
        elif wybor == '5':
            print("Zamykanie systemu TAXI...")
            break
        else:
            print("Nieprawidłowy wybór! Proszę wybrać opcję od 1 do 5.")


# Główne menu do wyboru zadania
def main_menu():
    while True:
        print("\n--- Główne Menu ---")
        print("1. Zadanie 1: Zbierz dane osobowe")
        print("2. Zadanie 2: Zwróć większą liczbę")
        print("3. Zadanie 3: Suma listy")
        print("4. Zadanie 4: Znajdź minimum")
        print("5. Zadanie 5: Dodaj studenta")
        print("6. Zadanie 6: Operacja na liczbie")
        print("7. Zadanie 7: System TAXI")
        print("8. Wyjście")

        wybor = input("Wybierz numer zadania do przetestowania (1-8): ").strip()

        if wybor == '1':
            zbierz_dane_osobowe()
        elif wybor == '2':
            try:
                a = float(input("Podaj pierwszą liczbę: "))
                b = float(input("Podaj drugą liczbę: "))
                zwroc_wieksza(a, b)
            except ValueError:
                print("Proszę podać prawidłowe liczby.")
        elif wybor == '3':
            lista = []
            while True:
                element = input("Podaj element listy (lub 'stop' aby zakończyć): ").strip()
                if element.lower() == 'stop':
                    break
                try:
                    liczba = float(element)
                    lista.append(liczba)
                except ValueError:
                    print("Proszę podać prawidłową liczbę.")
            if lista:
                suma_listy(lista)
            else:
                print("Lista jest pusta.")
        elif wybor == '4':
            args = []
            while True:
                element = input("Podaj liczbę (lub 'stop' aby zakończyć): ").strip()
                if element.lower() == 'stop':
                    break
                try:
                    liczba = float(element)
                    args.append(liczba)
                except ValueError:
                    print("Proszę podać prawidłową liczbę.")
            znajdz_minimum(*args)
        elif wybor == '5':
            dodaj_studenta()
        elif wybor == '6':
            try:
                liczba = float(input("Podaj liczbę do dodania: "))
                lista_input = input("Podaj listę (oddzielone przecinkami) lub pozostaw puste: ").strip()
                if lista_input:
                    lista = [float(x.strip()) for x in lista_input.split(',') if x.strip()]
                else:
                    lista = None
                operacja_na_liczbie(liczba, lista)
            except ValueError:
                print("Proszę podać prawidłowe dane.")
        elif wybor == '7':
            system_taxi()
        elif wybor == '8':
            print("Wyjście z programu. Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór! Proszę wybrać opcję od 1 do 8.")


# Wywołanie głównego menu
if __name__ == "__main__":
    main_menu()
