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

from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from pytgcalls.types import AudioPiped, HighQualityAudio

from HellMusic import (
    ASS_ID,
    ASS_NAME,
    BOT_ID,
    BOT_MENTION,
    BOT_USERNAME,
    LOGGER,
    app,
    fallendb,
    pytgcalls,
)
from HellMusic.Helpers import (
    _clear_,
    admin_check_cb,
    gen_thumb,
    is_streaming,
    stream_off,
    stream_on,
)
from HellMusic.Helpers.dossier import *
from HellMusic.Helpers.inline import (
    buttons,
    close_key,
    help_back,
    helpmenu,
    pm_buttons,
)


@app.on_callback_query(filters.regex("forceclose"))
async def close_(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "» ιт'ℓℓ вє вєттєя ιf уσυ ѕтαу ιи уσυя ℓιмιт ∂αяℓιиg.", show_alert=True
            )
        except:
            return
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex("close"))
async def forceclose_command(_, CallbackQuery):
    try:
        await CallbackQuery.message.delete()
    except:
        return
    try:
        await CallbackQuery.answer()
    except:
        pass


@app.on_callback_query(filters.regex(pattern=r"^(resume_cb|pause_cb|skip_cb|end_cb)$"))
@admin_check_cb
async def admin_cbs(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        pass

    data = query.matches[0].group(1)

    if data == "resume_cb":
        if await is_streaming(query.message.chat.id):
            return await query.answer(
                "∂ι∂ уσυ яємємвєя тнαт уσυ ραυѕє тнє ѕтяєαм ?", show_alert=True
            )
        await stream_on(query.message.chat.id)
        await pytgcalls.resume_stream(query.message.chat.id)
        await query.message.reply_text(
            text=f"➻ ѕтяєαм яєѕυмє∂ 💫\n│ \n└ʙʏ : {query.from_user.mention} 🤨",
            reply_markup=close_key,
        )

    elif data == "pause_cb":
        if not await is_streaming(query.message.chat.id):
            return await query.answer(
                "∂ι∂ уσυ яємємвєя тнαт уσυ яєѕυмє∂ тнєя ѕтяєαм ?", show_alert=True
            )
        await stream_off(query.message.chat.id)
        await pytgcalls.pause_stream(query.message.chat.id)
        await query.message.reply_text(
            text=f"➻ ѕтяєαм ραυѕє∂ 🥺\n│ \n└ʙʏ : {query.from_user.mention} 🤨",
            reply_markup=close_key,
        )

    elif data == "end_cb":
        try:
            await _clear_(query.message.chat.id)
            await pytgcalls.leave_group_call(query.message.chat.id)
        except:
            pass
        await query.message.reply_text(
            text=f"➻ ѕтяєαм єи∂є∂/ѕтσρρє∂ ❄\n│ \n└ву : {query.from_user.mention} 😒",
            reply_markup=close_key,
        )
        await query.message.delete()

    elif data == "skip_cb":
        get = helldb.get(query.message.chat.id)
        if not get:
            try:
                await _clear_(query.message.chat.id)
                await pytgcalls.leave_group_call(query.message.chat.id)
                await query.message.reply_text(
                    text=f"➻ ѕтяєαм ѕкιρρє∂ 🥺\n│ \n└ву : {query.from_user.mention} 😤\n\n**» иσ мσяє qυєυє∂ тяα¢кѕ ιи** {query.message.chat.title}, **ℓєανιиg νι∂єσ¢нαт.**",
                    reply_markup=close_key,
                )
                return await query.message.delete()
            except:
                return
        else:
            title = get[0]["title"]
            duration = get[0]["duration"]
            videoid = get[0]["videoid"]
            file_path = get[0]["file_path"]
            req_by = get[0]["req"]
            user_id = get[0]["user_id"]
            get.pop(0)

            stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
            try:
                await pytgcalls.change_stream(
                    query.message.chat.id,
                    stream,
                )
            except Exception as ex:
                LOGGER.error(ex)
                await _clear_(query.message.chat.id)
                return await pytgcalls.leave_group_call(query.message.chat.id)

            img = await gen_thumb(videoid, user_id)
            await query.edit_message_text(
                text=f"➻ ѕтяєαм ѕкιρρє∂ 🥺\n│ \n└ʙʏ : {query.from_user.mention} 😤",
                reply_markup=close_key,
            )
            return await query.message.reply_photo(
                photo=img,
                caption=f"**➻ ѕтαятє∂ ѕтяєαмιиg**\n\n‣ **тιтℓє :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\n‣ **∂υяαтισи :** `{duration}` мιиυтєѕ\n‣ **яєqυєѕтє∂ ву :** {req_by}",
                reply_markup=buttons,
            )


@app.on_callback_query(filters.regex("unban_ass"))
async def unban_ass(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat_id, user_id = callback_request.split("|")
    umm = (await app.get_chat_member(int(chat_id), BOT_ID)).privileges
    if umm.can_restrict_members:
        try:
            await app.unban_chat_member(int(chat_id), ASS_ID)
        except:
            return await CallbackQuery.answer(
                "» fαιℓє∂ тσ υивαи αѕѕιѕтαит.",
                show_alert=True,
            )
        return await CallbackQuery.edit_message_text(
            f"➻ {ASS_NAME} ѕυ¢¢єѕѕfυℓℓу υивαииє∂ ву {CallbackQuery.from_user.mention}.\n\nтяу ρℓαуιиg иσω..."
        )
    else:
        return await CallbackQuery.answer(
            "» ι ∂σи'т нανє ρєямιѕѕισи тσ υивαи υѕєяѕ ιи тнιѕ ¢нαт.",
            show_alert=True,
        )


@app.on_callback_query(filters.regex("hell_help"))
async def help_menu(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        pass

    try:
        await query.edit_message_text(
            text=f"๏ нєу {query.from_user.first_name}, 🥀\n\nρℓєαѕє ¢ℓι¢к σи тнє вυттσи вєℓσω fσя ωнι¢н уσυ ωαииα gєт нєℓρ.",
            reply_markup=InlineKeyboardMarkup(helpmenu),
        )
    except Exception as e:
        LOGGER.error(e)
        return


@app.on_callback_query(filters.regex("hell_cb"))
async def open_hmenu(_, query: CallbackQuery):
    callback_data = query.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(help_back)

    try:
        await query.answer()
    except:
        pass

    if cb == "help":
        await query.edit_message_text(HELP_TEXT, reply_markup=keyboard)
    elif cb == "sudo":
        await query.edit_message_text(HELP_SUDO, reply_markup=keyboard)
    elif cb == "owner":
        await query.edit_message_text(HELP_DEV, reply_markup=keyboard)


@app.on_callback_query(filters.regex("hell_home"))
async def home_fallen(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        pass
    try:
        await query.edit_message_text(
            text=PM_START_TEXT.format(
                query.from_user.first_name,
                BOT_MENTION,
            ),
            reply_markup=InlineKeyboardMarkup(pm_buttons),
        )
    except:
        pass
