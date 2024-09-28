# Zadanie 1

int1 = 3
int2 = 4

print(f"Typy int1 i int2 przed konwersją {type(int1)}")
print(f"Typy int1 i int2 po konwersji {type(float(int2))}\n")


# Zadanie 2

str1 = "5"

print(f"Typ str przed konwersją {type(str1)}")
print(f"Typ po konwersji na float {type(float(str1))}, i int {type(int(str1))}\n")


# Zadanie 3

print(f"Typy int1 i int2 przed konwersją {type(int1)}")
print(f"Typy int1 i int2 po konwersji {type(str(int2))}\n")


# Zadanie 4
int1 = 10
float2 = 5.5

print("\nZadanie 4\n\nArytmetyczne operacje dla int1:", (int1 + 500, int1 * 3, int1 / 2, int1 ** 2, int1 // 2))
print("Arytmetyczne operacje dla float:", (float2 + 250.5, float2 * 2.5, float2 / 3.0, float2 ** 2, round(float2) / 2))


# Zadanie 5

int1 = 10
float2 = 5.5

print(f"\n\nZadanie 5\n\nArytmetyczne operacje dla int4 (zamiast int1): {int1 + 500, int1 * 3, int1 / 2, int1 ** 2, int1 // 2}")
print(f"Arytmetyczne operacje dla float: {float2 + 250.5, float2 * 2.5, float2 / 3.0, float2 ** 2, round(float2) / 2}")


# Zadanie 6
krotka = (1,2,3)
print("\n(Problem) Jak zmodyfikować krotkę?")
print("Można zmienić krotkę na listę a następnie listę znowu na krotkę: ")
print(f"Krotka przed edycją: {krotka}")
lista = list(krotka)
lista[0] = 5
lista[2] = 40

krotka = tuple(lista)
print(f"Krotka po edycji: {krotka}")


# Zadanie 7

print("\n(Problem) Jak zapisać elementy krotki/listy/zbioru do osobnych zmiennych?\n")

krotka = (1,2,3)
lista = [1,2,3]
zbior = {1,2,3}

a1, b1, c1 = krotka
l1, l2, l3 = lista
z1, z2, z3 = zbior

print(f"Elementy krotki: {a1}, {b1}, {c1} \nElementy listy: {l1}, {l2}, {l3}")
print(f"Elementy zbioru: {z1}, {z2}, {z3}")
# Zadanie 8

lista1 = []
lista1.append(1)
lista1.append(2)
lista1.append(14)
lista1.append(26)
lista1.append(30)
lista1.append(49)

print(f"\n\nNumery lotka dodane za pomocą '.append': {lista1}")


# Zadanie 9
ilosc_schronisk = {"Warszawa": 5,
                   "Kraków": 8,
                   "Poznań": 4}


# Zadanie 10
wyniki_lotka = {"2024-09-26" : [1,2,19,29,33,41],
                "2024-09-24": [1,2,14,26,30,49],
                "2024-09-21": [4,5,12,24,36,39]}

# Zadanie 11
print("(Problem) Jakie operacje arytmetyczne są dostępne dla różnych wbudowanych struktur danych? ")

tekst = """
**Liczby całkowite (int)**

* Dodawanie: `a + b`
* Odejmowanie: `a - b`
* Mnożenie: `a * b`
* Dzielenie: `a / b` (dzielenie zmiennoprzecinkowe)
* Modulo (reszta z dzielenia): `a % b`
* Potęgowanie: `a ** b`
* Dzielenie całkowite: `a // b`

**Liczby zmiennoprzecinkowe (float)**

* Dodawanie: `a + b`
* Odejmowanie: `a - b`
* Mnożenie: `a * b`
* Dzielenie: `a / b` (dzielenie zmiennoprzecinkowe)
* Modulo (reszta z dzielenia): `a % b`
* Potęgowanie: `a ** b`
* Dzielenie całkowite: `a // b`
* Zaokrąglanie do określonej liczby miejsc dziesiętnych za pomocą funkcji `round()`

**Liczby zespolone (complex)**

* Dodawanie: `a + b`
* Odejmowanie: `a - b`
* Mnożenie: `a * b`
* Dzielenie: `a / b` (dzielenie zespolone)
* Moduł (wartość bezwzględna): `abs(a)`
* Potęgowanie: `a ** b`

**Listy**

* Slicing: `my_list[start:stop:step]`
* Indeksowanie: `my_list[index]` lub `my_list[index] = value` (przypisanie nowej wartości)
* Dodawanie elementu: `my_list.append(value)`
* Wstawianie elementu: `my_list.insert(index, value)`
* Usuwanie elementu: `my_list.remove(value)` lub `my_list.pop(index)`

**Krotki (tuples)**

* Indeksowanie: `my_tuple[index]`
* Slicing: `my_tuple[start:stop:step]` (krotki są niemodyfikowalne, więc nie można ich edytować)
* Dodawanie elementu: **niedostępne**, krotki są niemodyfikowalne

**Zbiory (sets)**

* Suma zbiorów: `a | b`
* Przecięcie zbiorów: `a & b`
* Różnica zbiorów: `a - b`
* Różnica symetryczna: `a ^ b`

**Słowniki (dictionaries)**

* Odczyt: `my_dict[key]` lub `my_dict.get(key, default_value)`
* Przypisanie nowej wartości: `my_dict[key] = value`
* Aktualizacja słownika innym słownikiem: `my_dict.update(other_dict)`

**Napisy (strings)**

* Konkatenacja (łączenie napisów): `'hello' + 'world'`
* Powielanie (powtarzanie napisu): `'hello' * 3`
* Formatowanie: `'{name} ma {age} lat.'.format(name='Jan', age=30)`
* F-strings (napisy formatowane): `f'Nazywam się {name}, i mam {age} lat.'`
* Wyodrębnianie podnapisu: `my_string[start:end]`
* Porównanie napisów:
  + Równość: `a == b`
  + Nierówność: `a != b`
  + Większy niż: `a > b`
  + Mniejszy niż: `a < b`

Napisy w Pythonie są sekwencjami znaków i wspierają wiele operacji podobnych do list. Operacje arytmetyczne na napisach nie są typowe, ale można je wykonywać na liczbach całkowitych i zmiennoprzecinkowych.
"""

print(tekst)



