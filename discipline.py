from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackQueryHandler
import datetime

vaqt = []
reja = []
rejalar = []


def keyboard_btns(type=None):
    if type == "reja":
        btn = [
            [KeyboardButton("Day 🔆"),
             KeyboardButton("Week 🔅")],
            [KeyboardButton("SAVE ✅")]
        ]
    elif type == "rejalar":
        btn = [
            [KeyboardButton("Restaran 🍽"),
             KeyboardButton("Sport 🏀")],
            [KeyboardButton("Sayr qilish 🚞"),
             KeyboardButton("Dam olish 🎮")],
            [KeyboardButton("Boshqa ishlar ❔")]
        ]
    else:
        btn = []
    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def kun_botn():
    return [
        [InlineKeyboardButton("30 𝘮𝘪𝘯𝘶𝘵 🕝", callback_data=f"30"),
         InlineKeyboardButton("45 𝘮𝘪𝘯𝘶𝘵 🕟", callback_data=f"45"),
         InlineKeyboardButton("1 𝘴𝘰𝘢𝘵 🕞", callback_data=f"1")],
        [InlineKeyboardButton("1.5 𝘴𝘰𝘢𝘵 🕝", callback_data=f"1.5"),
         InlineKeyboardButton("2 𝘴𝘰𝘢𝘵 🕟", callback_data=f"2"),
         InlineKeyboardButton("2.5 𝘴𝘰𝘢𝘵 🕞", callback_data=f"2.5")],
        [InlineKeyboardButton("3 𝘴𝘰𝘢𝘵 🕝", callback_data=f"3"),
         InlineKeyboardButton("3.5 𝘴𝘰𝘢𝘵 🕟", callback_data=f"3.5"),
         InlineKeyboardButton("4 𝘴𝘰𝘢𝘵 🕞", callback_data=f"4")],
    ]


def week_botn():
    return [
        [InlineKeyboardButton("Dushanba 1️⃣", callback_data=f"du"),
         InlineKeyboardButton("Seshanba 2️⃣", callback_data=f"se"),
         InlineKeyboardButton("Chorshanba 3️⃣", callback_data=f"cho")],
        [InlineKeyboardButton("Payshanba 4️⃣", callback_data=f"pay"),
         InlineKeyboardButton("Juma 5️⃣", callback_data=f"juma"),
         InlineKeyboardButton("Shanba 6️⃣", callback_data=f"shanba")],
        [InlineKeyboardButton("Yakshanba 7️⃣", callback_data=f"yak")]
    ]


def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")
    now = datetime.datetime.now()

    if data[0] == "30":
        vaqt.append(30)
        query.message.edit_text("30 minutda nima qilishingizni kiriting 🕝")

    if data[0] == "45":
        vaqt.append(45)
        query.message.edit_text("45 minutda nima qilishingizni kiriting 🕝")

    if data[0] == "1":
        vaqt.append(60)
        query.message.edit_text("1 soatda nima qilishingizni kiriting 🕝")

    if data[0] == "1.5":
        vaqt.append(90)
        query.message.edit_text("1:30 minutda nima qilishingizni kiriting 🕝")

    if data[0] == "2":
        vaqt.append(120)
        query.message.edit_text("2 soatda nima qilishingizni kiriting 🕝")

    if data[0] == "2.5":
        vaqt.append(150)
        query.message.edit_text("2:30 minutda nima qilishingizni kiriting 🕝")

    if data[0] == "3":
        vaqt.append(180)
        query.message.edit_text("3 soatda nima qilishingizni kiriting 🕝")

    if data[0] == "3.5":
        vaqt.append(210)
        query.message.edit_text("3:30 minutda nima qilishingizni kiriting 🕝")

    if data[0] == "4":
        vaqt.append(240)
        query.message.edit_text("4 soatda nima qilishingizni kiriting 🕝")

    if data[0] == "du":
        rejalar.append(1)

    if data[0] == "se":
        rejalar.append(2)

    if data[0] == "cho":
        rejalar.append(3)

    if data[0] == "pay":
        rejalar.append(4)

    if data[0] == "juma":
        rejalar.append(5)

    if data[0] == "shanba":
        rejalar.append(6)

    if data[0] == "yak":
        rejalar.append(7)


def message(update, context):
    msg = update.message.text
    reja.append(msg)
    now = datetime.datetime.now()
    if msg == "Week 🔅" and msg != "Day 🔆":
        update.message.reply_text("Hafta kunlarini tanlang 🔢 \nRejangizni kiriting ✅",
                                  reply_markup=InlineKeyboardMarkup(week_botn()))

        update.message.reply_text(
            f"Rejalaringizni kiriting",
            reply_markup=keyboard_btns("rejalar"))

    if msg == "Day 🔆":
        soat = now.hour
        reja.clear()
        update.message.reply_text(
            f'Hozir vaqt {soat}:{now.minute} 🕟\nshu vaqtdan boshlab qilinadigan kunlik\nrejalarni kiriting ✅',
            reply_markup=InlineKeyboardMarkup(kun_botn()))

    if len(msg) > 3 and not msg == "Day 🔆" and not msg == "SAVE ✅" and not msg == "Week 🔅" and not msg == "Restaran 🍽" \
            and not msg == "Sport 🏀" and not msg == "Sayr qilish 🚞" and not msg == "Dam olish 🎮" \
            and not msg == "Boshqa ishlar ❔":
        update.message.reply_text(
            f"Hozir vaqt {now.hour}:{now.minute} 🕟\nshu vaqtdan boshlab qilinadigan kunlik\nRejalarni kiriting ✅",
            reply_markup=InlineKeyboardMarkup(kun_botn()))
    days = datetime.date.today()
    week = days.isoweekday()
    for i in rejalar:
        if i == week:
            s = ""
            for j in reja:
                s = f"{s}\n{j}"
            update.message.reply_text(f"Bugungi rejalar Rejalar 🏆\n{s[5:][:-1]}\n")
            break

    if msg == "SAVE ✅":
        s = ""
        for i in reja:
            s = f"{s}\n{i}"
        update.message.reply_text(f"Rejalar 🏆\n{s[:-6]}")

        if vaqt[0] < 60:
            now = datetime.datetime.now()
            a = vaqt[0]
            b = now.minute + a
            if b > 60:
                s = b - 60
                minu = now.minute + s
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(minu):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}")
                        break
            else:
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b):
                        s = ''
                        for i in reja:
                            s = f'{s}\n{i}'
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break
        if len(vaqt) == 2:
            if vaqt[0] < 60:
                now = datetime.datetime.now()
                a = vaqt[0]
                b = now.minute + a
                if b > 60:
                    s = b - 60
                    minu = now.minute + s
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(minu):
                            s = ''
                            for i in reja:
                                s = f'{s}\n{i}'
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                else:
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b):
                            s = ''
                            for i in reja:
                                s = f'{s}\n{i}'
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                s = vaqt[0] + vaqt[1]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        s = ''
                        for i in reja:
                            s = f'{s}\n{i}'
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break
        if len(vaqt) == 3:
            if vaqt[0] < 60:
                now = datetime.datetime.now()
                a = vaqt[0]
                b = now.minute + a
                if b > 60:
                    s = b - 60
                    minu = now.minute + s
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(minu):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                else:
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                s = vaqt[0] + vaqt[1::]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break
        if len(vaqt) == 4:
            if vaqt[0] < 60:
                now = datetime.datetime.now()
                a = vaqt[0]
                b = now.minute + a
                if b > 60:
                    s = b - 60
                    minu = now.minute + s
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(minu):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                else:
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                s = vaqt[0] + vaqt[1]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break
        if len(vaqt) == 5:
            if vaqt[0] < 60:
                now = datetime.datetime.now()
                a = vaqt[0]
                b = now.minute + a
                if b > 60:
                    s = b - 60
                    minu = now.minute + s
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(minu):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                else:
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                s = vaqt[0] + vaqt[1]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

        if len(vaqt) == 6:
            if vaqt[0] < 60:
                now = datetime.datetime.now()
                a = vaqt[0]
                b = now.minute + a
                if b > 60:
                    s = b - 60
                    minu = now.minute + s
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(minu):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break
                else:
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                s = vaqt[0] + vaqt[1]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

                s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4] + vaqt[5]
                soat = s // 60
                minu = s % soat
                b = now.minute + minu
                d = now.hour + soat
                while True:
                    now = datetime.datetime.now()
                    if str(now.minute) == str(b) and str(now.hour) == str(d):
                        update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                        break

            if len(vaqt) == 7:
                if vaqt[0] < 60:
                    now = datetime.datetime.now()
                    a = vaqt[0]
                    b = now.minute + a
                    if b > 60:
                        s = b - 60
                        minu = now.minute + s
                        while True:
                            now = datetime.datetime.now()
                            if str(now.minute) == str(minu):
                                update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                                break
                    else:
                        while True:
                            now = datetime.datetime.now()
                            if str(now.minute) == str(b):
                                update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                                break
                    s = vaqt[0] + vaqt[1]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4] + vaqt[5]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4] + vaqt[5] + vaqt[6]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

            if len(vaqt) == 8:
                if vaqt[0] < 60:
                    now = datetime.datetime.now()
                    a = vaqt[0]
                    b = now.minute + a
                    if b > 60:
                        s = b - 60
                        minu = now.minute + s
                        while True:
                            now = datetime.datetime.now()
                            if str(now.minute) == str(minu):
                                update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                                break
                    else:
                        while True:
                            now = datetime.datetime.now()
                            if str(now.minute) == str(b):
                                update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                                break
                    s = vaqt[0] + vaqt[1]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4] + vaqt[5]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4] + vaqt[5] + vaqt[6]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break

                    s = vaqt[0] + vaqt[1] + vaqt[2] + vaqt[3] + vaqt[4] + vaqt[5] + vaqt[6] + vaqt[7]
                    soat = s // 60
                    minu = s % soat
                    b = now.minute + minu
                    d = now.hour + soat
                    while True:
                        now = datetime.datetime.now()
                        if str(now.minute) == str(b) and str(now.hour) == str(d):
                            update.message.reply_text(f"Vaqt Tugadi 🔔\n{s[0:][:-6]}\n")
                            break


def start(update, context):
    rejalar.clear()
    reja.clear()
    vaqt.clear()
    user = update.message.from_user
    update.message.reply_text(
        f"""Salom {user.first_name} 🖐🏼\nBu botga qilishingiz kerak bolgan\nishlarni ketma-ketlik bilan kiriting ✅""",
        reply_markup=keyboard_btns("reja"))


def main():
    Token = "2126323168:AAF1yS1sC1hxUTYvKGB54M2xuXL5mtYzpZ8"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
