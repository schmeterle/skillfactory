import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценку
        5. Удалить предмет
        6. Удалить ученика
        7. Изменить оценку
        8. Изменить предмет
        9. Изменить ученика
        10. Посмотреть все оценки ученика
        11. Посмотреть средний балл ученика по каждому предмету
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        end_mark = int(input('Введите оценку: '))
        if end_mark in students_marks[student][class_]:
            (students_marks[student][class_]).remove(end_mark)
            print('Оценка удалена')
        else:
            print('Этой оценки нет в списке')
    elif command == 5:
        print('5. Удалить предмет')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        end_class = input('Введите предмет: ')
        if end_class in students_marks:
            del students_marks[end_class]
            print('Предмет удален')
        else:
            print('Этого предмета нет в списке')
    elif command == 6:
        print('6. Удалить ученика')
        # считываем имя ученика
        end_student = input('Введите имя ученика: ')
        if end_student in students_mark:
            del students_mark[end_student]
            print('Ученик удален')
        else:
            print('Этого ученика нет в списке')
    elif command == 7:
        print('7. Изменить оценку')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку, которую хотите изменить: '))
        new_mark = int(input('Введите новую оценку: '))
        if student in students_marks[student][class_] and class_ in students_marks[student][class_]:
            students_marks[mark] = students_marks[new_mark]
            del students_marks[mark]
            print('Оценка изменена')
        else:
            print('Этой оценки нет в списке')
    elif command == 8:
        print('8. Изменить предмет')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        old_class = input('Введите предмет, который хотите изменить: ')
        new_class = input('Введите новый предмет: ')
        if old_class in students_marks:
            students_marks[old_class] = students_marks[new_class]
            del students_marks[old_class]
            print('Предмет изменен')
        else:
            print('Этого предмета нет в списке')
    elif command == 9:
        print('9. Изменить ученика')
        # считываем имя ученика
        old_student = input('Введите имя ученика, которого хотите изменить: ')
        new_student = input('Введите новое имя: ')
        if old_student in students_marks:
            students_marks[old_student] = students_marks[new_student]
            del students_marks[old_student]
            print('Ученик изменен')
        else:
            print('Этого ученика нет в списке')
    elif command == 10:
        print('10. Посмотреть все оценки ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print('Список оценок: ')
            for class_, marks in students_marks[student].items():
                    print(f'{class_} - {marks}')
        else:
            print('Этого ученика нет в списке')
    elif command == 11:
        print('11. Вывести средний балл ученика по всем предметам')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        if student in students_marks:
            for classes,marks in students_marks[student].items():
                marks_sum = sum(marks)
                marks_count = len(marks)
                print(f'{classes} - {marks_sum//marks_count}')
        else:
            print('Этого ученика нет в списке')
    elif command == 12:
        print('4. Выход из программы')
        break
