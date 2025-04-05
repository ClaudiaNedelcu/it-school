"""
CERINTA 
Sa se scrie un program care tine evidenta angajatilor dintr-o companie.
Informatiile pe care trebuie sa le retinem despre un angajat sunt urmatoarele:
    1) CNP
    2) Nume
    3) Prenume
    4) Varsta
    5) Salar
    6) Departament
    7) Senioritate (junior, mid, senior)

Programul trebuie sa dispuna de un meniu care ne permite sa efectuam urmatoarele actiuni:
    1) Adaugare angajat
    2) Cautare angajat (dupa CNP)
    3) Modificare date angajat (dupa CNP)
    4) Stergere angajat
    5) Afisare angajati
    6) Calculator cost total salarii
    7) Calculator cost total salarii departament
    8) Calculator fluturas salar angajat (CAS - 10% din brut, CASS - 25% din brut, Impozit - 10% din ce a ramas)
    9) Afisarea angajatilor (dupa senioritate)
    10) Afisarea angajatilor (dupa departament)
    11) Iesire

Criterii notare:
    
Lizibilitate cod
Documentatie cod
Denumire variabile
Functionalitate
Verificare integriatate date (parametrii introdusi sa fie corespunzatori)
  ○ Exemplu: 
CNP sa fie de lungime corespunzatoare si sa contina doar cifre
Varsta sa fie mai mare de 18 ani
Salarul sa fie mai mare decat minimul (4050)
etc

"""


'''
--- DOCUMENTATIE PROIECT - EVIDENTA ANGAJATI ---

Aceasta aplicatie cuprinde cuprinde o mini baza de date cu anagajatii unei companii.
In cadrul aplicatiei diferite actiuni pot fi realizate prin intermediul meniului:

  1. Adaugare angajat
    2. Cautare angajat (dupa CNP)
    3. Modificare date angajat (dupa CNP)
    4. Stergere angajat
    5. Afisare angajati
    6. Calculator cost total salarii
    7. Calculator cost total salarii departament
    8. Calculator fluturas salariu angajat 
    9. Afisarea angajatilor (dupa senioritate)
    10. Afisarea angajatilor (dupa departament)
    11. Iesire

Baza de date este locala, cuprinsa in fisierul python si se reseteaza de fiecare data cand porneste aplicatia.

'''
__version__ = 1.0
__author__ = 'Claudia Nedelcu'

# Prima oara imi creez o mica baza de date initiala cu cativa angajati. Creez cate un dictionar ptr fiecare angajat si ii adaug intr-o lista.

Lista_angajati = [] # lista angajati
Angajat1 = {'CNP': 2970718440051, 'Nume': 'Nedelcu', 'Prenume': 'Claudia', 'Varsta': 27, 'Salariu': 90000, 'Departament': 'It', 'Senioritate': 'Junior'}
Angajat2 = {'CNP': 1910502440052, 'Nume': 'Popescu', 'Prenume': 'Ionel', 'Varsta': 34, 'Salariu': 120000, 'Departament': 'Financiar', 'Senioritate': 'Mid'}
Angajat3 = {'CNP': 1830623440053, 'Nume': 'Trandafir', 'Prenume': 'Georgeta', 'Varsta': 42, 'Salariu': 180000, 'Departament': 'Hr', 'Senioritate': 'Senior'}
Angajat4 = {'CNP': 2880623440053, 'Nume': 'Paraschiv', 'Prenume': 'Ioana', 'Varsta': 37, 'Salariu': 130000, 'Departament': 'Hr', 'Senioritate': 'Mid'}

Lista_angajati.append(Angajat1)
Lista_angajati.append(Angajat2)
Lista_angajati.append(Angajat3)
Lista_angajati.append(Angajat4)

# Incep sa imi definesc functiile ptr optiunile meniului

def Functie_Sortare_dupa_Senioritate(dictionar):
    return dictionar['Senioritate']

def Functie_Sortare_dupa_Departament(dictionar):
    return dictionar['Departament']

'''
Definesc functie Citire_Date_Angajat() prin care citesc urmatoarele informatii de la tastatura:

- CNP angajat
- Nume si Prenume angajat
- Varsta
- Salariu
- Departament

De asemenea, validez informatiile introduse pentru a minimiza % datelor incorecte:
- CNP-ul trebuie sa fie unic, format doar din 13 cifre
- Varsta trebuie sa fie cuprinsa intr 18 si 65 ani
- Salariul trebuie sa fie minim 4050 lei

In cazul nerespectarii acestor cerinte, un mesaj de eroare specific fiecarui scenariu va fi afisat pentru a indruma userul.

'''

def Citire_Date_Angajat():
        
        Date_Angajat = {}

        while True:
            Date_Angajat['CNP'] = input('Introduceti CNP-ul angajatului: ').strip()
            lungime_cnp = len(Date_Angajat['CNP'])
            Verificare_cifre = Date_Angajat['CNP'].isdigit()
                
            if Verificare_cifre == True:
                if Lista_angajati and any(Angajat.get('CNP') == int(Date_Angajat['CNP']) for Angajat in Lista_angajati):
                    print("\n CNP deja existent! Introduceti un CNP unic.\n")
                    continue
            
            if lungime_cnp == 13 and Verificare_cifre == True:
                break
                
            elif lungime_cnp != 13 and Verificare_cifre == True:
                print()
                print('CNP invalid!')
                print(f'CNP-ul introdus are {lungime_cnp} cifre, in loc de 13 cifre.\n')
                    
            elif lungime_cnp == 13 and Verificare_cifre == False:
                print()
                print('CNP invalid!')
                print('CNP-ul introdus trebuie sa contina doar cifre! \n')
                
            elif lungime_cnp != 13 and Verificare_cifre == False:
                print()
                print('CNP invalid!')
                print('CNP-ul introdus contine litere! Trebuie sa contina doar 13 cifre! \n')
                    

        Date_Angajat['Nume'] = input('Introduceti numele angajatului: ').strip().capitalize()
        Date_Angajat['Prenume'] = input('Introduceti prenumele angajatului: ').strip().capitalize()
            

        while True:
                    Date_Angajat['Varsta'] = int(input('Introduceti varsta angajatului: '))
                    varsta_introdusa = Date_Angajat['Varsta']
                    if varsta_introdusa < 18 or varsta_introdusa > 65:
                        print('Angajatul nu poate fi adaugat deoarece nu are varsta legala pentru a lucra!')
                        
                
                    else:
                        break  

        
        while True:
                    Date_Angajat['Salariu'] = int(input('Introduceti salariul angajatului: '))
                    salariu_introdus = Date_Angajat['Salariu']
                    if salariu_introdus < 4050:
                        print('Salariul introdus trebuie sa fie cel putin egal cu salariul minim (4050 lei)!')
                        
                    
                    else:
                        break
        
        Date_Angajat['Departament'] = input('Introduceti departamentul angajatului: ').strip().capitalize()
        Date_Angajat['Senioritate'] = input('Introduceti senioritatea angajatului: ').strip().capitalize()
    

        return Date_Angajat

'''
Functia Adaugare_Angajat ia datele verificate anterior prin functia Citire_Date_Angajat si creeaza un nou dictionar ce va fi adaugat in Lista_Angajati.
Pentru a nu avea date duplicate, inainte de a realiza dictionarul verifica daca CNP-ul exista in vreun dictionar(angajat) deja existent in Lista_Angajati.
'''
def Adaugare_Angajat(Date_Angajat):
    exista = False
    for Angajat in Lista_angajati:
        if Angajat.get('CNP') == Date_Angajat.get('CNP'):
            print('ERROR: Angajatul se afla deja in evidenta!')
            print('INFO: Va rugam folositi optiunea: 3) Modificare date angajat.')
            exista = True
            break

    if not exista:
        Lista_angajati.append(Date_Angajat)
        print(f'Angajatul a fost adaugat cu succes!')

'''
Functia Afisare_Angajat arata datele existente ale angajatilor din Lista_Angajati. Formatul afisate este de tipul {key}:{value}.
'''
def Afisare_Angajati():
    for Angajat in Lista_angajati:
        print()
        for key, value in Angajat.items():
            print(f'{key}: {value}')

'''
Functia Cautare_Angajat_CNP cauta in Lista_Angajati cnp-ul introdus de la tastatura. In cazul in care este gasit, se afiseaza datele acelui cnp.
'''

def Cautare_Angajat_CNP():
    CNP = int(input('Introduceti CNP-ul angajatului pe care doriti sa il cautati: '))

    exista = False
    for Angajat in Lista_angajati:
        if Angajat.get('CNP') == CNP:
            print()
            for key, value in Angajat.items():
                print(f'{key}: {value}')

            exista = True
            break

    if not exista:
        print('CNP-ul introdus nu exista in evidenta!')

'''
Functia Stergere_Angajat cauta in Lista_Angajati cnp-ul introdus de la tastatura. In cazul in care este gasit, sterge acel dictionar din Lista_Angajati.
'''

def Stergere_Angajat():
    CNP = int(input('Introduceti CNP-ul angajatului pe care doriti sa il stergeti: '))

    exista = False
    for index, Angajat in enumerate(Lista_angajati):
        if Angajat.get('CNP') == CNP:
            Lista_angajati.remove(Angajat)
            print('INFO: Angajatul a fost sters cu succes!')
            exista = True
            break

    if not exista:
        print('CNP-ul introdus nu exista in evidenta!')

'''
Functia Afisare_Angajati_Departament cauta in Lista_Angajati dictionarele care contin acelasi departament ca cel introdus de la tastatura si afiseaza rezultatele.
'''

def Afisare_Angajati_Departament():
    Departament = input('Introduceti departamentul (IT, HR, Financiar): ')
    for Angajat in Lista_angajati:
        if Angajat.get('Departament') == Departament:
            print()
            for key, value in Angajat.items():
                print(f'{key}: {value}')

'''
Functia Afisare_Angajati_Senioritate cauta in Lista_Angajati dictionarele care contin aceeasi senioritate ca cea introdusa de la tastatura si afiseaza rezultatele.
'''

def Afisare_Angajati_Senioritate():
    Senioritate = input('Introduceti senioritatea (Junior, Mid, Senior): ')
    Senioritate = Senioritate.capitalize()
    for Angajat in Lista_angajati:
        if Angajat.get('Senioritate') == Senioritate:
            print()
            for key, value in Angajat.items():
                print(f'{key}: {value}')

'''
Functia Modificare_Angajat cauta in Lista_Angajati dupa cnp-ul introdus de la tastatura si reintroduce datele pentru acesta.
'''

def Modificare_Angajat():

    print('Introduceti noile date ale angajatului:')
    Date_Angajat = Citire_Date_Angajat()

    exista = False
    for Angajat in Lista_angajati:
        if Angajat.get('CNP') == Date_Angajat.get('CNP'):
            Index_Angajat = Lista_angajati.index(Angajat)
            Lista_angajati[Index_Angajat] = Date_Angajat
            print('INFO: Datele angajatului au fost modificate cu succes!')
            exista = True
            break

    if not exista:
        print('CNP-ul pe care doriti sa-l modificati nu exista in evidenta!')

'''
Functia Calculator_Salarii_Total aduna toate valorile salariilor brute introduse in campul 'Salariu' al fiecarui dictionar (angajat) din Lista_Angajati.
'''

def Calculator_Salarii_Total():
    suma_salarii = 0
    for Angajat in Lista_angajati:
        suma_salarii += Angajat.get('Salariu')

    print(f'Total salarii angajati = {suma_salarii} lei brut.') 

'''
Functia Calculator_Salarii_Departament aduna valorile salariilor brute introduse in campul 'Salariu' al fiecarui dictionar (angajat) din Lista_Angajati in functie de departamente.
Se afiseaza totalul per departament.
'''

def Calculator_Salarii_Departament():
    suma_salarii_it = 0
    suma_salarii_hr = 0
    suma_salarii_financiar = 0
    for Angajat in Lista_angajati:
        if Angajat.get('Departament') == 'It':
            suma_salarii_it += Angajat.get('Salariu')
        elif Angajat.get('Departament') == 'Hr':
            suma_salarii_hr += Angajat.get('Salariu')
        elif Angajat.get('Departament') == 'Financiar':
            suma_salarii_financiar += Angajat.get('Salariu')     

    print(f'Total salarii angajati in functie de departament: \n')
    print(f'Total salarii IT = {suma_salarii_it}')
    print(f'Total salarii HR = {suma_salarii_hr}')
    print(f'Total salarii Financiar = {suma_salarii_financiar}')   

'''
Functia Calculator_Fluturas_Salariu_Angajat calculeaza si afiseaza urmatoarele valori ptr un cnp introdus de la tastatura: CAS, CASS, Impozit, Salariu Net.
'''

def Calculator_Fluturas_Salariu_Angajat():
    valoare_cas = 0
    valoare_cass = 0
    valoare_impozit = 0
    salariu_net = 0
    CNP = int(input('Introduceti CNP-ul angajatului pe care doriti sa il cautati: '))

    exista = False
    for Angajat in Lista_angajati:
        if Angajat.get('CNP') == CNP:
            valoare_cas = 0.10*Angajat.get('Salariu')
            valoare_cass = 0.25*Angajat.get('Salariu')
            suma_impozabila = Angajat.get('Salariu') - valoare_cas - valoare_cass
            valoare_impozit = 0.10*suma_impozabila
            salariu_net = suma_impozabila - valoare_impozit
            nume_Angajat = Angajat.get('Nume')
            preume_Angajat = Angajat.get('Prenume')
            salariu_brut = Angajat.get('Salariu')
        
            print()
            print(f'\n --- Fluturas salariu - {nume_Angajat} {preume_Angajat} ---\n')
            print(f'Salariu brut = {salariu_brut} lei')
            print(f'Salariu net = {salariu_net} lei')
            print(f'CAS (10%) = {valoare_cas} lei')
            print(f'CASS (25%) = {valoare_cass} lei')
            print(f'Impozit (10%) = {valoare_impozit} lei')
        
            exista = True
            break

    if not exista:
        print('CNP-ul introdus nu exista in evidenta!')


while True:
    Meniu = '''\n --- MENIU ---\n
    1. Adaugare angajat
    2. Cautare angajat (dupa CNP)
    3. Modificare date angajat (dupa CNP)
    4. Stergere angajat
    5. Afisare angajati
    6. Calculator cost total salarii
    7. Calculator cost total salarii departament
    8. Calculator fluturas salariu angajat 
    9. Afisarea angajatilor (dupa senioritate)
    10. Afisarea angajatilor (dupa departament)
    11. Iesire
    '''

    continuare_program = input('\n Apasati "ENTER" pentru vedea meniul principal.\n')

    if continuare_program == '':
        print(Meniu)
        optiune = input('Introduceti optiunea dorita:')
    else:
        continue

    if optiune == '1':
        Date_Angajat = Citire_Date_Angajat()
        Adaugare_Angajat(Date_Angajat)
    elif optiune == '2':
        Cautare_Angajat_CNP()
    elif optiune == '3':
        Modificare_Angajat()
    elif optiune == '4':
        Stergere_Angajat()
    elif optiune == '5':
        Afisare_Angajati()
    elif optiune == '6':
        Calculator_Salarii_Total()
    elif optiune == '7':
        Calculator_Salarii_Departament()
    elif optiune == '8':
        Calculator_Fluturas_Salariu_Angajat()
    elif optiune == '9':
        Afisare_Angajati_Senioritate()
    elif optiune == '10':
        Afisare_Angajati_Departament()
    elif optiune == '11':
        print('Aplicatia se va inchide. Goodbye!')
        break
    else:
        print('Optiunea introdusa nu se afla in meniu!')


