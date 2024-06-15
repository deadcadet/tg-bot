import random
import math

# Common functions:


def get_question(game_type):
    if game_type == 'calc':
        expression, correct_answer = generate_random_expression()
        question = get_rules(game_type) + f'Question: {expression}'
    if game_type == 'even':
        random_number = get_random_number(1, 100)
        correct_answer = 'yes' if is_even(random_number) else 'no'
        question = get_rules(game_type) + f'Question: {random_number}'
    if game_type == 'gcd':
        num1 = get_random_number(1, 100)
        num2 = get_random_number(1, 100)
        question = get_rules(game_type) + f"Question: {num1} {num2}"
        correct_answer = math.gcd(num1, num2)
    if game_type == 'progression':
        progression, correct_answer = generate_progression()
        question = get_rules(game_type) + f"Question: {show(progression)}"
    if game_type == 'prime':
        random_number = get_random_number(1, 100)
        question = get_rules(game_type) + f"Question: {random_number}"
        correct_answer = 'yes' if is_prime(random_number) else 'no'
    return question, correct_answer


def welcome_user(user):
    msg = f'Welcome to the Brain Games. {user}!. Choose a game!'
    return msg


def get_rules(game_type):
    games = {
        'even': 'Answer "yes" if the number is even, otherwise answer "no".\n',
        'calc': 'What is the result of the expression?\n',
        'gcd': 'Find the greatest common divisor of given numbers.\n',
        'progression': 'What number is missing in the progression?\n',
        'prime': 'Answer "yes" if given number is prime. Otherwise answer "no".\n'
    }
    return games[game_type]


def get_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


# Functions for CALC game:
def generate_random_expression():
    operators = ['+', '-', '*']
    num1 = get_random_number(1, 10)
    num2 = get_random_number(1, 10)
    operator = random.choice(operators)
    expression = f"{num1} {operator} {num2}"
    result = eval(expression)
    return expression, result


# Functions for EVEN game:
def is_even(number):
    return True if number % 2 == 0 else False


# Functions for PROGRESSION game:
def generate_progression():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    length = random.randint(5, 15)
    progression = [start + step * i for i in range(length)]
    index_to_find = random.randint(0, length - 1)
    correct_answer = progression[index_to_find]
    progression[index_to_find] = '..'
    return progression, correct_answer


def show(progression):
    prog = ''
    for i in range(0, len(progression)):
        prog = prog + str(progression[i]) + ' '
    return prog


# Functions for PRIME game:
def is_prime(number):
    if number == 1:
        return False
    if number == 2 and number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
