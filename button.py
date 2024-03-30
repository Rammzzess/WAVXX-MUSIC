import telebot
from telebot import types


start_reply_bt = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Да >>')
btn2 = types.KeyboardButton('Нет --')
btn3 = types.KeyboardButton('Отзывы >>')
start_reply_bt.add(btn1, btn2, btn3)

distribution = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Оставить заявку на дистрибуцию...')
distribution.add(btn1)

distribution_prise = types.ReplyKeyboardMarkup(resize_keyboard=True)
sell = types.KeyboardButton('Платную')
free = types.KeyboardButton('Бесплатную')
distribution_prise.add(sell, free)

type_relize = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Сингл')
btn2 = types.KeyboardButton('Ер альбом')
btn3 = types.KeyboardButton('Альбом')
type_relize.add(btn1, btn2, btn3)

yes_no = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Да')
btn2 = types.KeyboardButton('Нет')
yes_no.add(btn1, btn2)

start_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Оставить заявку на еще одну дистрибуцию...')
start_2.add(btn1)

del_btn = types.ReplyKeyboardRemove()