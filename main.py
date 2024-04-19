import telebot
import button
import sqlite3

bot = telebot.TeleBot(str(input('Введите токен бота')

PrIsE = 200

connect = sqlite3.connect('useriddata.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS useridtable (
USID INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS mes_id_otzivy (
MESS_ID INTEGER,
MESS_ID_STAS INTEGER,
MESS_ID_3 INTEGER,
MESS_ID_4 INTEGER,
MESS_ID_5 INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS all_data_user (
USERID TEXT,
us_prise TEXT,
mess_id_wav_file TEXT,
NAME_ARTIST TEXT,
TYPE_RELIZE TEXT,
mess_id_photo TEXT,
DOGOVOR_FILE TEXT,
MAT TEXT,
USERURL TEXT,
NAME_TRACK TEXT,
DATE_RELIZE TEXT
)
''')

connect.commit()
connect.close()


def data_in_table(name_parameter, name_data, usidd):
    connect = sqlite3.connect('useriddata.db')
    cursor = connect.cursor()

    cursor.execute(f'UPDATE all_data_user SET {name_parameter} = ? WHERE USERID = ?',
                   (name_data, str(usidd)))

    connect.commit()
    connect.close()


def select_data(name_parameter, usidd):
    connect = sqlite3.connect('useriddata.db')
    cursor = connect.cursor()

    cursor.execute(f'SELECT {name_parameter} FROM all_data_user WHERE USERID = ?',
                   (str(usidd),))

    k_0 = list(set(cursor.fetchall()))
    k = [str(i)[1:-2] for i in k_0]

    connect.commit()
    connect.close()
    return k[0]


massivv = [1144748923, 1024476833, 1118325249, 6269154840, 1013942285]


@bot.message_handler(commands=['start'])
def adm_or_not(message):
    if message.from_user.id in massivv:
        start_admin(message)
    else:
        bot_start(message)


def bot_start(message):
    connect = sqlite3.connect('useriddata.db')
    cursor = connect.cursor()

    cursor.execute(f'INSERT INTO useridtable (USID) VALUES ({message.from_user.id})')
    cursor.execute(f'INSERT INTO all_data_user (USERID) VALUES ({message.from_user.id})')
    connect.commit()
    connect.close()

    bot.reply_to(message, f'Привет, {message.from_user.first_name}!'
                          f'\nДобро пожаловать в WAVXX '
                          f'MUSIC! \nМы занимаемся сведением и мастерингом треков, '
                          f'дистрибуцией, созданием обложек и полной подготовкой '
                          f'треков к площадкам')
    stop_message = bot.send_message(message.chat.id, 'Вы хотите оставить заявку на '
                                                     'дистрибуцию?',
                                    reply_markup=button.start_reply_bt)
    bot.register_next_step_handler(stop_message, distribution)


def start_admin(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Вижу, '
                                      f'что ты администратор! Сейчас я тебе расскажу о '
                                      f'основных командах для администратора...')
    next_start(message)


def next_start(message):
    bot.send_message(message.chat.id, 'Для того, чтобы отправить сообщение '
                                      'всем пользователям, введи команду /message')
    bot.send_message(message.chat.id, 'Чтобы добавить новый отзыв введи команду /otz')
    bot.send_message(message.chat.id, 'Чтобы изменить цену на платную дистрибуцию, '
                                      'введи команду /setprice')
    bot.send_message(message.chat.id, 'На этом пока что все! Приятного использования '
                                      'бота! Успеха)', reply_markup=button.del_btn)


def distribution(message):
    try:
        if (message.text == 'Да >>' or 'да' in str(message.text).lower() or
                'оставить заявку на дистрибуцию...' in str(message.text).lower()):
            bot.reply_to(message, f'Давай помогу вам определиться, какую дистрибуцию '
                                  f'выбрать? Платную ({PrIsE} рублей) или бесплатную?',
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
            connect = sqlite3.connect('useriddata.db')
            cursor = connect.cursor()

            try:
                cursor.execute('SELECT MESS_ID FROM mes_id_otzivy')
                k_0 = list(set(cursor.fetchall()))
                k = [int(str(i)[1:-2]) for i in k_0]

                for i in k:
                    bot.forward_message(message.from_user.id, 1024476833, i)
            except:
                pass

            try:
                cursor.execute('SELECT MESS_ID_STAS FROM mes_id_otzivy')
                P_0 = list(set(cursor.fetchall()))
                P = [int(str(i)[1:-2]) for i in P_0]

                connect.commit()
                for t in P:
                    bot.forward_message(message.from_user.id, 1144748923, t)
            except:
                pass

            try:
                cursor.execute('SELECT MESS_ID_3 FROM mes_id_otzivy')
                R_0 = list(set(cursor.fetchall()))
                R = [int(str(i)[1:-2]) for i in R_0]

                connect.commit()
                for s in R:
                    bot.forward_message(message.from_user.id, 1118325249, s)
            except:
                pass

            try:
                cursor.execute('SELECT MESS_ID_4 FROM mes_id_otzivy')
                x_0 = list(set(cursor.fetchall()))
                x = [int(str(i)[1:-2]) for i in x_0]

                connect.commit()
                for cv in x:
                    bot.forward_message(message.from_user.id, 6269154840, cv)
            except:
                pass

            try:
                cursor.execute('SELECT MESS_ID_5 FROM mes_id_otzivy')
                rrr_0 = list(set(cursor.fetchall()))
                rrr = [int(str(i)[1:-2]) for i in rrr_0]

                connect.commit()
                connect.close()
                for z in rrr:
                    bot.forward_message(message.from_user.id, 1013942285, z)
            except:
                pass
            stop_message = bot.send_message(message.chat.id, 'Пока что это все отзывы! '
                                                             'Скоро они '
                                                             'пополнятся... '
                                                             'А пока выберите, хотите ли '
                                                             'вы оставить заявку на '
                                                             'дистрибуцию?',
                                            reply_markup=button.start_reply_bt)
            bot.register_next_step_handler(stop_message, distribution)
        else:
            stop_message = bot.reply_to(message, 'К сожалению, я не знаю такой команды! '
                                                 'Нажмите на одну из кнопок ниже, чтобы '
                                                 'продолжить...')
            bot.register_next_step_handler(stop_message, distribution)
    except:
        print('Ошибка! Строка 107')
        stop_message = bot.reply_to(message, 'К сожалению, я не знаю такой команды! '
                                             'Нажмите на одну из кнопок ниже, чтобы '
                                             'продолжить...')
        bot.register_next_step_handler(stop_message, distribution)


def distribution_2(message):
    if 'Платную' in message.text:
        us_prise = 'Платная дистрибуция'

        stop_message = bot.send_message(message.chat.id, 'Хорошо. '
                                                         'Для начала пришлите '
                                                         'ваш трек в формате wav. '
                                                         '(Если это альбом, '
                                                         'то пришлите сразу все треки!)',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, file_wav)
        data_in_table('us_prise', us_prise, message.from_user.id)
    elif 'Бесплатную' in message.text:
        us_prise = 'Бесплатная дистрибуция'
        stop_message = bot.send_message(message.chat.id, 'Хорошо. '
                                                         'Для начала пришлите '
                                                         'ваш трек в формате wav. '
                                                         '\n(Если это альбом, '
                                                         'то пришлите сразу все треки!)',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, file_wav)
        data_in_table('us_prise', us_prise, message.from_user.id)
    elif 'отзывы' in str(message.text).lower():
        distribution(message)
    else:
        stop_message = bot.reply_to(message, 'К сожалению, я не знаю такой команды! '
                                             'Нажмите на одну из кнопок ниже, чтобы '
                                             'продолжить...')
        bot.register_next_step_handler(stop_message, distribution_2)


def file_wav(message):
    if message.content_type == 'document':
        mess_id_wav_file = message.message_id
        data_in_table('mess_id_wav_file', mess_id_wav_file,
                      message.from_user.id)
        stop_message = bot.send_message(message.chat.id, 'Теперь пришлите имя артиста'
                                                         ' (псевдоним)\n(Если трек '
                                                         'является фитом, то напишите '
                                                         'feat. и имя (псевдоним) '
                                                         'артиста, который принимал '
                                                         'участие в треке.)')
        bot.register_next_step_handler(stop_message, name_artist)
    else:
        stop_message = bot.send_message(message.chat.id, 'Вы должны прислать файл в '
                                                         'формате wav!!!')
        bot.register_next_step_handler(stop_message, file_wav)


def name_artist(message):
    NAME_ARTIST = message.text
    data_in_table('NAME_ARTIST', NAME_ARTIST, message.from_user.id)
    stop_message = bot.send_message(message.chat.id, 'Отлично! Теперь укажите'
                                                     ' дату релиза!')
    bot.register_next_step_handler(stop_message, date_relize)

def date_relize(message):
    DATE_RELIZE = message.text
    data_in_table('DATE_RELIZE', DATE_RELIZE, message.from_user.id)
    stop_message = bot.send_message(message.chat.id, 'Теперь укажите '
                                                     'название трека...')
    bot.register_next_step_handler(stop_message, name_track)


def name_track(message):
    NAME_TRACK = message.text
    data_in_table('NAME_TRACK', NAME_TRACK, message.from_user.id)
    stop_message = bot.send_message(message.chat.id, 'Отлично! Теперь выберете тип '
                                                     'релиза...',
                                    reply_markup=button.type_relize)
    bot.register_next_step_handler(stop_message, type_relize)


def type_relize(message):
    if str(message.text).lower() == 'сингл':
        TYPE_RELIZE = 'Сингл'
        data_in_table('TYPE_RELIZE', TYPE_RELIZE, message.from_user.id)
        stop_message = bot.send_message(message.chat.id, 'Спасибо! Теперь пришлите '
                                                         'обложку трека в формате '
                                                         '3000x3000',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, photo_treck)
    elif str(message.text).lower() == 'ер альбом':
        TYPE_RELIZE = 'Ер альбом'
        data_in_table('TYPE_RELIZE', TYPE_RELIZE, message.from_user.id)
        stop_message = bot.send_message(message.chat.id, 'Спасибо! Теперь пришлите '
                                                         'обложку трека в формате '
                                                         '3000x3000',
                                        reply_markup=button.del_btn)
        bot.register_next_step_handler(stop_message, photo_treck)
    elif str(message.text).lower() == 'альбом':
        TYPE_RELIZE = 'Альбом'
        data_in_table('TYPE_RELIZE', TYPE_RELIZE, message.from_user.id)
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
        mess_id_photo = message.message_id
        data_in_table('mess_id_photo', mess_id_photo, message.from_user.id)
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
        DOGOVOR_FILE = message.message_id
        data_in_table('DOGOVOR_FILE', DOGOVOR_FILE, message.from_user.id)
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
    USERURL = '@' + str(message.from_user.username)
    data_in_table('USERURL', USERURL, message.from_user.id)
    if 'нет' in str(message.text).lower():
        MAT = 'Нет'
        data_in_table('MAT', MAT, message.from_user.id)
        bot.send_message(message.chat.id, 'Отлично! Обрабатываю '
                                          'информацию...',
                         reply_markup=button.del_btn)
        if_free_or_sell(message)
    elif 'да' in str(message.text).lower():
        MAT = 'Да'
        data_in_table('MAT', MAT, message.from_user.id)
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
    USERURL = '@' + str(message.from_user.username)
    bot.send_message(message.chat.id, 'Извините, произошла техническая ошибка...'
                                      ' С вами свяжется администратор, для оформления'
                                      ' заказа в лс...')
    for i in massivv:
        bot.send_message(i, f'У пользователя {USERURL} произошла '
                            f'техническая ошибка во время оформления заказа... '
                            f'Свяжитесь с ним для оформления заказа...')


def if_free_or_sell(message):
    us_prise = (select_data('us_prise', message.from_user.id))[1:-1]
    if us_prise == 'Платная дистрибуция':
        bot.send_message(message.chat.id, 'Отправляю данные для завершения заказа...')
        bot.send_message(message.chat.id, f'Покупка составит {PrIsE} рублей. '
                                          f'\nОплатите по номеру +79506769732 \nТинькофф '
                                          f'\nОсипов Станислав В.')
        stop_message = bot.send_message(message.chat.id, 'После оплаты, отправьте '
                                                         'скриншот '
                                                         'операции админу - @Hexxx303',
                                        reply_markup=button.start_2)
        mailing_data_sell(message)
        bot.register_next_step_handler(stop_message, start_2)
    elif us_prise == 'Бесплатная дистрибуция':
        bot.send_message(message.chat.id, 'Отправляю данные для завершения заказа...')
        stop_message = bot.send_message(message.chat.id, 'С вами свяжется администратор, '
                                                         'как только '
                                                         'примет заказ',
                                        reply_markup=button.start_2)
        mailing_data_sell(message)
        bot.register_next_step_handler(stop_message, start_2)
    else:
        if_error(message)


def mailing_data_sell(message):
    try:
        USERID = message.from_user.id
        USERURL = (select_data('USERURL', USERID))[1:-1]
        us_prise = (select_data('us_prise', USERID))[1:-1]
        NAME_ARTIST = (select_data('NAME_ARTIST', USERID))[1:-1]
        TYPE_RELIZE = (select_data('TYPE_RELIZE', USERID))[1:-1]
        MAT = (select_data('MAT', USERID))[1:-1]
        mess_id_wav_file = (select_data('mess_id_wav_file', USERID))[1:-1]
        mess_id_photo = (select_data('mess_id_photo', USERID))[1:-1]
        DOGOVOR_FILE = (select_data('DOGOVOR_FILE', USERID))[1:-1]
        DATE_RELIZE = (select_data('DATE_RELIZE', USERID))[1:-1]
        NAME_TRACK = (select_data('NAME_TRACK', USERID))[1:-1]

        for i in massivv:
            bot.send_message(i, f'Пользователь {USERURL} ({USERID}) '
                                f'сделал заказ!'
                                f'\nЦена: {us_prise}'
                                f'\nИмя артиста: {NAME_ARTIST}'
                                f'\nНазвание трека: {NAME_TRACK}'
                                f'\nТип релиза: {TYPE_RELIZE}'
                                f'\nДата релиза: {DATE_RELIZE}'
                                f'\nЕсть ли маты в треке: {MAT}'
                                f'\n1-й файл - трек в формате wav'
                                f'\n2-й файл - обложка трека'
                                f'\n3-й файл - фото договора о покупке бита или '
                                f'видео с записью проекта бита')
            bot.forward_message(i, USERID, int(mess_id_wav_file))
            bot.forward_message(i, USERID, int(mess_id_photo))
            bot.forward_message(i, USERID, int(DOGOVOR_FILE))
    except:
        if_error(message)


def start_2(message):
    if 'Оставить заявку на еще одну дистрибуцию...' in message.text:
        bot_start(message)
    else:
        stop_message = bot.send_message(message.chat.id, 'Для того, чтобы оставить еще '
                                                         'одну заявку на дистрибуцию, '
                                                         'нажмите на кнопку ниже...')
        bot.register_next_step_handler(stop_message, start_2)


@bot.message_handler(commands=['message'])
def mess_com(message):
    stop_message = bot.send_message(message.chat.id, 'Давай отправим пользователям '
                                                     'сообщение. Введи его текст и '
                                                     'прикрепи файлы если они нужны!')
    bot.register_next_step_handler(stop_message, spam)


def spam(message):
    connect = sqlite3.connect('useriddata.db')
    cursor = connect.cursor()

    cursor.execute('SELECT USID FROM useridtable')
    k_0 = list(set(cursor.fetchall()))
    k = [int(str(i)[1:-2]) for i in k_0]

    connect.close()

    IDMES = message.message_id
    USERID = message.from_user.id

    for i in k:
        bot.forward_message(i, USERID, IDMES)

    bot.send_message(USERID, 'Сообщение отправленно всем пользователям!')
    next_start(message)


@bot.message_handler(commands=['otz'])
def otz_1(message):
    stop_message = bot.send_message(message.chat.id, 'Скинь сюда отзыв! (текст, фото, '
                                                     'видео. В общем все что хочешь)')
    bot.register_next_step_handler(stop_message, otz_2)


def otz_2(message):
    id_otz = message.message_id
    connect = sqlite3.connect('useriddata.db')
    cursor = connect.cursor()

    if str(message.from_user.id) == '1144748923':
        cursor.execute(f'INSERT INTO mes_id_otzivy (MESS_ID_STAS) VALUES '
                       f'({message.message_id})')
        connect.commit()
        connect.close()
        bot.send_message(message.chat.id, 'Отзыв добавлен!')
        next_start(message)
    elif str(message.from_user.id) == '1024476833':
        cursor.execute(
            f'INSERT INTO mes_id_otzivy (MESS_ID) VALUES ({message.message_id})')
        connect.commit()
        connect.close()
        bot.send_message(message.chat.id, 'Отзыв добавлен!')
        next_start(message)
    elif str(message.from_user.id) == '1118325249':
        cursor.execute(
            f'INSERT INTO mes_id_otzivy (MESS_ID_3) VALUES ({message.message_id})')
        connect.commit()
        connect.close()
        bot.send_message(message.chat.id, 'Отзыв добавлен!')
        next_start(message)
    elif str(message.from_user.id) == '6269154840':
        cursor.execute(
            f'INSERT INTO mes_id_otzivy (MESS_ID_4) VALUES ({message.message_id})')
        connect.commit()
        connect.close()
        bot.send_message(message.chat.id, 'Отзыв добавлен!')
        next_start(message)
    elif str(message.from_user.id) == '1013942285':
        cursor.execute(
            f'INSERT INTO mes_id_otzivy (MESS_ID_5) VALUES ({message.message_id})')
        connect.commit()
        connect.close()
        bot.send_message(message.chat.id, 'Отзыв добавлен!')
        next_start(message)


@bot.message_handler(commands=['setprice'])
def set_priseee(message):
    stop_message = bot.send_message(message.chat.id, 'Введите новую цену! (Число без '
                                                     'букв!!!)')
    bot.register_next_step_handler(stop_message, set_pr)


def set_pr(message):
    global PrIsE
    PrIsE = int(message.text)
    bot.send_message(message.chat.id, 'Цена установлена!')
    next_start(message)


@bot.message_handler(content_types=['text'])
def helper(message):
    bot.reply_to(message, 'Произошел перезапуск бота на сервере. Пожалуйста нажмите на '
                          'команду /start')


bot.infinity_polling(timeout=10, long_polling_timeout=5)
