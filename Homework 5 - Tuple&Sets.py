# 42) Sa se creeze un tuple cu 5 elemente diferite si sa se afiseze al doilea si ultimul element.

tuplu = (1, [1,2], "Ana", 20.5, "mere")

print(tuplu[1])
print(tuplu[-1])

# 43) Sa se creeze 2 tuple cu cate 3 elemente fiecare. Sa se concateneze cele doua si sa se afiseze noul tuple rezultat in urma operatiei.

tuplu1 = (1, 2, 3)
tuplu2 = ("Ana", "Maria", "Ioana")

tuplu_concatenat = tuplu1 + tuplu2

print(tuplu_concatenat)

# 44) Sa se creeze un tuplu cu 10 elemente. Sa se citeasca de la tastatura un element si sa se verifice daca elementul se afla in tuplul creat.

tuplu = (1, "masina", 100.53, "muzica", 4, 9, 103, "floare", 10, 45)

element = input("Introduceti un element pentru a verifica daca se regaseste in tuplu: ")

if element in tuplu:
    print(f"Elementul {element} se regaseste in tuplu.")
else:
    print(f"Elementul {element} nu se regaseste in tuplu.")

# 45) Sa se creeze un tuple cu 5 elemente. Sa se citeasca un element de la tastatura si sa se afiseze indexul elementului in acel tuple. 
# In caz ca nu se regaseste in tuple, sa se afiseze "not found".

tuplu = (1, 2, 3, 4, "masina")

element = input("Introduceti un element pentru a verifica daca se regaseste in tuplu: ")

if element in tuplu:
    print(f"Elementul {element} se regaseste in tuplu la indexul {tuplu[element]} .")
else:
    print(f"Elementul {element} nu se regaseste in tuplu. Not found.")

# 46) Sa se creeze un tuplu cu 10 elemente. Sa se extraga un subtuplu din el pornind de la pozitia 2 pana la pozitia 5 si sa se afiseze.


# 47) Se da o lista [1,1,2,2,2,3,4,5,5,5,5,6,7,8,9,9,9]. Sa se stearga elementele duplicate si sa se afiseze rezultatul.

lista = [1,1,2,2,2,3,4,5,5,5,5,6,7,8,9,9,9]

tuplu = (lista)

print(tuplu)

# 48)Se dau doua seturi: {1,2,3,4,5,6} si {4,5,6,7,8,9}. Sa se afiseze elementele care se afla in ambele seturi.

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

