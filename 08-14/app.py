from Person import Person

people = []

people.append(Person('Cecília',20,'Analista de Dados'))
people.append(Person('Luis',22,'Engenheiro de Software'))

print(people)

for i in people:
    i.greeting()
    print(i.get_name())
    print(i.get_age())
    print(i.get_profession())

print(people[0].get_name())
people[0].set_name('Ceci')
print(people[0].get_name())
people[0].greeting()