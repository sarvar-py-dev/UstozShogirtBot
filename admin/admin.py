from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from config import CHANNEL

admin_router = Router()


@admin_router.callback_query(F.data.startswith('channelga'))
async def channelga_handler(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(CHANNEL, callback.message.text)
    await callback.message.edit_reply_markup()
    await callback.answer('Yuborildi', show_alert=True)
    await state.clear()


@admin_router.callback_query(F.data.startswith('xato'))
async def xato_handler(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.clear()
