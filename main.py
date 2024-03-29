import telebot
import button

from telebot import types

bot = telebot.TeleBot('6597040115:AAH9wOSD44nJm21g8vNoIj7mAkxzrxVcJnk')

PrIsE = 200


@bot.message_handler(commands=['start'])
def bot_start(message):
    global USERID
    global USERURL
    USERID = message.from_user.id
    USERURL = '@' + message.from_user.username
    print(message.from_user.first_name, message.from_user.id)
    bot.reply_to(message, f'Привет, {message.from_user.first_name}!'
                          f'\nДобро пожаловать в WAVXX '
                          f'MUSIC! \nМы занимаемся сведением и мастерингом треков, '
                          f'дистрибуцией, созданием обложек и полной подготовкой '
                          f'треков к площадкам')
    stop_message = bot.send_message(message.chat.id, 'Вы хотите оставить заявку на '
                                                     'дистрибуцию?',
                                    reply_markup=button.start_reply_bt)
    bot.register_next_step_handler(stop_message, distribution)


def distribution(message):
    try:
        if (message.text == 'Да >>' or 'да' in str(message.text).lower() or
                'оставить заявку на дистрибуцию...' in str(message.text).lower()):
            bot.reply_to(message, 'Давай помогу вам определиться, какую дистрибуцию '
                                  'выбрать? Платную (Recommend) или бесплатную?',
                         reply_markup=button.distribution_prise)
            bot.send_message(message.chat.id, 'Почему стоит выбрать именно платную '
                                              'дистрибуцию? \n1) Роялти с вашего трека '
                                              'идут прямиком вам\n2) Промо поддержка '
                                              'трека\n3) На всем пути с начала до '
                                              'публикации трека на площадки мы будем '
                                              'помогать и проводить по всему пути "за '
                                              'руку"\n4) Помещаем ваш трек в своей '
                                              'группе (Прослушивания = ваш доход)\n5) '
                                              'Ежедневная статистика трека')
            stop_message = bot.send_message(message.chat.id, 'Какую дистрибуцию '
                                                             'выберете?')
            bot.register_next_step_handler(stop_message, distribution_2)
        elif 'нет' in str(message.text).lower():
            stop_message = bot.reply_to(message, 'Очень жаль(( Если решите вернуться, '
                                                 'нажмите на кнопку ниже!',
                                        reply_markup=button.distribution)
            bot.register_next_step_handler(stop_message, distribution)
        elif 'отзывы' in str(message.text).lower():
            pass
        else:
            stop_message = bot.reply_to(message, 'К сожалению, я не знаю такой команды! '
                                                 'Нажмите на одну из кнопок ниже, чтобы '
                                                 'продолжить...')
            bot.register_next_step_handler(stop_message, distribution)
    except:
        stop_message = bot.reply_to(message, 'К сожалению, я не знаю такой команды! '
                                             'Нажмите на одну из кнопок ниже, чтобы '
                                             'продолжить...')
        bot.register_next_step_handler(stop_message, distribution)


def distribution_2(message):
    global us_prise
    if 'Платную' in message.text:
        us_prise = 'Платная дистрибуция'

        stop_message = bot.send_message(message.chat.id, 'Хорошо. '
                                                         'Для начала пришлите '
                                                         'ваш трек в формате wav',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, file_wav)
    elif 'Бесплатную' in message.text:
        us_prise = 'Бесплатная дистрибуция'

        stop_message = bot.send_message(message.chat.id, 'Хорошо. '
                                                         'Для начала пришлите '
                                                         'ваш трек в формате wav',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, file_wav)
    else:
        stop_message = bot.reply_to(message, 'К сожалению, я не знаю такой команды! '
                                             'Нажмите на одну из кнопок ниже, чтобы '
                                             'продолжить...')
        bot.register_next_step_handler(stop_message, distribution_2)


def file_wav(message):
    if message.content_type == 'document':
        global mess_id_wav_file
        mess_id_wav_file = message.message_id
        stop_message = bot.send_message(message.chat.id, 'Теперь пришлите имя артиста'
                                                         ' (псевдоним)')
        bot.register_next_step_handler(stop_message, name_artist)
    else:
        stop_message = bot.send_message(message.chat.id, 'Вы должны прислать файл в '
                                                         'формате wav!!!')
        bot.register_next_step_handler(stop_message, file_wav)


def name_artist(message):
    global NAME_ARTIST
    NAME_ARTIST = message.text
    stop_message = bot.send_message(message.chat.id, 'Отлично! Теперь выберете тип '
                                                     'релиза...',
                                    reply_markup=button.type_relize)
    bot.register_next_step_handler(stop_message, type_relize)


def type_relize(message):
    global TYPE_RELIZE
    if str(message.text).lower() == 'сингл':
        TYPE_RELIZE = 'Сингл'
        stop_message = bot.send_message(message.chat.id, 'Спасибо! Теперь пришлите '
                                                         'обложку трека в формате '
                                                         '3000x3000',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, photo_treck)
    elif str(message.text).lower() == 'ер альбом':
        TYPE_RELIZE = 'Ер альбом'
        stop_message = bot.send_message(message.chat.id, 'Спасибо! Теперь пришлите '
                                                         'обложку трека в формате '
                                                         '3000x3000',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, photo_treck)
    elif str(message.text).lower() == 'альбом':
        TYPE_RELIZE = 'Альбом'
        stop_message = bot.send_message(message.chat.id, 'Спасибо! Теперь пришлите '
                                                         'обложку трека в формате '
                                                         '3000x3000',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, photo_treck)
    else:
        stop_message = bot.send_message(message.chat.id, 'Пожалуйста, воспользуйтесь '
                                                         'кнопками для выбора типа '
                                                         'релиза...')
        bot.register_next_step_handler(stop_message, type_relize)


def photo_treck(message):
    if message.content_type == 'photo' or message.content_type == 'document':
        global mess_id_photo
        mess_id_photo = message.message_id
        stop_message = bot.send_message(message.chat.id, 'Пришлите фото договора о '
                                                         'покупке бита,а если бит ваш,'
                                                         'то пожалуйста запишите 30-ти '
                                                         'секундное видео с записью '
                                                         'проекта бита')
        bot.register_next_step_handler(stop_message, dogovor)
    else:
        stop_message = bot.send_message(message.chat.id, 'Вы должны прислать обложку '
                                                         'для трека файлом или '
                                                         'фотографией в разрешении '
                                                         '3000х3000')
        bot.register_next_step_handler(stop_message, photo_treck)


def dogovor(message):
    if (message.content_type == 'photo' or message.content_type == 'document' or
            message.content_type == 'video'):
        global DOGOVOR_FILE
        DOGOVOR_FILE = message.message_id
        stop_message = bot.send_message(message.chat.id, 'Есть ли маты в вашем треке? ('
                                                         'Да | Нет)',
                                        reply_markup=button.yes_no)
        bot.register_next_step_handler(stop_message, mat_in_track)
    else:
        stop_message = bot.send_message(message.chat.id, 'Пришлите фото договора о '
                                                         'покупке бита,а если бит ваш,'
                                                         'то пожалуйста запишите 30-ти '
                                                         'секундное видео с записью '
                                                         'проекта бита')
        bot.register_next_step_handler(stop_message, dogovor)


def mat_in_track(message):
    global MAT
    if 'нет' in str(message.text).lower():
        MAT = 'Нет'
        bot.send_message(message.chat.id, 'Отлично! Обрабатываю '
                                                         'информацию...',
                                        reply_markup=button.del_btn)
        if_free_or_sell(message)
    elif 'да' in str(message.text).lower():
        MAT = 'Да'
        bot.send_message(message.chat.id, 'Отлично! Обрабатываю '
                                                         'информацию...',
                                        reply_markup=button.del_btn)
        if_free_or_sell(message)
    else:
        stop_message = bot.send_message(message.chat.id, 'Воспользуйтесь кнопками. '
                                                         'Есть ли маты в вашем треке? ('
                                                         'Да | Нет)')
        bot.register_next_step_handler(stop_message, mat_in_track)


def if_error(message):
    bot.send_message(message.chat.id, 'Извините, произошла техническая ошибка...'
                                      ' С вами свяжется администратор, для оформления'
                                      ' заказа в лс...')
    bot.send_message(1024476833, f'У пользователя {USERURL} произошла '
                                 f'техническая ошибка во время оформления заказа... '
                                 f'Свяжитесь с ним для оформления заказа...')


def if_free_or_sell(message):
    if us_prise == 'Платная дистрибуция':
        bot.send_message(message.chat.id, 'Отправляю данные для завершения заказа...')
        bot.send_message(message.chat.id, f'Покупка составит {PrIsE} рублей. '
                                          f'\nОплатите по номеру +79506769732 \nТинькофф '
                                          f'\nОсипов Станислав В.')
        bot.send_message(message.chat.id, 'После оплаты, отправьте скриншот '
                                          'операции админу - @Hexxx303')
        mailing_data_sell()
    elif us_prise == 'Бесплатная дистрибуция':
        bot.send_message(message.chat.id, 'Отправляю данные для завершения заказа...')
        bot.send_message(message.chat.id, 'С вами свяжется администратор, как только '
                                          'примет заказ')
        mailing_data_sell()
    else:
        if_error(message)


def mailing_data_sell():
    bot.send_message(1024476833, f'Пользователь {USERURL} сделал заказ!'
                                 f'\nЦена: {us_prise}'
                                 f'\nИмя артиста: {NAME_ARTIST}'
                                 f'\nТип релиза: {TYPE_RELIZE}'
                                 f'\nЕсть ли маты в треке: {MAT}'
                                 f'\n1-й файл - трек в формате wav'
                                 f'\n2-й файл - обложка трека'
                                 f'\n3-й файл - фото договора о покупке бита или видео '
                                 f'с записью проекта бита')
    # TO_CHAT_ID = "593069749"  # айди пользователя ,которому должен приходить файл
    bot.forward_message(1024476833, USERID, mess_id_wav_file)
    bot.forward_message(1024476833, USERID, mess_id_photo)
    bot.forward_message(1024476833, USERID, DOGOVOR_FILE)


bot.polling(none_stop=True)
