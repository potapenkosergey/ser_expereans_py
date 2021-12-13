# TODO Кортеж, семь учащихся ВУЗов.
# Загрузка модуля collections
from collections import namedtuple

# Создание объекта namedtuple с четырмя полями:
Student = namedtuple('Student', 'name age mark city')
students = (
    Student('Иван', '18', 7.1, 'Киев'),
    Student('Светлана', '20', 8.2, 'Киев'),
    Student('Дмитрий', '19', 5.1, 'Фастов'),
    Student('Николай', '18', 7.0, 'Одесса'),
    Student('Стас', '18', 6.7, 'Киев'),
    Student('Илона', '20', 9.9, 'Жмерынка'),
    Student('Надя', '21', 8.6, 'Маякы')
)


# Определение средней отметки за семестр:
def good_students(students1):
    total_mark = 0

    for student in students1:
        total_mark += student.mark
    avg_mark = total_mark / len(students1)

    good_mark_students = [student.name for student in students1 if
                          student.mark >= avg_mark]
    print('Ученики:', ', '.join(good_mark_students),
          ' в этом семестре хорошо учатся!')


good_students(students)
