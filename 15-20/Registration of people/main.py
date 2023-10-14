import csv

path = '15-20/Registration of people/people.csv'

def uiLine():
    return print('-------------------------------------------')

def showPeople():
    data_csv = []

    with open(path, 'r', encoding='UTF-8') as f:
        reader_csv = csv.reader(f)
        
        for i in reader_csv:
            data_csv.append(i)
        
        uiLine()
        for j in data_csv:
            print(f"{j[0]:<15} {j[1]:<20} {j[2]:<3}")

def addPeople (name: str, profession: str, age: int):
    try:
        with open(path, 'a', encoding='UTF-8') as f:
            f.write(f'{name}, {profession}, {age}\n')
    except TypeError:
        print('Data type problem!')
    else:
        print('Added successfully!')
    finally:
        showPeople()

def registrationPeople ():
    name = input('Name: ')
    profession = input('Profession: ')
    age = input('Age: ')

    addPeople(name, profession, age)

if __name__=='__main__':
    registrationPeople()