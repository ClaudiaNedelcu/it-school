'''
 Cerintele pentru tema legata de fisiere:
1) Sa se afiseze toti elevii din clasele de Filologie (ClassA) care au nota peste 90 la Istorie
2) Sa se afiseze toti elevii din clasele de Mate-Info (ClassB) care au media mai mica deca 80
3) Sa se calculeze media generala a tuturor claselor de Filologie
4) Sa se afiseze clasele de de Mate-info in ordine crescatoare a mediei generale pe clasa
5) Sa se converteasca fisierele csv in care sunt salvate informatiile despre elevii de la Filologie in fisiere json.
Folderul cu fisierele se numeste "school" si il gasiti in folderul cu recordings de pe drive

'''

import os
import csv
import json

# 1)

print('Sa se afiseze toti elevii din clasele de Filologie (ClassA) care au nota peste 90 la Istorie')
print()
print('Elevii clasei 9A (Filologie) care au nota la Istorie peste 90 sunt: \n')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}9_grade.csv'

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                if int(row.get('History')) > 90:
                    print(row.get('Name'))

print()
print('Elevii clasei 10A (Filologie) care au nota la Istorie peste 90 sunt: \n')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}10_grade.csv'

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                if int(row.get('History')) > 90:
                    print(row.get('Name'))

print()
print('Elevii clasei 11A (Filologie) care au nota la Istorie peste 90 sunt: \n')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}11_grade.csv'

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                if int(row.get('History')) > 90:
                    print(row.get('Name'))


print()
print('Elevii clasei 12A (Filologie) care au nota la Istorie peste 90 sunt: \n')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}12_grade.csv'

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                if int(row.get('History')) > 90:
                    print(row.get('Name'))


# 2) 

print('---' * 30)

print('2) Sa se afiseze toti elevii din clasele de Mate-Info (ClassB) care au media mai mica deca 80')
print()
print('Elevii clasei 9B (Mate-Info) care au media sub 80 sunt: \n')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classB' in dirnames:
        file_path = f'{dirpath}{os.sep}classB{os.sep}9_grade.json'

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for data in json_data:
                medie = (data.get('grades').get('math') + data.get('grades').get('english') + data.get('grades').get('science')) / 3
                if medie < 80:
                    print(data.get('name'))


print()
print('Elevii clasei 10B (Mate-Info) care au media sub 80 sunt: \n')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classB' in dirnames:
        file_path = f'{dirpath}{os.sep}classB{os.sep}10_grade.json'

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for data in json_data:
                medie = (data.get('grades').get('math') + data.get('grades').get('english') + data.get('grades').get('science')) / 3
                if medie < 80:
                    print(data.get('name'))



print()
print('Elevii clasei 11B (Mate-Info) care au media sub 80 sunt: \n')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classB' in dirnames:
        file_path = f'{dirpath}{os.sep}classB{os.sep}11_grade.json'

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for data in json_data:
                medie = (data.get('grades').get('math') + data.get('grades').get('english') + data.get('grades').get('science')) / 3
                if medie < 80:
                    print(data.get('name'))



print()
print('Elevii clasei 12B (Mate-Info) care au media sub 80 sunt: \n')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classB' in dirnames:
        file_path = f'{dirpath}{os.sep}classB{os.sep}12_grade.json'

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for data in json_data:
                medie = (data.get('grades').get('math') + data.get('grades').get('english') + data.get('grades').get('science')) / 3
                if medie < 80:
                    print(data.get('name'))



# 3) 

print('---' * 30)
print('3) Sa se calculeze media generala a tuturor claselor de Filologie')
print()

path = 'school'
medie_clasa = 0

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}9_grade.csv'

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                medie = (int(row.get('Geography')) + int(row.get('English')) + int(row.get('History'))) / 3
                
                medie_clasa += medie
        
        medie_finala_clasa = medie_clasa / 10

        print(f'Medie generala 9A: {round(medie_finala_clasa,2)} \n')


path = 'school'
medie_clasa = 0

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}10_grade.csv'

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                medie = (int(row.get('Geography')) + int(row.get('English')) + int(row.get('History'))) / 3
                
                medie_clasa += medie
        
        medie_finala_clasa = medie_clasa / 10

        print(f'Medie generala 10A: {round(medie_finala_clasa,2)} \n')

path = 'school'
medie_clasa = 0

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}11_grade.csv'

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                medie = (int(row.get('Geography')) + int(row.get('English')) + int(row.get('History'))) / 3
                
                medie_clasa += medie
        
        medie_finala_clasa = medie_clasa / 10

        print(f'Medie generala 11A: {round(medie_finala_clasa,2)} \n')


path = 'school'
medie_clasa = 0

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}12_grade.csv'

        with open(file_path, 'r') as csv_file:
            csv_data = csv.DictReader(csv_file)

            for row in csv_data:
                medie = (int(row.get('Geography')) + int(row.get('English')) + int(row.get('History'))) / 3
                
                medie_clasa += medie
        
        medie_finala_clasa = medie_clasa / 10

        print(f'Medie generala 12A: {round(medie_finala_clasa,2)} \n')


# 4) 

print('---' * 30)
print('4) Sa se afiseze clasele de de Mate-info in ordine crescatoare a mediei generale pe clasa')
print()

dictionar_medii = {
    'Clasa 9B' : 0,
    'Clasa 10B' : 0,
    'Clasa 11B' : 0,
    'Clasa 12B' : 0,
}

path = 'school'
medie_clasa = 0

for dirpath, dirnames, filenames in os.walk(path):
    if 'classB' in dirnames:
        file_path = f'{dirpath}{os.sep}classB{os.sep}9_grade.json'

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for data in json_data:
                medie = (data.get('grades').get('math') + data.get('grades').get('english') + data.get('grades').get('science')) / 3
                
                medie_clasa += medie
        
        medie_finala_clasa = round(medie_clasa / 10 , 2)
        dictionar_medii['Clasa 9B'] = medie_finala_clasa

path = 'school'
medie_clasa = 0

for dirpath, dirnames, filenames in os.walk(path):
    if 'classB' in dirnames:
        file_path = f'{dirpath}{os.sep}classB{os.sep}10_grade.json'

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for data in json_data:
                medie = (data.get('grades').get('math') + data.get('grades').get('english') + data.get('grades').get('science')) / 3
                
                medie_clasa += medie
        
        medie_finala_clasa = round(medie_clasa / 10 , 2)
        dictionar_medii['Clasa 10B'] = medie_finala_clasa


path = 'school'
medie_clasa = 0

for dirpath, dirnames, filenames in os.walk(path):
    if 'classB' in dirnames:
        file_path = f'{dirpath}{os.sep}classB{os.sep}11_grade.json'

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for data in json_data:
                medie = (data.get('grades').get('math') + data.get('grades').get('english') + data.get('grades').get('science')) / 3
                
                medie_clasa += medie
        
        medie_finala_clasa = round(medie_clasa / 10 , 2)
        dictionar_medii['Clasa 11B'] = medie_finala_clasa

path = 'school'
medie_clasa = 0

for dirpath, dirnames, filenames in os.walk(path):
    if 'classB' in dirnames:
        file_path = f'{dirpath}{os.sep}classB{os.sep}12_grade.json'

        with open(file_path, 'r') as json_file:
            json_data = json.load(json_file)

            for data in json_data:
                medie = (data.get('grades').get('math') + data.get('grades').get('english') + data.get('grades').get('science')) / 3
                
                medie_clasa += medie
        
        medie_finala_clasa = round(medie_clasa / 10 , 2)
        dictionar_medii['Clasa 12B'] = medie_finala_clasa

sortare_dictionar = dict(sorted(dictionar_medii.items(), key = lambda item : item[1]))
print(sortare_dictionar)

# 5)

print('---' * 30)
print('5) Sa se converteasca fisierele csv in care sunt salvate informatiile despre elevii de la Filologie in fisiere json.')
print('Verifica existenta fisierelor convertite in folder.')

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}9_grade.csv'

        with open(file_path, 'r') as csv_file:
            list_data = []
            data = csv.DictReader(csv_file)
        
            for item in data:
                list_data.append(item)

        file_path_json_nou = f'{dirpath}{os.sep}classA{os.sep}9_grade_convert.json'
        with open(file_path_json_nou, 'w') as json_file:
            json.dump(list_data, json_file, indent = 4)


path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}10_grade.csv'

        with open(file_path, 'r') as csv_file:
            list_data = []
            data = csv.DictReader(csv_file)
        
            for item in data:
                list_data.append(item)

        file_path_json_nou = f'{dirpath}{os.sep}classA{os.sep}10_grade_convert.json'
        with open(file_path_json_nou, 'w') as json_file:
            json.dump(list_data, json_file, indent = 4)  
        

path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}11_grade.csv'

        with open(file_path, 'r') as csv_file:
            list_data = []
            data = csv.DictReader(csv_file)
        
            for item in data:
                list_data.append(item)

        file_path_json_nou = f'{dirpath}{os.sep}classA{os.sep}11_grade_convert.json'
        with open(file_path_json_nou, 'w') as json_file:
            json.dump(list_data, json_file, indent = 4)


path = 'school'

for dirpath, dirnames, filenames in os.walk(path):
    if 'classA' in dirnames:
        file_path = f'{dirpath}{os.sep}classA{os.sep}12_grade.csv'

        with open(file_path, 'r') as csv_file:
            list_data = []
            data = csv.DictReader(csv_file)
        
            for item in data:
                list_data.append(item)

        file_path_json_nou = f'{dirpath}{os.sep}classA{os.sep}12_grade_convert.json'
        with open(file_path_json_nou, 'w') as json_file:
            json.dump(list_data, json_file, indent = 4)