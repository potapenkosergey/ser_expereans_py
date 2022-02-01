# TODO Итоговая работа, записная книжка.
"""Вызов данной программы осуществляеться:
    * start_book()"""


class Notebook:
    """"Класс Notebook - Записывает данные введённые пользователем и имеет
    множество методов.
    Имеет методы:
        * Добавляет данные человека
        * Удаляет запись в списке
        * Метод изменяет запись
        * Поиск данных в записи
        * сортирует по имени и по фамилии
        * Закрытие программы с сохранением в фаил
        * Проверка на существования фаила
        * Выдаёт список всех записей
        * Пронумерованная каждая запись в журнале"""

    def __init__(self):
        self.jotter = {}
        self.cnt = 0
        self.file_name = "".split()

    def add_person(self, val):
        """Добавляет данные человека"""
        self.jotter[str(self.cnt)] = val  # ключ является счетчиком
        self.cnt += 1
        return 'Запись внесена'

    def del_name(self, name):
        """"Метод удаляет запись по номеру в списке"""
        if name in self.jotter:
            del self.jotter[name]
            return f'№{name} удален'
        return 'нет такого в списке'

    def change(self, name):
        """Метод изменяет запись"""
        if name in self.jotter:
            print('Введите новые данные ')
            new_lst = [input("Имя: "),
                       input("Фамилия: "),
                       input("Дата рождения: "),
                       input("Номер телефона: "),
                       input("Адресс: ")]
            self.jotter[name] = new_lst
            data = ' '.join(self.jotter[name])
            return f'Данные исправлены = №{name} {data}'
        return 'нет такого в списке'

    def find_person(self, name):
        """Метод ищет по имени и по номеру телефона"""
        while True:
            for key, val in self.jotter.items():
                val1, val2, val3, val4, val5 = val
                if val1 == name:
                    data = ' '.join(self.jotter[key])
                    return f'{data}'
                if val4 == name:
                    data = ' '.join(self.jotter[key])
                    return f'{data}'
            else:
                return "Контакт не найден"

    def srt_list(self):
        """Метод сортирует по имени и по фамилии"""
        print('''Выберите что вы хотите сделать
                * 1 - Сортировать по Имени
                * 2 - Сортировать по Фаимилии''')
        print("Введите команду \n")
        command = input()
        if command == '1':
            srt = sorted(self.jotter.items(), key=lambda item: item[1])
            srt = dict(srt)
            self.jotter.clear()
            self.jotter = srt
            return f'Список обновлён'
        elif command == '2':
            srt = sorted(self.jotter.items(), key=lambda item: item[1][1])
            srt = dict(srt)
            self.jotter.clear()
            self.jotter = srt
            return f'Список обновлён'

    def exit(self):
        """Метод закрывает программу и записывает все данные в фаил"""
        with open(f"{self.file_name}.txt", "w", encoding="utf-8") as f:
            for key, val in Notebook.info(self):
                val = ' '.join(val)
                f.write('{}\n'.format(val))
            print("Вы вышли с программы")
            return exit()

    def chek_file(self):
        """Метод считывает информацию с существуещего фаила и обьявляет
        сколько записей было в несено в программу, а так же если фаила нет
        предлогает создать новый"""
        self.file_name = input("Ввидите наименование фаила \n")
        try:
            with open(f"{self.file_name}.txt", "r", encoding="utf-8") as infile:
                for i in infile.readlines():
                    val = i.split()
                    Notebook.add_person(self, val)
                print(f"Загружено {self.cnt} записей")
        except IOError:
            print("Такого фаила нет")
            print("Выберите что вы хотите сделать\n"
                  f"* 1 - Создать новый фаил {self.file_name}\n"
                  "* 2 - Повторить попытку\n")
            command = input()
            if command == '1':  # Создаём новый фаил
                print("Удачной работы")
            elif command == '2':  # Повторяем попытку
                Notebook.chek_file(self)

    def info(self):
        """Метод воозвращает словарь созданных записей"""
        return self.jotter.items()

    def my_num_list(self):
        """Метод выводит ключ и значение, где ключ помогает определить с
        какой записью надо работать"""
        for key, val in Notebook.info(self):
            val = ' '.join(val)
            print("№", key, val)


def menu_note():
    """Метод экранного меню"""
    print('Записная книга')
    print("Выберите что вы хотите сделать\n"
          "* 1 - Добавить запись\n"
          "* 2 - Удалить запись \n"
          "* 3 - Изменить запись \n"
          "* 4 - Поиск\n"
          "* 5 - Сортировка\n"
          "* 6 - Выход\n"
          "* 7 - Количество записей")


def chek_menu(name):
    """Обязательный ввод значения"""
    name = name.strip()
    if name == "":
        print("Пустая строка !!!! Введите информацию")
        while True:
            say = input()
            say = say.strip()
            if say == "":
                print("Пустая строка !!!! Введите информацию")
            else:
                print("Информация принята все хорошо")
                return say
    return name


class FuncNoteBook(Notebook):
    """"Класс FuncNoteBook - наследник Class Notebook.
    Вызов данной программы осуществляеться:
            * start_book()
    Имеет методы:
            * Выводит на экран меню программы
            * Обрабатывает Экранное меню """

    def func_note(self):
        """Метод позволяющий обрабатывать метод экранного меню, в дальгейшем
        обращаясь к классу Notebook """
        self.chek_file()
        while True:
            menu_note()
            print("Введите команду \n")
            command = input()
            if command == '1':  # Добавляем данные
                new_list = [chek_menu(input("*Имя: ")),
                            chek_menu(input("*Фамилия: ")),
                            input("Дата рождения: "),
                            chek_menu(input("*Номер телефона: ")),
                            input("Адресс: ")]
                print(self.add_person(new_list))
            elif command == '2':  # Удаляем данные
                self.my_num_list()
                name = input("Введите номер списка который хотите удалить >:  ")
                print(self.del_name(name))
            elif command == '3':  # Изменяем данные
                self.my_num_list()
                name = input("Введите номер списка который хотите изменить >: ")
                print(self.change(name))
            elif command == '4':  # Ищем по имени или тел.номеру
                name = input("Введите имя или номер телефона контакта >:  ")
                print(self.find_person(name))
            elif command == '5':  # Сортируем по имени или фаимилии
                print(self.srt_list())
            elif command == '6':  # Выход
                print(self.exit())
            elif command == '7':  # Позволяет просметреть всех кто в базе данных
                for key, val in self.info():
                    val = ' '.join(val)
                    print(val)

            else:
                print('неизвестная команда')


def start_book():
    """Запускает программу для пользователя """
    st = FuncNoteBook()
    print(st.func_note())


__all__ = ["start_book"]

if __name__ == "__main__":
    start_book()
