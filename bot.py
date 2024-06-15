import telebot
from telebot import types
from game_functions import get_question as get_question
from game_functions import welcome_user as welcome_user

API_TOKEN = '7346594372:AAE5zBU80VkMxfcYK-Hd4sA5owJwfPnwQ5Y'
bot = telebot.TeleBot(API_TOKEN)


user_state = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_state[message.chat.id] = None
    markup = types.ReplyKeyboardMarkup(row_width=2)
    calc_btn = types.KeyboardButton('/calc')
    even_btn = types.KeyboardButton('/even')
    progression_btn = types.KeyboardButton('/progression')
    prime_btn = types.KeyboardButton('/prime')
    gcd_btn = types.KeyboardButton('/gcd')
    markup.add(calc_btn, even_btn, progression_btn, prime_btn, gcd_btn)
    bot.send_message(message.chat.id, welcome_user(message.from_user.first_name), reply_markup=markup)  # noqa E501


@bot.message_handler(commands=['calc',
                               'even',
                               'progression',
                               'prime',
                               'gcd'])
def start_game(message):
    game_type = message.text[1:]
    question, answer = get_question(game_type)
    user_state[message.chat.id] = {'game': game_type, 'answer': answer}
    bot.send_message(message.chat.id, question)


@bot.message_handler(commands=['stop'])
def stop_game(message):
    user_state[message.chat.id] = None
    bot.send_message(message.chat.id, 'Game stopped. You can choose another game')


@bot.message_handler(func=lambda message: True)
def check_answer(message):
    user_data = user_state.get(message.chat.id)
    if not user_data:
        bot.send_message(message.chat.id, 'Start a game using /start')
        return
    current_game = user_data
    if message.text.lower() == str(current_game['answer']):
        bot.send_message(message.chat.id, 'Right!')
    else:
        bot.send_message(message.chat.id, f'Wrong! Correct answer was: {current_game['answer']}')  # noqa E501            
        bot.send_message(message.chat.id, "Start a new game using /start")
        bot.send_message(message.chat.id, 'You won! Press /start if u wanna play again')  # noqa E501
    user_state[message.chat.id] = None


bot.polling()
