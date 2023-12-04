Russia = ['Морозовск', 'Москва', 'Ростов-на-Дону']
Spain = ['Барселона', 'Мадрид', 'Валенсия']
China = ['Шанхай', 'Пекин', 'Чунцин']

print(Russia)
print(Spain)
print(China)

town = input('Введите название города: ')

for i in Russia:
    if i == town:
        print('Россия')

for i in Spain:
    if i == town:
        print('Испания')

for i in China:
    if i == town:
        print('Китай')
    else:
        print()
    

    
        
