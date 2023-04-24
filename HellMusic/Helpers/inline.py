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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from HellMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ¢ℓσѕє ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="α∂∂ мє тσ уσυ gяσυρ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="нєℓρ & ¢σммαи∂ѕ", callback_data="hell_help")],
    [
        InlineKeyboardButton(text="❄ ¢нαт gяσυρ ❄", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="☁️ sᴏᴜʀᴄᴇ ☁️", url="https://graph.org/file/83460f247a582d9349f1f.jpg"
        ),
        InlineKeyboardButton(text="😈 ∂єνєℓσρєя 😈", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="α∂∂ мє тσ уσυ gяσυρ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="❄ ¢нαт gяσυρ ❄", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="☁️ sᴏᴜʀᴄᴇ ☁️", url="https://graph.org/file/83460f247a582d9349f1f.jpg"
        ),
        InlineKeyboardButton(text="😈 ∂єνєℓσρєя 😈", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="єνєяуσиє",
            callback_data="hell_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="ѕυ∂σ", callback_data="hell_cb sudo"),
        InlineKeyboardButton(text="σωиєя", callback_data="hell_cb owner"),
    ],
    [
        InlineKeyboardButton(text="вα¢к", callback_data="hell_home"),
        InlineKeyboardButton(text="¢ℓσѕє", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="✨ ѕυρρσят ✨", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="вα¢к", callback_data="hell_help"),
        InlineKeyboardButton(text="¢ℓσѕє", callback_data="close"),
    ],
]
