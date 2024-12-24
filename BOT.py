import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('7765631188:AAEgAWBCj_TmFT26prHpCY4ICSasOycdCNg')

CHANNEL_ID = -1002163866848

def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

def create_subscription_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Подписаться🌟", url="https://t.me/+n5-qkfmgz6BhMTFi"))
    keyboard.add(InlineKeyboardButton(text="Проверить подписку🔃", callback_data="check_sub"))
    return keyboard

def create_key_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Получить ключ🔑", callback_data="get_key"))
    return keyboard

@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
    except:
        pass
        
    if not check_subscription(message.from_user.id):
        bot.send_message(
            message.chat.id,
            "<b>Подпишитесь пожалуйста на канал ниже чтобы продолжить:</b>",
            parse_mode='HTML',
            reply_markup=create_subscription_keyboard()
        )
    else:
        send_main_menu(message.chat.id)

def send_main_menu(chat_id):
    sent_message = bot.send_message(
        chat_id,
        "<b>🔑 Получите ваш бесплатный ключ для читов от VELNETS\n\n"
        "⚙️ Ключ нужен для авторизации, после этого, вы можете бесплатно пользоваться читами от VELNETS\n\n"
        "⚠️ Вам запрещено публиковать ваш специальный ключ в публичный доступ.</b>",
        parse_mode='HTML',
        reply_markup=create_key_keyboard()
    )
    return sent_message

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "check_sub":
        if not check_subscription(call.from_user.id):
            bot.answer_callback_query(
                call.id,
                "❌ Вы не подписались на канал подпишитесь",
                show_alert=True
            )
        else:
            try:
                bot.delete_message(call.message.chat.id, call.message.message_id)
            except:
                pass
            send_main_menu(call.message.chat.id)
            
    elif call.data == "get_key":
        try:
            bot.delete_message(call.message.chat.id, call.message.message_id)
        except:
            pass
            
        bot.send_message(
            call.message.chat.id,
            "<b>🔑 Ваш ключ для чита VELNETS\n\n"
            "🔓 Ключ:</b> <code>velnets777key7free</code>\n\n"
            "<b>⚠️ Никому не выдавайте ваш ключ! Люди могут использовать ваш ключ чтобы обойти защиту.</b>",
            parse_mode='HTML'
        )

bot.polling(none_stop=True)