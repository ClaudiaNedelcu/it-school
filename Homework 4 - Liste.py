# 33) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]. Sa se extraga numele "Ionut" din lista si sa se afiseze.

lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"] , [10.2, 7.5, 3.4]]

Nume_extras = lista[1][1]

print(Nume_extras)


# 34) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]

litera_extrasa = lista[1][2][2]

print(litera_extrasa)

# 35) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]. Sa se afiseze toate numerele de tip float din lista.

lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]




# 36) Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]. Scrieti un program care citeste un nume de la tastatura si verifica daca numele se afla in lista.

lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]

Nume_de_verificat = input("Introduceti un nume pentru a verifica daca exista in lista: ")

Nume_de_verificat = Nume_de_verificat.capitalize()

if Nume_de_verificat in lista[1]:
    print(f"Numele {Nume_de_verificat} exista in lista.")

else:
    print(f"Numele {Nume_de_verificat} nu exista in lista.")


# 37) Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. Sa se afiseze numerele pare din lista.

lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]

lista_numere_pare = []
index = 0 
for numar in lista:
    if numar % 2 == 0:
        lista_numere_pare = lista_numere_pare.append[index]
        index += 1
        print(lista_numere_pare)
    else:
        continue



# 38) Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. Sa se afiseze cel mai mic numar si cel mai mare numar din lista.

lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]



# 39) Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. Sa se scrie o functie care primeste ca parametru lista si un numar. 
# Functia trebuie sa afiseze toate numerele din lista care sunt divizibile cu numarul dat. Numarul dat este introdus de la tastatura de catre utilizatorul programului.

lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]

numar = input("Introduceti un numar pentru a verifica daca este divizibil: ")

lista_nr_divizibile = []

def dizibilitate(lista, numar):
    rezultat = lista % numar
    if rezultat == 0:
        lista_nr_divizibile.append()

    return rezultat




# 40) Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. Sa se scrie o functie care primeste ca parametru lista si afiseaza suma numerelor impare din lista.



# 41) Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. Sa se scrie o functie care primeste ca parametru lista si un numar. 
# Functia trebuie sa afiseaza indexul numarului daca acesta se afla in lista sau "Not Found" in caz contrar.


