# MIT License
#
# Copyright (c) 2023 HELL-BOY-OP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Callable

from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, Message

from HellMusic import SUDOERS, app

from .active import is_active_chat


def admin_check(func: Callable) -> Callable:
    async def non_admin(_, message: Message):
        if not await is_active_chat(message.chat.id):
            return await message.reply_text("вσт ιѕи'т ѕтяєαмιиg σи νι∂єσ¢нαт.")

        if message.from_user.id in SUDOERS:
            return await func(_, message)

        check = await app.get_chat_member(message.chat.id, message.from_user.id)
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply_text(
                "» уσυ'яє иσт αи α∂мιи ∂αяℓιиg, ρℓєαѕє ѕтαу ιи уσυя ℓιмιтѕ."
            )

        admin = (
            await app.get_chat_member(message.chat.id, message.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, message)
        else:
            return await message.reply_text(
                "» уσυ ∂σи'т нανє ρєямιѕѕισи тσ мαиαgє νι∂єσ¢нαт, ρℓєαѕє ѕтαу ιи уσυя ℓιмιтѕ."
            )

    return non_admin


def admin_check_cb(func: Callable) -> Callable:
    async def cb_non_admin(_, query: CallbackQuery):
        if not await is_active_chat(query.message.chat.id):
            return await query.answer(
                "вσт ιѕи'ᴛ ѕтяєαмιиg σи νι∂єσ¢нαт.", show_alert=True
            )

        if query.from_user.id in SUDOERS:
            return await func(_, query)

        try:
            check = await app.get_chat_member(query.message.chat.id, query.from_user.id)
        except:
            return
        if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            return await query.answer(
                "» уσυ'яє иσт αи α∂мιи ∂αяℓιиg, ρℓєαѕє ѕтαу ιи уσυя ℓιмιтєѕ.",
                show_alert=True,
            )

        admin = (
            await app.get_chat_member(query.message.chat.id, query.from_user.id)
        ).privileges
        if admin.can_manage_video_chats:
            return await func(_, query)
        else:
            return await query.answer(
                "» уσυ ∂σит'ᴛ нανє ρєямιѕѕισи тσ мαиαgє νι∂єσ¢нαт, ρℓєαѕє ѕтαу ιи уσυя ℓíмιтѕ.",
                show_alert=True,
            )

    return cb_non_admin
