from aiogram.types import KeyboardButton
from aiogram.utils.i18n import gettext as _, lazy_gettext as __
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_keyboard_btn(**kwargs):
    rkb = ReplyKeyboardBuilder()
    rkb.add(KeyboardButton(text=_('Sherik kerak', **kwargs)), KeyboardButton(text=_('Ish joyi kerak', **kwargs)),
            KeyboardButton(text=_('Hodim kerak', **kwargs)), KeyboardButton(text=_('Ustoz kerak', **kwargs)))
    rkb.adjust(2, repeat=True)
    rkb.row(KeyboardButton(text=_('Shogird kerak', **kwargs)))
    rkb.row(KeyboardButton(text=_('🌐 Tilni almashtirish', **kwargs)))
    return rkb
