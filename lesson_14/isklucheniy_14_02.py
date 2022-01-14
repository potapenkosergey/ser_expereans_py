# TODO Исключения 14_02.
class PasswordError(Exception):
    msg = 'Неверный пароль!'

    def __init__(self, value=None):
        if value is not None:
            self.msg = value

    def __str__(self):
        return self.msg


def f_password(password):
    enter_password = 'serg.7777'

    try:
        if password != enter_password:
            raise PasswordError('Неверный пароль!')
    except PasswordError as error:
        print(error.__str__())


name = input('Введите пароль(правильный пароль serg.7777):')
f_password(name)
