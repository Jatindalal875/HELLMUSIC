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
from pyrogram.enums import ChatType
from pyrogram.types import Message

import config
from HellMusic import BOT_NAME, app


@app.on_message(
    filters.command(["config", "variables"]) & filters.user(config.OWNER_ID)
)
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(config.OWNER_ID),
            text=f"""<u>**{BOT_NAME} ¢σиfιg ναяιαвℓєѕ :**</u>

**αρι_ι∂ :** `{config.API_ID}`
**αρι_нαѕн :** `{config.API_HASH}`

**вσт_тσкєи :** `{config.BOT_TOKEN}`
**∂υяαтισи_ℓιмιт :** `{config.DURATION_LIMIT}`

**σωиєя_ι∂ :** `{config.OWNER_ID}`
**ѕυ∂σ_υѕєя :** `{config.SUDO_USERS}`

**ριиg_ιмg :** `{config.PING_IMG}`
**ѕтαят_ιмg :** `{config.START_IMG}`
**ѕυρρσят_¢нαт :** `{config.SUPPORT_CHAT}`

**ѕєѕѕισи :** `{config.SESSION}`""",
            disable_web_page_preview=True,
        )
    except:
        return await message.reply_text("» fαιℓє∂ тσ ѕєи∂ тнє ¢σиfιg ναяιαвℓєѕ.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text(
            "» ρℓєαѕє ¢нє¢к уσυя ρм, ι'νє ѕєит тнє ¢σиfιg ναяιαвℓєѕ тнєяє."
        )
