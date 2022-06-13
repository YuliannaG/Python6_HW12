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
            phone_contact: 'phone', birthday_contact: 'birthday', func_exit: ['good buy', 'close', 'exit']}


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
    while True:
        user_input = input('>>>')
        user_command = normalize(user_input)
        result = output_func(user_command)
        print(result)
        if result == 'Good bye!':
            break


if __name__ == '__main__':
    filename = 'address_book.txt'
    main()

#
# def save_to_file:
#     with shelve.open(filename) as ab:
    #
    # with shelve.open(filename) as ab:
    #     user_input = input('To work with Address book print "main". To search by part or the name or phone number print "search".')
    #     if user_input == 'main':
    #         main()
    #     elif user_input == 'search':
    #         search_input = input('Please, enter part of the name (lowercase) or part of the phone number to search for the record.')
    #         for line in ab:
    #             if search_input in line:
    #                 print(line)
    #         print('No such record in the Address book.')
    #     else:
    #         print('Please, enter correct command')
