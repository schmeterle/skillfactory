coworkers = ['Иван', 'Катя', 'Саша', 'Юля', 'Витя']
print(coworkers[0])
print(coworkers[-1])
print(coworkers[::2])
print(coworkers[1::2])
print(len(coworkers))

new_coworcker = input('Введите имя: ')
coworkers.append(new_coworcker)
print(len(coworkers))

coworcker = input('Введите имя: ')
if coworcker in coworkers:
    print('Имя есть в списке')
else:
    print('Имени нет в списке')
