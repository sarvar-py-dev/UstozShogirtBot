from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.i18n import gettext as _, lazy_gettext as __

from config import ADMIN
from routers.user import print_state

send_router = Router()


@send_router.callback_query(F.data.endswith('cancel'))
async def cancel_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(_('Qabul qilinmadi'))
    await state.clear()


@send_router.callback_query(F.data.endswith('confirm'))
async def confirm_handler(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    msg = print_state(data)
    ikb = InlineKeyboardBuilder()
    ikb.add(InlineKeyboardButton(text='Channelga', callback_data='channelga'),
            InlineKeyboardButton(text='Xato', callback_data='xato'))
    await callback.message.edit_reply_markup()
    await bot.send_message(chat_id=ADMIN, text=msg, reply_markup=ikb.as_markup())
    await callback.message.answer(_('Adminga tashladik bu kurib chiqilib kegin channelga tashlanadi'))
