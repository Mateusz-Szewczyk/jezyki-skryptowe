# Zadanie 1
lista_wyrazow = []

while True:
    slowo = input("Podaj slowo (wpisz q aby opuscic): \n")
    if slowo == "q":
        break
    lista_wyrazow.append(slowo)

while lista_wyrazow:
    print(lista_wyrazow.pop())

# Zadanie 2
import random
random.seed(21)

liczba_wygranych = 0
while liczba_wygranych < 3:
    wylosowana_liczba = random.randint(0, 10)
    print(f"Musisz wygrać jeszcze {3 - liczba_wygranych} razy żeby się stąd wydostać (mozesz opuscic 42)\n")
    while True:
        guess = int(input('Podaj liczbę: \n'))
        if guess == 42:
            liczba_wygranych = 10
            break
        if guess < wylosowana_liczba:
            print("Podana liczba jest za mała, spróbuj jeszcze raz :D\n")
        elif guess > wylosowana_liczba:
            print("Podana liczba jest za wysoka, spróbuj jeszcze raz :D\n")
        else:
            print("ZGADLES BRAWO!!!")
            liczba_wygranych += 1
            break

# Zadanie 3
moja_lista = ["Student", "UKEN", "Python"]
lista_uzytkownika = []

while True:
    slowo = input("Podaj slowo: (opusc za pomoca q)\n")
    if slowo == "q":
        break
    lista_uzytkownika.append(slowo)

for slowo in lista_uzytkownika:
    if slowo in moja_lista:
        print(slowo)

# Zadanie 4
miasta_populacja = {}

while True:
    miasto = input("Podaj miasto (wpisz 'q' aby zakończyć): ")
    if miasto == 'q':
        break
    populacja = int(input("Podaj populację: "))
    miasta_populacja[miasto] = populacja

print("\nInformacje o miastach:")
for miasto, populacja in miasta_populacja.items():
    print(f"{miasto}: {populacja} mieszkańców")

szukane_miasto = input("\nPodaj miasto do sprawdzenia populacji: ")
print(f"Populacja miasta {szukane_miasto}: {miasta_populacja.get(szukane_miasto, 'nieznana')}")

# Zadanie 5
lista = [1, 3, 7, 3, 2, 1, 8]

print("\nZawartość listy:")
for element in lista:
    print(element)

# Próba modyfikacji listy w trakcie iteracji
print("\nModyfikacja listy w trakcie iteracji:")
temp_lista = lista.copy()
for element in temp_lista:
    if element == 3:
        lista.remove(element)
    lista.append(9)
print("Zmodyfikowana lista:", lista)

# Nowa lista z wartościami nieparzystymi
nieparzyste = [x for x in lista if x % 2 != 0]
print("\nWartości nieparzyste:", nieparzyste)

# Sprawdzenie obecności wartości
wartosc = int(input("\nPodaj wartość do sprawdzenia: "))
print(f"Czy wartość {wartosc} jest w liście? {'Tak' if wartosc in lista else 'Nie'}")

# Wyświetlenie elementów bez pierwszego i ostatniego
if len(lista) >= 2:
    print("\nElementy bez pierwszego i ostatniego:", lista[1:-1])
else:
    print("\nLista jest za krótka, aby usunąć pierwszy i ostatni element.")

# Pobranie indeksu od użytkownika
try:
    indeks = int(input("\nPodaj indeks elementu do wyświetlenia: "))
    print(f"Element o indeksie {indeks}: {lista[indeks]}")
except IndexError:
    print("Podany indeks jest poza zakresem listy!")
except ValueError:
    print("To nie jest poprawny indeks!")