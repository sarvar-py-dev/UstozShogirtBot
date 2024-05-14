from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, InlineKeyboardButton, CallbackQuery, BotCommand
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.keyboards import main_keyboard_btn
from state.state import States

handler_router = Router()


@handler_router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(_('''<b>Assalom alaykum {name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!</b>

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!''').format(name=message.from_user.full_name),
                         reply_markup=main_keyboard_btn().as_markup(resize_keyboard=True))


@handler_router.message(Command(commands='help'))
async def help_command(message: Message):
    await message.answer(_('''UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. 

Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. 

E'lon berish: @Ustoz_Shogird_py_Bot

Admin @sarvar_py_dev'''))


@handler_router.message(F.text.endswith('kerak') | F.text.endswith('нужен'))
async def kerak_command(message: Message, state: FSMContext):
    await message.answer(_('''<b>{category} topish uchun ariza berish</b>

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.''').format(
        category=' '.join(message.text.split()[:-1])))
    if message.text.startswith(_('Hodim')):
        await message.answer(_('🎓 Idora nomi?'), reply_markup=ReplyKeyboardRemove())
        await state.set_state(States.idora)
    else:
        await message.answer(_('<b>Ism, familiyangizni kiriting?</b>'))
        await state.set_state(States.full_name)
    await state.update_data(category=' '.join(message.text.split()[:-1]))


@handler_router.message(F.text == __('🌐 Tilni almashtirish'))
async def change_language(message: Message):
    ikb = InlineKeyboardBuilder()
    ikb.row(InlineKeyboardButton(text='Uz🇺🇿', callback_data='lang_uz'),
            InlineKeyboardButton(text='Ru🇷🇺', callback_data='lang_ru'))
    await message.answer(_('Tilni tanlang: '), reply_markup=ikb.as_markup(resize_keyboard=True))


@handler_router.callback_query(F.data.startswith('lang_'))
async def languages(callback: CallbackQuery, state: FSMContext, bot: Bot):
    lang_code = callback.data.split('lang_')[-1]
    await state.update_data(locale=lang_code)
    if lang_code == 'uz':
        lang = _('Uzbek', locale=lang_code)
    else:
        lang = _('Rus', locale=lang_code)
    await callback.answer(_('{lang} tili tanlandi', locale=lang_code).format(lang=lang))
    command_list = [
        BotCommand(command='start', description=_('Botni boshlash', locale=lang_code)),
        BotCommand(command='help', description=_('Yordam kerakmi', locale=lang_code)),
    ]
    await bot.set_my_commands(command_list)
    rkb = main_keyboard_btn(locale=lang_code)
    msg = _('Assalomu alaykum! Tanlang.', locale=lang_code)
    await callback.message.delete()
    await callback.message.answer(text=msg, reply_markup=rkb.as_markup(resize_keyboard=True))
