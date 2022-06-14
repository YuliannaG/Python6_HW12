"""Цикл запрос-ответ. Эта часть приложения отвечает за получения от пользователя данных
и возврат пользователю ответа от функции-handlerа."""
from handler import *
from parser import normalize
import shelve

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Please, check the data format:\n- name should be latin letters only;\n- phone should be in format + /country code/ /area code/ /phone number/;\n- date of birth should be in format yyyy/mm/dd.'
        except TypeError:
            return 'Please enter full command'
    return inner


COMMANDS = {func_hello: 'hello', show_all: 'show all', add_contact: 'add', change_contact: 'change',
            phone_contact: 'phone', birthday_contact: 'birthday', func_exit: ['good buy', 'close', 'exit'], func_search: 'search'}


@input_error
def output_func(user_command):
    command = user_command['command']
    name_command = user_command['name']
#    phone_command = None if (user_command['phone'] == []) else user_command['phone']
    phone_command = user_command['phone']
    birthday_command = user_command['birthday']
    for k, v in COMMANDS.items():
        if command in v:
            return k(name=name_command, phone=phone_command, birthday=birthday_command)   # name_command, *phone_command, birthday_command


def main():
    print('Address book\nCommands:\nadd name phone DOB\nchange name old_phone new_phone\nshow all\nbirthday name\nphone name\nsearch')
    while True:
        user_input = input('>>>')
        user_command = normalize(user_input)
        result = output_func(user_command)
        print(result)
        if result == 'Good bye!':
            break


if __name__ == '__main__':
    main()

