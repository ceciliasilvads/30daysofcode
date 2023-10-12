def addPeople (name: str, profession: str, age: int):
    try:
        with open('15-20/Registration of people/people.csv', 'a', encoding='UTF-8') as f:
            f.write(f'{name}, {profession}, {age}\n')
    except TypeError:
        print('Data type problem!')
    else:
        print('Added successfully!')

def registrationPeople ():
    name = input('Name: ')
    profession = input('Profession: ')
    age = input('Age: ')

    addPeople(name, profession, age)

if __name__=='__main__':
    registrationPeople()