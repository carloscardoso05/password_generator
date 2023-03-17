import random


def unicode_to_str(codes: list):
    codes_str = ''
    for code in codes:
        codes_str += chr(code)
    return codes_str


def filter_chars(options: dict) -> str:
    """
    options -> a dictionary that represents either a type of character can be used or not, it must have the following structure:
        options = {
            'uppercase': <bool>,
            'lowercase': <bool>,
            'number': <bool>,
            'special': <bool>
        }
    """

    valid_chars = ''
    chars = {
        'uppercase': (unicode_to_str(range(65, 91))),
        'lowercase': (unicode_to_str(range(97, 123))),
        'number': (unicode_to_str(range(48, 58))),
        'special': (unicode_to_str([*range(33, 48), *range(58, 65), *range(91, 97), *range(123, 127)]))
    }

    if not any(options.values()):
        raise ValueError('All options are false.')

    # creates a string with all the characters that can be used
    for type, wanted in options.items():
        if wanted:
            valid_chars += chars[type]

    return valid_chars


def create_password(length: int, options: dict) -> str:
    password = ''
    valid_chars = filter_chars(options)

    # randomly chooses the characters of the password
    for i in range(length):
        password += random.choice(valid_chars)

    return password


def read_answer(answer: str) -> bool:
    """
    - Validates a console input to avoid value errors
    - Accepts both uppercase and lowercase input
    - Valid inputs:
        - True/Yes: S, Y, 1, or True
        - False/No: N, 0 or False
    """
    if isinstance(answer, str):
        if answer.upper() in 'SY1 TRUE':
            return True
        elif answer.upper() in 'N0 FALSE':
            return False
        else:
            raise ValueError('Invalid option.')
    else:
        raise TypeError('Invalid type.')


def define_options():
    "define which types of characters will be used in the password"
    options = {
        'uppercase': False,
        'lowercase': False,
        'number': False,
        'special': False
    }

    for type, value in options.items():
        options[type] = read_answer(
            input(f'Want to have {type} in your password?[Y/N] '))

    return options


if __name__ == '__main__':    
    length = int(input("Length of your password: "))

    options = define_options()
    print('Your password is:', create_password(length, options))
