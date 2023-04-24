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
from pyrogram.types import Message

from HellMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2


@app.on_message(filters.command(["asspfp", "setpfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("» ¢нαиgιиg αѕѕιѕтαит ρяσfιℓє ρι¢...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"» {ASS_MENTION} ρяσfιℓє ρι¢ ¢нαиgє∂ ѕυ¢¢єѕѕfυℓℓу."
            )
        except:
            return await fuk.edit_text("» fαιℓє∂ тσ ¢нαиgє αѕѕιѕтαит ρяσfιℓє ρι¢.")
    else:
        await message.reply_text(
            "» яєρℓу тσ α ρнσтσ fσя ¢нαиgιиg αѕѕιѕтαит ρяσfιℓє ρι¢."
        )


@app.on_message(filters.command(["delpfp", "delasspfp"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "» ѕυ¢¢єѕѕfυℓℓу ∂єℓєтє∂ αѕѕιѕтαит's ρяσfιℓє ρι¢."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("» fαιℓє∂ тσ ∂єℓєтє αѕѕιѕтαит'ѕ ρяσfιℓє ρι¢.")


@app.on_message(filters.command(["assbio", "setbio"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"» {ASS_MENTION} вισ ¢нαиgє∂ ѕυ¢¢єѕѕfυℓℓу."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"» {ASS_MENTION} вισ ¢нαиgє∂ ѕυ¢¢єѕѕfυℓℓу.")
    else:
        return await message.reply_text(
            "» яєρℓу тσ α мєѕѕαgє σя gινє ѕσмє тєχт тσ ѕєт ιт αѕ αѕѕιѕтαит'ѕ вισ."
        )


@app.on_message(filters.command(["assname", "setname"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"» {ASS_MENTION} иαмє ¢нαиgє∂ ѕυ¢¢єѕѕfυℓℓу."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"» {ASS_MENTION} иαмє ¢нαмgє∂ ѕυ¢¢єѕѕfυℓℓу.")
    else:
        return await message.reply_text(
            "» яєρℓу тσ α мєѕѕαgє σя gινє ѕσмє тєχт тσ ѕєт ιт αѕ αѕѕιѕтαит иєω иαмє."
        )
