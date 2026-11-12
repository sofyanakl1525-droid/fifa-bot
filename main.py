import telebot
from telebot import types
from urllib.parse import quote
import os, json

TOKEN = os.environ.get("8853805372:AAGB1r_hZ9Xofv3MDkzoOr5cfgZ_crLTj94")
bot = telebot.TeleBot(TOKEN)

# ===== الروابط =====
MY_NUMBER = "201553353379"
WHATSAPP_CHANNEL = "https://whatsapp.com/channel/0029Vb96B7r0G0XngffxQx2O"
FACEBOOK = "https://www.facebook.com/share/1KKhCVoXTn/"
TIKTOK = "https://www.tiktok.com/@sofyan.akl8?_r=1&_t=ZS-9BJWp60uIQp"

# ===== رسالة الواتساب =====
msg = "السلام عليكم 👋⚽\nعايز اشترك في الدوري FIFA Champions League 🔥🏆\n\nبرجاء ارسال البيانات الاتيه 👇\n📌 الاسم الحقيقي :\n📌 الاي دي :\n📌 الاوفر :\n📌 الاسم باللعبة :"
WHATSAPP_LINK = f"https://wa.me/{MY_NUMBER}?text={quote(msg)}"

LEAGUE_PASSWORD = "SM7"

FILE = "players.json"
if not os.path.exists(FILE):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump({}, f, ensure_ascii=False)

def load_players():
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def save_players(data):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

TOMORROW_MATCHES = "لسه مفيش ماتشات متحددة، استنى اعلان الادمن"
LAST_MATCH = "لسه مفيش مسابقات اتلعبت"

# ===== 1 - الروابط =====
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("1️⃣ قناة الواتساب - Follow the FIFA Champions League 27 ⚡", url=WHATSAPP_CHANNEL))
    markup.add(types.InlineKeyboardButton("2️⃣ صفحة الفيس بوك", url=FACEBOOK))
    markup.add(types.InlineKeyboardButton("3️⃣ صفحة التيك توك - @sofyan.akl8", url=TIKTOK))
    markup.add(types.InlineKeyboardButton("➡️ معلومات الدوري 🏆", callback_data="info"))
    bot.send_message(message.chat.id,
        "أهلا بيك في بوت FIFA Champions League ⚡🔥27\n\n"
        "👋 ده بوت الدوري بتاعنا، هنا هتعرف كل حاجة عن الدوري، مين هيلعب، وترتيبك كام، وكسبت كام وخسرت كام.\n\n"
        "📌 أول خطوة:\n"
        "اشترك في الـ 3 روابط اللي فوق دول 👆\n"
        "1- قناة الواتساب Follow the FIFA Champions League 27 ⚡ عشان توصلك كل الأخبار\n"
        "2- صفحة الفيس بوك\n"
        "3- صفحة التيك توك @sofyan.akl8\n\n"
        "بعد ما تشترك، دوس على زرار ➡️ معلومات الدوري اللي تحت.",
        reply_markup=markup)

# ===== 2 - معلومات الدوري =====
@bot.callback_query_handler(func=lambda c: c.data == "info")
def info(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("✅ مشترك في الدوري", callback_data="i_sub"))
    markup.add(types.InlineKeyboardButton("❌ غير مشترك - عايز اشترك", callback_data="not_sub"))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_start"))
    bot.edit_message_text(
        "📋 معلومات الدوري:\n\n"
        "🏆 اسم الدوري: FIFA Champions League 27\n"
        "⚽ اللعبة: FC Mobile\n"
        "👥 عدد الفرق: 16 فريق\n"
        "🏅 نظام الدوري: كل واحد بيلعب ماتشات وبيجمع نقط\n"
        "🎁 الجايزة: المركز الأول بيكسب جايزة\n"
        "📅 الماتشات: كل يوم في معاد ثابت هنعلنه\n\n"
        "❓ انت دلوقتي ايه؟\n"
        "لو انت اشتركت معانا قبل كده واسمك متسجل، دوس ✅ مشترك في الدوري\n"
        "لو لسه جديد وعايز تشترك، دوس ❌ غير مشترك",
        call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data == "back_start")
def back_start(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("1️⃣ قناة الواتساب - Follow the FIFA Champions League 27 ⚡", url=WHATSAPP_CHANNEL))
    markup.add(types.InlineKeyboardButton("2️⃣ صفحة الفيس بوك", url=FACEBOOK))
    markup.add(types.InlineKeyboardButton("3️⃣ صفحة التيك توك - @sofyan.akl8", url=TIKTOK))
    markup.add(types.InlineKeyboardButton("➡️ معلومات الدوري 🏆", callback_data="info"))
    bot.edit_message_text("أهلا بيك في FIFA Champions League ⚡🔥27\n\nاشترك في الـ 3 روابط اللي فوق 👆 وبعدين دوس معلومات الدوري", call.message.chat.id, call.message.message_id, reply_markup=markup)

# ===== 3 - غير مشترك =====
@bot.callback_query_handler(func=lambda c: c.data == "not_sub")
def not_sub(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📩 عايز اشترك - دوس على اللينك", url=WHATSAPP_LINK))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="info"))
    bot.edit_message_text(
        "❌ انت لسه مش مشترك، مفيش مشكلة، هنشتركك دلوقتي 👇\n\n"
        "📌 اعمل ايه؟\n"
        "1- دوس على زرار 📩 عايز اشترك اللي تحت\n"
        "2- هيوديك على الواتساب بتاع الادمن على طول\n"
        "3- هتلاقي رسالة جاهزة مكتوب فيها:\n"
        "السلام عليكم 👋⚽\n"
        "عايز اشترك في الدوري FIFA Champions League 🔥🏆\n"
        "برجاء ارسال البيانات الاتيه 👇\n"
        "📌 الاسم الحقيقي :\n"
        "📌 الاي دي :\n"
        "📌 الاوفر :\n"
        "📌 الاسم باللعبة :\n\n"
        "املاهم وابعتهم.\n\n"
        "بعد ما تبعت، الادمن هيرد عليك وهيبعتلك كلمة السر SM7 عشان تدخل الدوري.",
        call.message.chat.id, call.message.message_id, reply_markup=markup)

# ===== 4 - مشترك -> كلمة السر =====
@bot.callback_query_handler(func=lambda c: c.data == "i_sub")
def i_sub(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="info"))
    bot.edit_message_text(
        "✅ تمام، انت مشترك، نورتنا 🔥\n\n"
        "📌 عشان نتأكد انك انت مش حد غريب، اكتب كلمة السر هنا في الشات 👇\n\n"
        "❓ كلمة السر دي ايه؟\n"
        "دي كلمة الادمن بيبعتها ليك على الواتساب بعد ما تشترك.\n"
        "اكتبها زي ما هي بالظبط وابعتهالي.",
        call.message.chat.id, call.message.message_id, reply_markup=markup)
    bot.register_next_step_handler(call.message, check_password)

def check_password(message):
    if message.text.strip() != LEAGUE_PASSWORD:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📩 كلم الادمن على الواتساب", url=WHATSAPP_LINK))
        markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="info"))
        bot.send_message(message.chat.id,
            "❌ كلمة السر غلط!\n\n"
            "📌 اتأكد انك كاتبها صح: SM7\n"
            "لو انت مشترك فعلا ولسه مجتلكش كلمة السر، او نسيتها،\n"
            "دوس على زرار 📩 كلم الادمن على الواتساب اللي تحت،\n"
            "وهيفتحلك الواتساب برسالة:\n"
            "السلام عليكم 👋⚽\n"
            "عايز اشترك في الدوري FIFA Champions League 🔥🏆\n"
            "برجاء ارسال البيانات الاتيه 👇\n"
            "📌 الاسم الحقيقي :\n"
            "📌 الاي دي :\n"
            "ابعتها للادمن وهيبعتلك كلمة السر الصح.",
            reply_markup=markup)
        return

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⚽ معلومات مسابقة الدوري", callback_data="matches"))
    markup.add(types.InlineKeyboardButton("🏆 آخر تحديث لتوقيت النقط", callback_data="rank"))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="info"))
    bot.send_message(message.chat.id,
        "✅ كلمة السر صح، نورت الدوري 🔥\n\n"
        "🏆 انت دلوقتي جوه صفحة الدوري\n\n"
        "📌 هنا هتلاقي حاجتين:\n"
        "1- ⚽ معلومات مسابقة الدوري: مين هيلعب بكره، وفزنا كام وخسرنا كام\n"
        "2- 🏆 آخر تحديث لتوقيت النقط: ترتيبك كام ونقطك كام\n\n"
        "اختار واحد من تحت 👇",
        reply_markup=markup)

# ===== 5 - معلومات مسابقة الدوري =====
@bot.callback_query_handler(func=lambda c: c.data == "matches")
def matches(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("👥 من سيشارك في مسابقة الدوري", callback_data="who_play"))
    markup.add(types.InlineKeyboardButton("📊 عدد المسابقات اللي فوزنا بيها واللي خسرناها", callback_data="stats"))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_league"))
    bot.edit_message_text(
        "⚽ معلومات مسابقة الدوري 🏆\n\n"
        "📌 الصفحة دي فيها كل حاجة عن المسابقة:\n"
        "👥 لو عايز تعرف مين هيلعب بكره وامتى، دوس على أول زرار\n"
        "📊 لو عايز تعرف احنا فوزنا كام مسابقة وخسرنا كام، دوس على تاني زرار\n\n"
        "اختار من تحت 👇",
        call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda c: c.data == "back_league")
def back_league(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⚽ معلومات مسابقة الدوري", callback_data="matches"))
    markup.add(types.InlineKeyboardButton("🏆 آخر تحديث لتوقيت النقط", callback_data="rank"))
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="info"))
    bot.edit_message_text("🏆 صفحة الدوري\n\nاختار من تحت 👇", call.message.chat.id, call.message.message_id, reply_markup=markup)

# ===== 6 - من سيشارك =====
@bot.callback_query_handler(func=lambda c: c.data == "who_play")
def who_play(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="matches"))
    bot.edit_message_text(
        f"👥 من سيشارك في مسابقة الدوري:\n\n"
        f"{TOMORROW_MATCHES}\n\n"
        f"📌 يعني ايه الكلام ده؟\n"
        f"دي الماتشات اللي هتتلعب بكره، كل واحد عارف هيلعب ضد مين وامتى.\n"
        f"لو اسمك موجود هنا، جهز نفسك وجهز فريقك.\n\n"
        f"🏆 {LAST_MATCH}\n"
        f"دي نتيجة آخر مسابقة لعبناها.",
        call.message.chat.id, call.message.message_id, reply_markup=markup)

# ===== 7 - عدد المسابقات =====
@bot.callback_query_handler(func=lambda c: c.data == "stats")
def stats(call):
    players = load_players()
    total_wins = sum(p['wins'] for p in players.values())
    total_losses = sum(p['losses'] for p in players.values())
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="matches"))
    bot.edit_message_text(
        f"📊 عدد المسابقات:\n\n"
        f"✅ اللي فوزنا بيها: {total_wins} مسابقة\n"
        f"❌ اللي خسرناها: {total_losses} مسابقة\n\n"
        f"📌 يعني ايه؟\n"
        f"دي احصائيات الدوري كله لحد دلوقتي.\n"
        f"كل ما نفوز اكتر، نقطنا بتزيد وترتيبنا بيعلى.",
        call.message.chat.id, call.message.message_id, reply_markup=markup)

# ===== 8 - آخر تحديث لتوقيت النقط =====
@bot.callback_query_handler(func=lambda c: c.data == "rank")
def rank(call):
    players = load_players()
    if not players:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_league"))
        bot.edit_message_text("🏆 آخر تحديث لتوقيت النقط:\n\nلسه مفيش لعيبة متسجلين، الادمن لسه هيضيفهم.", call.message.chat.id, call.message.message_id, reply_markup=markup)
        return
    sorted_players = sorted(players.values(), key=lambda x: x['points'], reverse=True)
    text = "🏆 آخر تحديث لتوقيت النقط:\n\n"
    text += "📌 ده ترتيب الدوري لحد دلوقتي، اللي فوق هو الأول.\n"
    text += "كل فوز بيزود نقطك، وكل خسارة بتقللها.\n\n"
    for i, pl in enumerate(sorted_players, 1):
        text += f"{i}. {pl['name']} | {pl['game_name']} | أوفر {pl['over']} | {pl['points']} نقطة | مركز {i}\n"
    text += "\n🔄 الترتيب ده بيتحدث كل ما نخلص مسابقة."
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔙 رجوع", callback_data="back_league"))
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=markup)

# ===== انت كأدمن تضيف لاعب =====
# /add سفيان 130 sofyan 20 6 1
@bot.message_handler(commands=['add'])
def add_player(message):
    try:
        p = message.text.split()
        name, over, game_name = p[1], int(p[2]), p[3]
        points, wins, losses = int(p[4]), int(p[5]), int(p[6])
        players = load_players()
        players[game_name] = {"name": name, "over": over, "game_name": game_name, "points": points, "wins": wins, "losses": losses}
        save_players(players)
        bot.send_message(message.chat.id, f"✅ تم اضافة {name} | {game_name} | {points} نقطة")
    except:
        bot.send_message(message.chat.id, "اكتب كده:\n/add سفيان 130 sofyan 20 6 1")

print("البوت شغال...")
bot.infinity_polling()
