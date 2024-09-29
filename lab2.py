# Zadanie 1

l1 = [1,23,4,5,6,7,78]
l2 = l1.copy()

# Zadanie 2

print(id(l1))
print(id(l2))

# Zadanie 3

print(len(l1))

# Zadanie 4

panstwa = [
    "Albania",
    "Andora",
    "Argentyna",
    "Australia",
    "Austria",
    "Belgia",
    "Białoruś",
    "Brazylia",
    "Bułgaria",
    "Chile"
]

print(panstwa[::-1])

# Zadanie 5

print(panstwa[-3:])

# Zadanie 6

print(panstwa[::2])

# Zadanie 7
print(l2)
del l2[::2]

print(l2)

# Zadanie 8

oceny = [3.5, 4, 5, 4.5, 5, 3, 5, 4]
print("Lista ocen przed sortowaniem: ", oceny)

sorted_oceny = sorted(oceny)
suma_ocen = sum(oceny)
print("Lista ocen po sortowaniu: ", sorted_oceny)
print("Średnia ocen przed zmianą oceny: ", suma_ocen/len(oceny))

sorted_oceny[0] += 1
suma_ocen = sum(sorted_oceny)
print("Lista ocen po zmianie oceny: ", sorted_oceny)
print("Średnia ocen po zmianie oceny: ", suma_ocen/len(oceny))

# Zadanie 9

kolory = ["zielony", "limonkowy", "czarny", "lawendowy", "brązowy"]
try:
    kolory.index("fioletowy")
    print("Kolor fioletowy znajduje się w liście")
except ValueError:
    print("Kolor fioletowy nie znajduje się w liście")

# Zadanie 10

lista = [True, True, False]
print(any(lista))
print(all(lista))

# Zadanie 11

lista_kolorow = ['biały', 'niebieski', 'zielony', 'żółty']
lista_kolorow.extend(['czerwony', 'fioletowy'])
print(lista_kolorow)

# Zadanie 12

lista_kolorow1 = ['biały', 'niebieski', 'zielony', 'żółty']

for kolor in ['czerwony', 'fioletowy']:
    lista_kolorow1.append(kolor)
print(lista_kolorow1)

# Zadanie 13
lista_kolorow.sort()
print(lista_kolorow)

# Zadanie 14

lista_kolorow[len(lista_kolorow)//2 - 1] = "seledynowy"
lista_kolorow[len(lista_kolorow)//2] = "czarny"
print(lista_kolorow)

# Zadanie 15

print("Kolor zielony znajduje się na indeksie: ", lista_kolorow.index("zielony"))

# Zadanie 16

if "pomaranczowy" not in lista_kolorow:
    lista_kolorow.insert(0, "pomaranczowy")

if "szary" not in lista_kolorow:
    lista_kolorow.insert(len(lista_kolorow), "szary")

print(lista_kolorow)

# Zadanie 17

l5 = [1,2,3,4,5,6]
l6 = [4,6,8,1,3,5]

krotka = (l5, l6)

l5.append(7)

list(krotka)[0] += (8,6)

print("Lista l5 po modyfikacji:", l5)
print("Lista l6 po modyfikacji:", l6)
print("Krotka po modyfikacji:", krotka)

# Zadanie 18
# FIFO (First In, First Out)
fifo_queue = []
fifo_queue.append('Element 1')
fifo_queue.append('Element 2')
fifo_queue.append('Element 3')

print("Kolejka FIFO:", fifo_queue)
print("Usunięto:", fifo_queue.pop(0))
print("Kolejka FIFO:", fifo_queue)
print("Usunięto:", fifo_queue.pop(0))
print("Kolejka FIFO:", fifo_queue)

# LIFO (Last In, First Out)
lifo_stack = []
lifo_stack.append('Element 1')
lifo_stack.append('Element 2')
lifo_stack.append('Element 3')

print("\nStos LIFO:", lifo_stack)
print("Usunięto:", lifo_stack.pop())
print("Stos LIFO:", lifo_stack)
print("Usunięto:", lifo_stack.pop())
print("Stos LIFO:", lifo_stack)

