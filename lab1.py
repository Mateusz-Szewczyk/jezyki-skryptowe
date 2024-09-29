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

# Liczby całkowite (int)
a = 10
b = 5

# Dodawanie
dodawanie = a + b

# Odejmowanie
odejmowanie = a - b

# Mnożenie
mnożenie = a * b

# Dzielenie zmiennoprzecinkowe
dzielenie_zmiennoprzecinkowe = a / b

# Modulo (reszta z dzielenia)
modulo = a % b

# Potęgowanie
potegowanie = a ** b

# Dzielenie całkowite
dzielenie_calkowite = a // b


# Liczby zmiennoprzecinkowe (float)
c = 7.5
d = 3.0

# Dodawanie
dodawanie_float = c + d

# Odejmowanie
odejmowanie_float = c - d

# Mnożenie
mnożenie_float = c * d

# Dzielenie zmiennoprzecinkowe
dzielenie_float = c / d

# Modulo (reszta z dzielenia)
modulo_float = c % d

# Potęgowanie
potegowanie_float = c ** d

# Dzielenie całkowite (dzielenie zaokrąglone w dół)
dzielenie_calkowite_float = c // d

# Zaokrąglanie do najbliższej liczby
zaokraglenie = round(c)


# Liczby zespolone (complex)
e = complex(2, 3)
f = complex(1, 1)

# Dodawanie
dodawanie_complex = e + f

# Odejmowanie
odejmowanie_complex = e - f

# Mnożenie
mnożenie_complex = e * f

# Dzielenie zespolone
dzielenie_complex = e / f

# Moduł (wartość bezwzględna liczby zespolonej)
modul_complex = abs(e)

# Potęgowanie
potegowanie_complex = e ** 2


# Listy (lists)
my_list = [1, 2, 3, 4]

# Slicing (wycinanie elementów)
slicing = my_list[1:3]

# Indeksowanie
indeksowanie = my_list[2]

# Przypisanie nowej wartości
my_list[2] = 10

# Dodawanie elementu
my_list.append(5)

# Wstawianie elementu na określone miejsce
my_list.insert(1, 9)

# Usuwanie elementu
my_list.remove(9)
element = my_list.pop(2)


# Krotki (tuples)
my_tuple = (1, 2, 3)

# Indeksowanie
indeksowanie_tuple = my_tuple[1]

# Slicing (wycinanie elementów)
slicing_tuple = my_tuple[1:3]


# Zbiory (sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Suma zbiorów
suma = set1 | set2

# Przecięcie zbiorów
przeciecie = set1 & set2

# Różnica zbiorów
roznica = set1 - set2

# Różnica symetryczna (elementy różne dla obu zbiorów)
roznica_symetryczna = set1 ^ set2


# Słowniki (dictionaries)
my_dict = {"name": "Jan", "age": 30}

# Odczyt wartości
name = my_dict["name"]

# Przypisanie nowej wartości
my_dict["age"] = 31

# Aktualizacja słownika innym słownikiem
my_dict.update({"city": "Kraków"})


# Napisy (strings)
my_string = "hello world"

# Konkatenacja (łączenie napisów)
konkatenacja = "hello" + "world"

# Powielanie (powtarzanie napisu)
powielanie = "hello" * 3

# Formatowanie
formatowanie = "{name} ma {age} lat.".format(name="Jan", age=30)

# F-strings (formatowane napisy)
fstring = f"Nazywam się {name}, i mam {my_dict['age']} lat."

# Wyodrębnianie podnapisu (slicing)
podnapis = my_string[0:5]

# Porównanie napisów
rownosc = "a" == "b"
nierownosc = "a" != "b"
wiekszy = "a" > "b"
mniejszy = "a" < "b"




