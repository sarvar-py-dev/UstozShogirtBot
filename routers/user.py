from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from keyboards.keyboards import main_keyboard_btn
from state.state import States

user_router = Router()


def print_state(data):
    msg = f'<b>{data["category"]} kerak: </b>\n\n'
    if data['category'] == "Hodim":
        msg += f"🏢 Idora: {data['idora']}\n📚 Texnologiya: <b>{data['texnology']}</b>\n🇺🇿 Telegram: @{data['telegram']}\t\t\n📞 Aloqa: {data['aloqa']}\n🌐 Hudud: <b>{data['hudud']}</b>\n✍️ Mas'ul: <b>{data['masul']}</b>\n🕰 Murojaat qilish vaqti: {data['murojat_time']}\n🕰 Ish vaqti: {data['ish_vaqti']}\n💰 Maosh: {data['maosh']}\n‼️ Qo`shimcha: {data['qoshimcha']}\n\n#{data['category'].lower()}"
    else:
        if data['category'] == 'Sherik':
            msg += f'🏅 Sherik: <b>{data["full_name"]}</b>\n'
        elif data['category'] == "Ish joyi":
            msg += f"👨‍💼 Xodim: {data['full_name']}\n🕑 Yosh: {data['yosh']}\n"
        else:
            msg += f"🎓 {data['category']}: {data['full_name']}\n🌐 Yosh: {data['yosh']}\n"
        msg += f'📚 Texnologiya: <b>{data["texnology"]}</b>\n🇺🇿 Telegram: @{data["telegram"]}\n📞 Aloqa: {data.get("aloqa")}\n🌐 Hudud: <b>{data["hudud"]}</b>\n💰 Narxi: {data["narxi"]}\n👨🏻‍💻 Kasbi: {data["kasbi"]}\n🕰 Murojaat qilish vaqti: {data["murojat_time"]}\n🔎 Maqsad: {data["maqsad"]}\n\n#{data["category"].lower()}'
    return msg


async def print_data(data, message: Message):
    ikb = InlineKeyboardBuilder()
    ikb.add(InlineKeyboardButton(text=_('✅ Ha'), callback_data='confirm'),
            InlineKeyboardButton(text=_("❌ Yo'q"), callback_data='cancel'))
    await message.answer(print_state(data), reply_markup=main_keyboard_btn().as_markup(resize_keyboard=True))
    await message.answer(_("Barcha ma'lumotlar to'g'rimi?"), reply_markup=ikb.as_markup())


async def texnolgyga(message, state):
    await message.answer(_('''📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

<i>Java, C++, C#</i>'''))

    await state.set_state(States.texnology)


async def to_murojat_time(message, state):
    await message.answer(_('''🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00'''))
    await state.set_state(States.murojat_time)


@user_router.message(States.idora)
async def idora(message: Message, state: FSMContext):
    await state.update_data(idora=message.text)
    await texnolgyga(message, state)


@user_router.message(States.full_name)
async def first_last_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    if States.category == __('Sherik'):
        await texnolgyga(message, state)
    else:
        await message.answer(_('''🕑 Yosh: 

Yoshingizni kiriting?
Masalan: 19'''))
        await state.set_state(States.yosh)


@user_router.message(States.yosh)
async def yosh(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await texnolgyga(message, state)


@user_router.message(States.texnology)
async def texno(message: Message, state: FSMContext):
    await state.update_data(texnology=message.text, telegram=message.from_user.username)
    await state.set_state(States.aloqa)
    await message.answer(_('''📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67'''))


@user_router.message(States.aloqa)
async def aloqa(message: Message, state: FSMContext):
    if not message.text.isalpha():
        await state.update_data(aloqa=message.text)
    await message.answer(_('''🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.'''))
    await state.set_state(States.hudud)


@user_router.message(States.hudud)
async def hudud(message: Message, state: FSMContext):
    await state.update_data(hudud=message.text)
    if States.category == __('Hodim'):
        await message.answer(_("✍️Mas'ul ism sharifi?"))
        await state.set_state(States.masul)
    else:
        await message.answer(_('''💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?'''))
        await state.set_state(States.narxi)


@user_router.message(States.masul)
async def masul(message: Message, state: FSMContext):
    await state.update_data(masul=message.text)
    await to_murojat_time(message, state)


@user_router.message(States.narxi)
async def narxi(message: Message, state: FSMContext):
    await state.update_data(narxi=message.text)
    await message.answer(_('''👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba'''))
    await state.set_state(States.kasbi)


@user_router.message(States.kasbi)
async def kasbi(message: Message, state: FSMContext):
    await state.update_data(kasbi=message.text)
    await to_murojat_time(message, state)


@user_router.message(States.murojat_time)
async def murojat_time(message: Message, state: FSMContext):
    await state.update_data(murojat_time=message.text)
    if States.category == __('Hodim'):
        await message.answer(_('🕰 Ish vaqtini kiriting?'))
        await state.set_state(States.ish_vaqti)
    else:
        await message.answer(_('''🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.'''))
        await state.set_state(States.maqsad)


@user_router.message(States.ish_vaqti)
async def ish_vaqti(message: Message, state: FSMContext):
    await state.update_data(ish_vaqti=message.text)
    await message.answer(_('‼️ Qo`shimcha ma`lumotlar?'))
    await state.set_state(States.qoshimcha)


@user_router.message(States.qoshimcha)
async def qoshimcha(message: Message, state: FSMContext):
    await state.update_data(qoshimcha=message.text)
    data = await state.get_data()
    await print_data(data, message)


@user_router.message(States.maqsad)
async def maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    data = await state.get_data()
    await print_data(data, message)


@user_router.message()
async def any(message: Message):
    await message.answer(_("/start so`zini bosing. E'lon berish qaytadan boshlanadi️"))
