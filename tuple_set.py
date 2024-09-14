family = ('Mom', 'Dad', 'Brother')
print(family[0])
print(family[-1])
print(family[1::2])

numbers = {1, 3, 7, 7, 5, 9}
num = int(input('Введите число: '))
if num in numbers:
    numbers.remove(num)
else:
    numbers.add(num)
print(len(numbers))
print(numbers)
