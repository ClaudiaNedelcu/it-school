
# 32) Sa se scrie un program care sa replice functionalitatea unui calculator. 
# Utilizatorul trebuie sa introduca operatia pe care doreste sa o realizeze sub forma: "10 + 5" , "11 * 3" , "10 / 2" , "12 - 10", 
# iar programul trebuie sa afiseze rezultatul operatiei. Pentru implementarea programului se va creea cate o functie pentru fiecare operatie: adunare, scadere, inmultire, impartire. 
# Executia programului va inceta in momentul in care utilizatorul introduce cuvantul "exit".


def adunare(nr1, nr2):
    rezultat = nr1 + nr2
    return rezultat

def scadere(nr1, nr2):
    rezultat = nr1 - nr2
    return rezultat

def impartire(nr1, nr2):
    rezultat = nr1 // nr2
    return rezultat

def inmultire(nr1, nr2):
    rezultat = nr1 * nr2
    return rezultat

operatie_efectuata = input("Introduceti operatia pe care doriti sa o efectuati intre 2 numere. In cazul in care doriti sa inchideti aplicatia scrieti 'exit'. : ")
operator_adunare = "+"
operator_scadere = "-"
operator_inmultire = "*"
operator_impartire = "/"


while operatie_efectuata != "exit":
    if operator_adunare in operatie_efectuata:

        index_operator = operatie_efectuata.find(operator_adunare)
        nr1 = float(operatie_efectuata[0:index_operator])
        lungime_operatie = len(operatie_efectuata)
        index_operator = index_operator + 1
        nr2 = float(operatie_efectuata[index_operator:lungime_operatie])

        rezultat = adunare(nr1, nr2)
        print(rezultat)
    
        operatie_efectuata = input("Introduceti operatia pe care doriti sa o efectuati intre 2 numere. In cazul in care doriti sa inchideti aplicatia scrieti 'exit'. : ") 
    
   

    elif operator_scadere in operatie_efectuata:

        index_operator = operatie_efectuata.find(operator_scadere)
        nr1 = float(operatie_efectuata[0:index_operator])
        lungime_operatie = len(operatie_efectuata)
        index_operator = index_operator + 1
        nr2 = float(operatie_efectuata[index_operator:lungime_operatie])

        rezultat = scadere(nr1, nr2)
        print(rezultat)

        operatie_efectuata = input("Introduceti operatia pe care doriti sa o efectuati intre 2 numere. In cazul in care doriti sa inchideti aplicatia scrieti 'exit'. : ")


    elif operator_inmultire in operatie_efectuata:

        index_operator = operatie_efectuata.find(operator_inmultire)
        nr1 = float(operatie_efectuata[0:index_operator])
        lungime_operatie = len(operatie_efectuata)
        index_operator = index_operator + 1
        nr2 = float(operatie_efectuata[index_operator:lungime_operatie])

        rezultat = inmultire(nr1, nr2)
        print(rezultat)

        operatie_efectuata = input("Introduceti operatia pe care doriti sa o efectuati intre 2 numere. In cazul in care doriti sa inchideti aplicatia scrieti 'exit'. : ")


    elif operator_impartire in operatie_efectuata:

        index_operator = operatie_efectuata.find(operator_impartire)
        nr1 = float(operatie_efectuata[0:index_operator])
        lungime_operatie = len(operatie_efectuata)
        index_operator = index_operator + 1
        nr2 = float(operatie_efectuata[index_operator:lungime_operatie])

        rezultat = impartire(nr1, nr2)
        print(rezultat)

        operatie_efectuata = input("Introduceti operatia pe care doriti sa o efectuati intre 2 numere. In cazul in care doriti sa inchideti aplicatia scrieti 'exit'. : ")