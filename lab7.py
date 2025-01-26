# zadanie 1 generatory

import string

def alphabet_generator():
    for letter in string.ascii_lowercase:
        yield letter

gen = alphabet_generator()
print(next(gen))
print(next(gen))
print(next(gen))

for letter in alphabet_generator():
    print(letter, end=" ")

# zadanie 2 generatory
import random

def alphanum_generator():
    chars = string.ascii_letters + string.digits
    while True:
        yield random.choice(chars)

gen = alphanum_generator()
print('\n')

for _ in range(5):
    print(next(gen), end=" ")

print('\n')


# zadanie 3 generatory

def password_generator(length):
    random.seed(42)
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        yield random.choice(chars)

password_length = int(input("Podaj długość hasła: "))

password_gen = password_generator(password_length)
password = ''.join(password_gen)
print(f"Wygenerowane hasło: {password}")

# zadanie 4 wyraqzania listowe
list1 = [x for x in range(20) if x % 3 == 0]

list2 = [x for x in range(20) if x % 2 != 0]

print("Liczby podzielne przez 3:", list1)
print("Liczby nieparzyste:", list2)

# zadanie 5 wyrażenia listowe

matrix = [[x + y * 4 for x in range(4)] for y in range(4)]

for row in matrix:
    print(row)

# zadanie 6 wyrażenia listowe

powered_matrix = [[element**2 for element in row] for row in matrix]

for row in powered_matrix:
    print(row)

# zadanie 7 wyrażenia listowe

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


non_primes = [x for x in range(1, 101) if not is_prime(x)]

print("Liczby niebędące liczbami pierwszymi:", non_primes)

# zadanie 8 wyrażenia listowe

names = input("Podaj listę imion, oddzielając je przecinkami: ").split(",")
letters = input("Podaj listę liter, oddzielając je przecinkami: ").split(",")

# Filtracja imion na podstawie liter
filtered_names = [name for name in names if all(letter in name for letter in letters)]

print("Imiona spełniające kryteria:", filtered_names)

#----------------------------------------------#

# Zadania z ostatniej listy

# 1. Wyświetl liczby podzielne przez 2
liczby = [100, 95, 80, 75, 60, 55, 40, 35, 20, 15, 0]
divisible_by_2 = [x for x in liczby if x % 2 == 0]
print(divisible_by_2)

# 2. Sprawdź, czy osoba jest pełnoletnia
is_adult = lambda age: age >= 18
print(is_adult(20))
print(is_adult(15))

# 3. Posortuj listę miast po ilości znaków
cities = ["Warsaw", "Paris", "Berlin", "Tokyo"]
sorted_cities = sorted(cities, key=len)
print(sorted_cities)

# 4. Posortuj mapę gazy po wartościach
gazy = {'hel': 1, 'neon': 2, 'argon': 6, 'ksenon': 8}
sorted_gazy = dict(sorted(gazy.items(), key=lambda item: item[1]))
print(sorted_gazy)

# 5. Sprawdź, czy wszystkie liczby są typu zmiennoprzecinkowego
liczby = [1.5, 5.1, 6.3, 2.2, 8.4]
all_floats = all(isinstance(x, float) for x in liczby)
print(all_floats)

# 6. Znajdź część wspólną dwóch list
l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
intersection = [x for x in l1 if x in l2]
print(intersection)

# 7. Znajdź tylko stringi, które są anagramami
input_strings = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
anagrams = [word for word in input_strings if sorted(word) == sorted('abcd')]
print(anagrams)

# 8. Zamień listę liczb całkowitych na stringi
lista = [1, 2, 3, 4]
string_list = [str(x) for x in lista]
print(string_list)

# 9. Dodaj do siebie trzy list
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]
combined_list = l1 + l2 + l3
print(combined_list)




