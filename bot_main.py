# coding=utf-8
import telebot
import constants
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

bot = telebot.AsyncTeleBot(constants.token)
print ("Bot is started")


@bot.message_handler(commands=['help'])
def handle_command(message):
    bot.send_message(message.chat.id,
                     "Привет! Ты попал в раздел помощи. Смотри, в чем дело. Я понимаю определенный текст и умею его обрабатывать. По ходу заказа нужно нажимать кнопки, которые будут появляться под клавиатурой, они представляют само меню. Там ты сможешь выбрать продукцию, ее размер и время, на которую ты хочешь ее получить. А команд у меня все две : \n/start - для оформления заказа \n/help - для получения справки")

    # start is the first command from user


@bot.message_handler(commands=['start'])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    user_markup.row(constants.command_make_order)
    bot.send_message(message.from_user.id, "Привет!" + " " +  "Я готов слушать твой заказ, давай начнем!",
                     reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    user_id = message.from_user.id
    if user_id not in constants.collectCategories:
        constants.collectCategories[user_id] = ""

    # --------------------------  commands  -----------------------------------------------------------
    if message.text.decode('utf-8') == constants.command_make_order.decode('utf-8'):
        constants.collectCategories[user_id] = ""
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.order_hot, constants.order_cold, constants.order_food)
        bot.send_message(message.from_user.id, "Выбери, чего душа желает!", reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.command_finish_order.decode('utf-8'):
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

        # ----------------------------- Set the prize-----------------
        if constants.size_m in constants.collectCategories[user_id]:
            if constants.coffee_capuchino in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "17"
            elif constants.coffee_late in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "17"
            elif constants.coffee_ruf in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "22"
            elif constants.coffee_flat_white in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "21"
            elif constants.want_cacao in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "18"
        elif constants.size_l in constants.collectCategories[user_id]:
            if constants.coffee_capuchino in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "22"
            elif constants.coffee_late in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "22"
            elif constants.coffee_ruf in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "27"
            elif constants.coffee_flat_white in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "26"
            elif constants.want_cacao in constants.collectCategories[user_id]:
                constants.collectCategories[user_id] += " " + "Цена" + " " + "23"
        elif constants.coffee_espresso in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "12"
        elif constants.without_milk in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "12"
        elif constants.with_milk in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "14"
        elif constants.want_tea in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "10"
        elif constants.drink_cola in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "10"
        elif constants.drink_water in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "8"
        elif constants.drink_burn in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "20"
        elif constants.drink_nestea in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "14"
        elif constants.food_pizza_with_chicken in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "Цена" + " " + "17"
        elif constants.food_pizza_with_meat in constants.collectCategories[user_id]:
            constants.collectCategories[user_id] += " " + "17"

        length = len(constants.collectCategories[user_id])
        first_symbol = constants.collectCategories[user_id].find("Цена") + 5

        price = ""
        i = first_symbol
        while i < length:
            price += constants.collectCategories[user_id][i]
            i += 1

        bot.send_message(message.from_user.id,
                         "Хорошего дня! Заказ скоро будет готов. К оплате" + " " + price + " " + "грн")
        bot.send_message(message.from_user.id,
                         "Для еще одного заказа тыкай кнопку /start или пиши эту команду")
        user_markup.row('/start')

        user_name = ""
        if message.from_user.first_name is not None:
            user_name += message.from_user.first_name.decode('utf-8')
            if message.from_user.last_name is not None:
                user_name += " " + message.from_user.last_name.decode('utf-8')
        print ("Заказ :" + " " + constants.collectCategories[user_id])
        print ("Кто :" + " " + user_name)
        print (message.from_user.id)
        print ("")

        bot.send_message(constants.nikita_chat_id,
                         "Заказ : " + constants.collectCategories[user_id] + "\nКто : " + user_name + "\nid : " + str(
                             message.from_user.id))
        constants.collectCategories[user_id] = ""
        del constants.collectCategories[user_id]

        # ---------------------------  Coffee  -----------------------------------------------

    elif message.text.decode('utf-8') == constants.order_hot.decode('utf-8'):
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.want_coffee, constants.want_tea, constants.want_cacao)
        bot.send_message(message.from_user.id, "Чего именно ты хочешь?", reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.want_coffee.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.coffee_espresso, constants.coffee_capuchino, constants.coffee_late)
        user_markup.row(constants.coffee_ruf, constants.coffee_flat_white, constants.coffee_americano)
        bot.send_message(message.from_user.id, "Кофе - он разный бывает... Какой?", reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.coffee_espresso.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.coffee_capuchino.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.size_m, constants.size_l)
        bot.send_message(message.from_user.id, "Кофе средний или большой?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.coffee_late.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.size_m, constants.size_l)
        bot.send_message(message.from_user.id, "Кофе средний или большой?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.coffee_ruf.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.size_m, constants.size_l)
        bot.send_message(message.from_user.id, "Кофе средний или большой?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.coffee_flat_white.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.size_m, constants.size_l)
        bot.send_message(message.from_user.id, "Кофе средний или большой?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.coffee_americano.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.with_milk, constants.without_milk)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)
    elif message.text.decode('utf-8') == constants.with_milk.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)
    elif message.text.decode('utf-8') == constants.without_milk.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

        # --------------------------------------  Tea  ------------------
    elif message.text.decode('utf-8') == constants.want_tea.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.tea_black, constants.tea_green, constants.tea_fruit)
        bot.send_message(message.from_user.id, "А вот чай у нас большоой", reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.tea_black.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.tea_green.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.tea_fruit.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

        # -------------------------  Cacao ---------------
    elif message.text.decode('utf-8') == constants.want_cacao.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.size_m, constants.size_l)
        bot.send_message(message.from_user.id, "Кофе средний или большой?",
                         reply_markup=user_markup)

        # -------------------------- Cold drinks ----------------

    elif message.text.decode('utf-8') == constants.order_cold.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.drink_cola, constants.drink_nestea)
        user_markup.row(constants.drink_water, constants.drink_burn)
        bot.send_message(message.from_user.id, "Что пьем?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.drink_water.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.drink_nestea.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.drink_cola.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.drink_burn.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)
        # --------------------------  Food ----------------------
    elif message.text.decode('utf-8') == constants.order_food.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.food_pizza_with_chicken, constants.food_pizza_with_meat)
        bot.send_message(message.from_user.id, "Что будем есть? Какую пиццу?:)",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.food_pizza_with_meat.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.food_pizza_with_chicken.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

        # --------------------------  Time ----------------------
    elif message.text.decode('utf-8') == constants.time_between_1_and_2.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.command_finish_order)
        print (constants.collectCategories)
        bot.send_message(message.from_user.id, "Последний шаг, нужно подтвердить заказ", reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.time_between_2_and_3.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.command_finish_order)
        bot.send_message(message.from_user.id, "Последний шаг, нужно подтвердить заказ", reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.time_between_3_and_4.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.command_finish_order)
        bot.send_message(message.from_user.id, "Последний шаг, нужно подтвердить заказ", reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.time_now.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.command_finish_order)
        bot.send_message(message.from_user.id, "Последний шаг, нужно подтвердить заказ", reply_markup=user_markup)

        # --------------------------  Size ----------------------

    elif message.text.decode('utf-8') == constants.size_s.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.size_m.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)

    elif message.text.decode('utf-8') == constants.size_l.decode('utf-8'):
        constants.collectCategories[user_id] += " " + message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row(constants.time_between_1_and_2, constants.time_between_2_and_3)
        user_markup.row(constants.time_between_3_and_4, constants.time_now)
        bot.send_message(message.from_user.id, "На какое время приготовить? На перемене между парами или сейчас?",
                         reply_markup=user_markup)
    else :
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        user_markup.row('/start')
        bot.send_message(message.from_user.id, "Наши отношения стали очень сложными. Я тебя прощу, давай начнем все сначала",
                         reply_markup=user_markup)


bot.polling(none_stop=True)
