import json
import csv


# Zadanie 1: Obsługa plików
def zadanie1_obsługa_plikow():
    plik_nazwa = 'przykladowy_plik.txt'

    # Tworzenie i zapisywanie do pliku
    with open(plik_nazwa, 'w', encoding='utf-8') as f:
        f.write("Linia 1: To jest przykładowy plik tekstowy.\n")
        f.write("Linia 2: Python jest świetny do obsługi plików.\n")
        f.write("Linia 3: To jest ostatnia linia.\n")
    print(f"\nPlik '{plik_nazwa}' został utworzony i zapisany.\n")

    # Odczyt za pomocą read()
    print("Odczyt za pomocą read():")
    with open(plik_nazwa, 'r', encoding='utf-8') as f:
        zawartosc = f.read()
        print(zawartosc)

    # Odczyt za pomocą readline()
    print("Odczyt za pomocą readline():")
    with open(plik_nazwa, 'r', encoding='utf-8') as f:
        pierwsza_linija = f.readline()
        print(pierwsza_linija.strip())

    # Iteracja po pliku
    print("Iteracja po pliku:")
    with open(plik_nazwa, 'r', encoding='utf-8') as f:
        for linia in f:
            print(linia.strip())

    # Odczyt za pomocą with
    print("Odczyt za pomocą bloku with:")
    try:
        with open(plik_nazwa, 'r', encoding='utf-8') as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print(f"Plik '{plik_nazwa}' nie został znaleziony.")


# Zadanie 2: Serializacja obiektów - JSON
def zadanie2_biblioteka_filmow():
    plik_json = 'filmy.json'

    # Wczytywanie istniejącej biblioteki lub tworzenie nowej
    try:
        with open(plik_json, 'r', encoding='utf-8') as f:
            biblioteka = json.load(f)
            print(f"\nZaładowano istniejącą bibliotekę filmów z '{plik_json}'.\n")
    except FileNotFoundError:
        biblioteka = []
        print(f"\nPlik '{plik_json}' nie istnieje. Tworzę nową bibliotekę filmów.\n")

    while True:
        tytul = input("Podaj tytuł filmu (lub naciśnij Enter, aby zakończyć): ").strip()
        if not tytul:
            break
        try:
            srednia_ocena = float(input("Podaj średnią ocenę filmu: "))
            rok_wydania = int(input("Podaj rok wydania filmu: "))
        except ValueError:
            print("Proszę podać prawidłowe dane (ocena jako liczba, rok jako liczba całkowita).")
            continue

        film = {
            'tytul': tytul,
            'srednia_ocena': srednia_ocena,
            'rok_wydania': rok_wydania
        }
        biblioteka.append(film)
        print(f"Film '{tytul}' dodany do biblioteki.\n")

    # Zapisywanie biblioteki do pliku JSON
    with open(plik_json, 'w', encoding='utf-8') as f:
        json.dump(biblioteka, f, ensure_ascii=False, indent=4)
    print(f"Biblioteka filmów została zapisana do '{plik_json}'.\n")


# Zadanie 3: Serializacja obiektów - CSV
def zadanie3_dodawanie_studentow():
    plik_csv = 'studenci.csv'

    # Sprawdzanie czy plik istnieje, aby dodać nagłówki
    try:
        with open(plik_csv, 'r', encoding='utf-8', newline='') as f:
            reader = csv.reader(f)
            existing = list(reader)
            if not existing:
                raise FileNotFoundError
    except FileNotFoundError:
        with open(plik_csv, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Numer Albumu', 'Ocena Końcowa'])
        print(f"\nPlik '{plik_csv}' został utworzony z nagłówkami.\n")

    try:
        liczba_studentow = int(input("Ilu studentów chcesz dodać? "))
        if liczba_studentow <= 0:
            print("Liczba studentów musi być większa niż zero.")
            return
    except ValueError:
        print("Proszę podać prawidłową liczbę całkowitą.")
        return

    with open(plik_csv, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for i in range(liczba_studentow):
            numer_albumu = input(f"Podaj numer albumu studenta {i + 1}: ").strip()
            if not numer_albumu:
                print("Numer albumu nie może być pusty. Pomijam tego studenta.")
                continue
            try:
                ocena_koncowa = float(input(f"Podaj ocenę końcową studenta {i + 1}: "))
            except ValueError:
                print("Ocena musi być liczbą. Pomijam tego studenta.")
                continue
            writer.writerow([numer_albumu, ocena_koncowa])
            print(f"Student {numer_albumu} z oceną {ocena_koncowa} został dodany.\n")
    print(f"Wszystkie dane zostały zapisane do '{plik_csv}'.\n")


# Zadanie 4: Wyjątki
class NegativeNumberError(Exception):
    """Wyjątek podnoszony, gdy liczba jest ujemna."""
    pass


def zadanie4_obsluga_wyjatkow():
    def sprawdz_liczbe(liczba):
        if liczba < 0:
            raise NegativeNumberError("Liczba nie może być ujemna!")
        return liczba

    try:
        liczba = float(input("Podaj liczbę (nieujemną): "))
        wynik = sprawdz_liczbe(liczba)
        print(f"Podana liczba to: {wynik}")
    except NegativeNumberError as e:
        print(f"Błąd: {e}")
    except ValueError:
        print("Proszę podać prawidłową liczbę.")


# Zadanie 5: Pętla while True z obsługą wyjątków
def zadanie5_pobieranie_wieku():
    while True:
        try:
            wiek = int(input("Podaj swój wiek: "))
            if wiek < 0:
                raise ValueError("Wiek nie może być ujemny.")
            print(f"Twój wiek to: {wiek} lat.")
            break
        except ValueError as e:
            print(f"Błąd: {e}. Spróbuj ponownie.\n")


# Główne menu do wyboru zadania
def main_menu():
    while True:
        print("\n--- Główne Menu ---")
        print("1. Zadanie 1: Obsługa plików")
        print("2. Zadanie 2: Biblioteka Filmów (JSON)")
        print("3. Zadanie 3: Dodawanie Studentów (CSV)")
        print("4. Zadanie 4: Obsługa Wyjątków")
        print("5. Zadanie 5: Pobieranie Wieków (Loop)")
        print("6. Wyjście")

        wybor = input("Wybierz numer zadania do wykonania (1-6): ").strip()

        if wybor == '1':
            zadanie1_obsługa_plikow()
        elif wybor == '2':
            zadanie2_biblioteka_filmow()
        elif wybor == '3':
            zadanie3_dodawanie_studentow()
        elif wybor == '4':
            zadanie4_obsluga_wyjatkow()
        elif wybor == '5':
            zadanie5_pobieranie_wieku()
        elif wybor == '6':
            print("Zakończenie programu. Do zobaczenia!")
            break
        else:
            print("Nieprawidłowy wybór! Proszę wybrać opcję od 1 do 6.")


# Wywołanie głównego menu
if __name__ == "__main__":
    main_menu()
