# 1) Avem 2 numere intregi. Sa se afiseze catul si restul impartirii numerelor.

a = 10
b = 2
catul_impartirii = a // b
restul_impartirii = a % b

print(catul_impartirii)
print(restul_impartirii)

# sau print(f"Catul este {a // b} si restul {a % b}")

# 2) Avem 2 numere intregi. Sa se afiseze rezultatele ridicarii la putere a celor doua numere. 

a = 10
b = 2
rezultat_ridicatputere = a ** b

print(rezultat_ridicatputere)


# 3) Avem 2 numere intregi. Sa se afiseze daca cel de al doilea numar este divizibil cu primul.

a = 10
b = 2

if b % a == 0:
    print("Al doilea numar este divizibil cu primul")
else:
    print("Al doilea numar nu este divizibil cu primul")
        
# 4) Avem un numar aleatoriu. Sa se afiseze daca numarul este par sau impar.
import random

numar = random.randint(1,100)

#numar = input("Introdu un numar pentru a determina daca este par sau impar: ")

if int(numar) % 2 == 0:
    print("Numarul introdus este par")
else:
    print("Numarul introdus este impar")


# 5) Se citeste de la tastatura un numar. Sa se verifice daca numarul se afla in intervalul 100-150.

numar = input("Introdu un numar pentru a determina daca se afla in intervalul 100-150: ")

if int(numar) >= 100 and int(numar) <= 150:
    print("Numarul se afla in intervalul 100-150")
else:
    print("Numarul introdus este in afara intervalului 100-150")


# 6) Se citeste un numar de la tastatura. Sa se verifice daca numarul este mai mic decat 50 sau mai mare decat 100.

numar = input("Introdu un numar pentru a determina daca este mai mic decat 50 sau mai mare decat 100: ")

if int(numar) < 50 or int(numar) > 100:
    print("Numarul introdus este <50 sau >100")
else:
    print("Numarul introdus NU este <50 sau >100")


# 7) Se citesc doua numere de la tastatura. Sa se determine tipul celor doua numere int/float si sa se afiseze rezultatele verificarii.

Numar_1 = input("Introdu primul numar pentru a se determina tipul sau: ")
Numar_2 = input("Introdu al doilea numar pentru a se determina tipul sau: ")

if "." in Numar_1:
    Numar_1 = float(Numar_1)
else:
    Numar_1 = int(Numar_1)

if "." in Numar_2:
    Numar_2 = float(Numar_2)
else:
    Numar_2 = int(Numar_2)


print("Primul numar este: ", type(Numar_1))
print("Al doilea numar este: ", type(Numar_2))


# 8) Se citesc doua numere de la tastatura. Sa se determine care dintre cele doua este mai mare si sa se afiseze un mesaj corespunzator.

Numar_1 = float(input("Introdu primul numar: "))
Numar_2 = float(input("Introdu al doilea numar: "))

if Numar_1 > Numar_2:
    print("Primul numar introdus este mai mare decat al doilea numar introdus.")
elif Numar_1 < Numar_2:
    print("Al doilea numar introdus este mai mare decat primul numar introdus.")
else:
    print("Numerele sunt egale.")


# 9) Se citesc doua string-uri de la tastatura. Sa se determine daca primul string se regaseste in cel de al doilea string.

String_1 = input("Introdu primul string: ")
String_2 = input("Introdu al doilea string: ")

print("Primul string se regaseste in al doilea string: ", String_1 in String_2)


# 10) Se da urmatorul string: "Ana are 10 mere si 5 pere.". Sa se extraga cuvantul "pere" din propozitie si sa se afiseze.

String = "Ana are 10 mere si 5 pere."

#print(String[20:-1]) #merge si asa dar trebuie numarate caracterele

start = String.find("pere")
stop = start + len("pere")
print(String[start:stop])
#print(start)
#print(stop)


# 11) Se citeste un sir de numere de la tastatura separate prin virgula. Se citeste un numar de la tastatura. Sa se verifice daca numarul face parte din lista.

Sir_numere = input("Introdu un sir de numere separate prin virgula: ")
Numar = input("Introdu un numar pentru a verifica daca se regaseste in sirul introdus anterior: ")

z = Sir_numere.split(",")

if Numar in z:
    print("Numarul introdus se regaseste in sirul de numere introdus initial.")
else: 
      print("Numarul introdus NU se regaseste in sirul de numere introdus initial.")


# 12) Se citesc doua numere de la tastatura. Sa se determine care dintre cele doua numere este mai mic si daca este un numar par sa se afiseze un mesaj corespunzator.

Numar_1 = int(input("Introdu primul numar: "))
Numar_2 = int(input("Introdu al doilea numar: "))

if  Numar_1 < Numar_2:
    rezultat = (Numar_1, "este mai mic decat", Numar_2) 
else: 
    rezultat = (Numar_1, "este mai mare decat", Numar_2) 

if Numar_1 % 2 == 0:
    Rezultat_ParImpar_Numar_1 = "este un numar par"
else:
    Rezultat_ParImpar_Numar_1 = "este un numar impar"

if Numar_2 % 2 == 0:
    Rezultat_ParImpar_Numar_2 = "este un numar par"
else:
    Rezultat_ParImpar_Numar_2 = "este un numar impar"

print(rezultat)
print(Numar_1, Rezultat_ParImpar_Numar_1)
print(Numar_2, Rezultat_ParImpar_Numar_2)

# 13) Se citeste un numar de la tastatura. Sa se afiseze un mesaj corespunzator in cazul in care numarul este divizibil cu 3 sau cu 5.

Numar_tastatura = input("Introdu un numar pentru a verifica daca este divizibil cu 3 sau 5: ")

if Numar_tastatura % 3 == 0 or Numar_tastatura % 5 == 0:
    print("Numarul introdus este divizibil cu 3 sau 5")
else:
    print("Numarul introdus NU este divizibil cu 3 sau 5")

# 14) Se citeste un numar de la tastatura. Sa se afiseze "fizz" daca numarul e divizibil cu 3, sa se afiseze "buzz" daca numarul este divizibil cu 5 si "fizzbuzz" daca numarul este divizibil si cu 3 si cu 5.

Numar = float(input("Introdu un numar: "))

if numar % 3 == 0 and numar % 5 == 0:
    print ("fizzbuzz")
elif numar % 3 == 0:
    print ("fizz")
elif numar % 5 == 0:
    print ("buzz")



# 15) Se da urmatorul string: "Nume: Daniel, Prenume: Neamtiu". Sa se extraga numele si prenumele din acest string si sa se afiseze de la tastatura.

String = "Nume: Daniel, Prenume: Neamtiu"

z = String.split(" ")

print(z)
print(z[1].strip(','))
print(z[3])


# 16) Se da urmatorul string: "mere, pere, mere, mere, pere, struguri". Sa se afiseze de cate ori apare cuvantul "pere" in string.

String = "mere, pere, mere, mere, pere, struguri"
Count_String = String.count("pere")

print(f"Cuvantul 'pere' apare in string de {Count_String} ori.")


# 17) Se da urmatorul string: "Ana are 10 mingi de fotbal intergalactic". Sa se stearga cuvantul intergalactic din string si sa se afiseze rezultatul.


String = "Ana are 10 mingi de fotbal intergalactic"
String_modificat = String.replace("intergalactic" , " ")

print(String_modificat)

# 18) Sa citeste de la tastatura o parola. Sa se verifice daca parola introdusa are cel putin 10 caractere si nu contine spatiu. Sa se afiseze un mesaj corespunzator pentru fiecare neregula gasita sau mesajul "OK" in cazul in care parola respecta regulile.

Password = input("Introdu parola:")
Lungime_Password = len(Password)
Spatiu_Password = Password.find(" ")

if Lungime_Password < 10 and (Spatiu_Password != -1 or Spatiu_Password >= 0):
    Mesaj = "Parola trebuie sa contina cel putin 10 caractere si sa nu contina spatii!"

elif Lungime_Password < 10 and Spatiu_Password == -1:
    Mesaj = "Parola trebuie sa contina cel putin 10 caractere!"

elif Lungime_Password > 10 and (Spatiu_Password != -1 or Spatiu_Password >= 0):
    Mesaj = "Parola nu trebuie sa contina spatii!"

else:
    Mesaj = "Ok."


print(Mesaj)
print(Lungime_Password)
print(Spatiu_Password)


# 19) Se citeste un numar intreg de la tastatura. Sa se verifice daca numarul este palindrom(ex: 123321, 12321 - are aceeasi valoarea citit si dintr-o parte si din alta) si sa se afiseze un mesaj corespunzator.

Numar = input("Introdu un numar pentru a verifica daca este palindrom: ")
Numar_inversat = Numar[::-1]

if Numar == Numar_inversat:
    print(f"Numarul introdus {Numar} este palindrom deoarece inversat are aceeasi valoare {Numar_inversat}.")
else:
       print(f"Numarul introdus {Numar} nu este palindrom deoarece inversat nu are aceeasi valoare {Numar_inversat}.")


#20)

my_string = "Sunt acasa si e bine"
start = my_string.find("acasa")
stop = len("acasa") + start

print(my_string[start:stop])