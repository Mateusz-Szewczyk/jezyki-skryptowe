# Zadanie 1

zbior1 = {1,2,3,4,5,6}
zbior2 = {3,4,5,6,7,8}


### SŁOWNIKI ###

# Zadanie 1

city_population = {"Warszawa": 4313455,
                   "Kraków": 325455,
                   "Łódź": 436346,
                   "Poznań": 243565,
                   "Wrocław": 575473}

isin = "Rzeszów" in city_population.keys()
print(isin)

city_population["Rzeszów"] = 280980

# Zadanie 2

europe_domains = {
    'ch': 'Szwajcaria',
    'cz': 'Czechy',
    'pt': 'Portugalia',
    'pl': 'Polska',
    'com': 'Komercyjny',
    'uk': 'Wielka Brytania',
    'de': 'Niemcy',
    'fr': 'Francja',
    'it': 'Włochy',
    'ru': 'Rosja'
}

asia_domains = {
    'jp': 'Japonia',
    'tw': 'Tajwan',
    'cn': 'Chiny',
    'in': 'Indie'
}

domains = {**europe_domains, **asia_domains}

print(domains)

# Zadanie 3

if "es" in domains.keys():
    print("Domena es znajduje się w słowniku")
else:
    print("Domena nie znajduje sie w slowniku")

print(domains.get("es", "brak przypisania"))


# Zadanie 4

print(domains.pop("ru"))

# Zadanie 5

print(len(domains))

# Zadanie 6

print(f"Wartosci .keys() dla słownika domains: ", domains.keys())
print(f"Wartości .values(), dla słownika domains: ", domains.values())

# Zadanie 7

shipments = {}

shipments[('Niemcy', 'USA')] = ['Bismark']

shipments[('USA', 'Polska')] = ['Błyskawica']

print("Słownik shipments po dodaniu tras:")
print(shipments)

del shipments[('Niemcy', 'USA')]

print("\nSłownik shipments po usunięciu trasy Niemcy -> USA:")
print(shipments)

# Zadanie 8
letters = dict([('A', 5), ('B', 3), ('F', 1), ('H', 1), ('Z', 6)])

print("\nSłownik letters:")
print(letters)

value_c = letters.get('C', 0)
print("\nWartość dla klucza 'C':", value_c)