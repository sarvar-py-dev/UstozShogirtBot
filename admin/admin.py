from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from config import CHANNEL
from routers.user import print_state

admin_router = Router()


@admin_router.callback_query(F.data.startswith('channelga'))
async def channelga_handler(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(CHANNEL, print_state(await state.get_data()))
    await callback.message.edit_reply_markup()
    await callback.answer('Yuborildi', show_alert=True)
    await state.clear()


@admin_router.callback_query(F.data.startswith('xato'))
async def xato_handler(callback: CallbackQuery):
    await callback.message.delete()
