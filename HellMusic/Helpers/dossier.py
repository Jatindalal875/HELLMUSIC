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

from FallenMusic import BOT_NAME

PM_START_TEXT = """
нєℓℓσ {0}, 🥰
๏ тнιѕ ιѕ** {1} !

➻ α fαѕт αи∂ ρσωєяfυℓ мυѕι¢ ρℓαуєя вσт.
"""

START_TEXT = """
**нєℓℓσ** {0}, 😍
  {1} ¢αи иσω ρℓαу ѕσиg ιи {2}.

──────────────────
➻ fσя gєттιиg нєℓρ αвσυт мє σя ιf уσυ ωαииα αѕк ѕσмєтнιиg уσυ ¢αи ʝσιи му [ѕυρρσят ¢нαт]({3}).
"""

HELP_TEXT = f"""
<u>❄ **αναιℓαвℓє ¢σммαи∂ѕ fσя υѕєяѕ ιи {BOT_NAME} :**</u>

๏ /play : ѕтαят ѕтяєαмιиg тнє яєqυєѕтєf тяα¢к σи νι∂єσ¢нαт.
๏ /pause : ραυѕє тнє ¢υяяєит ρℓαуιиg ѕтяєαм.
๏ /resume : яєѕυмє тнє ραυѕє∂ ѕтяєαм.
๏ /skip : ѕкιρ тнє ¢υяяєит ρℓαуιиg ѕтяєαм αи∂ ѕтαят ѕтяєαмιиg тнє иєχт тяα¢к ιи qυєυє.
๏ /end : ¢ℓєαиѕ тнє qυєυє αи∂ єи∂ тнє ¢υяяєит ρℓαуιиg ѕтяєαм.

๏ /ping : ѕнιω тнє ριиg αи∂ ѕуѕтєм ѕтαтѕ σf тнє вσт.
๏ /sudolist : ѕнσωѕ тнє ℓιѕт σf ѕυ∂σ υѕєяѕ σf тнє вσт.

๏ /song : ∂σωиℓσα∂ тнє яєqυєѕтє∂ ѕσиg αи∂ ѕє∂ ιт тσ уσυ.

๏ /search : ѕєαя¢єѕ тнє gινєи qυєяу σи уσυтυвє αи∂ ѕнσωѕ уσυ тнє яєѕυℓт.
"""

HELP_SUDO = f"""
<u>✨ **ѕυ∂σ ¢σммαи∂ѕ ιи {BOT_NAME} :**</u>

๏ /activevc : ѕнσωѕ тнє ℓιѕт σf ¢υяяєитℓу α¢тινє νσι¢є¢нαт.
๏ /eval or /sh : яυиѕ тнє gινєи ¢σ∂є σи тнє вσт'ѕ тєямιиαℓѕ.
๏ /speedtest : яυиѕ α ѕρєє∂тєѕт σи тнє вσт'∂ ѕєяνєя.
๏ /sysstats : ѕнιωѕ тнє ѕуѕтєм ѕтαтѕ σf тнє вσт'ѕ ѕєяνєя.

๏ /setname [тєχт σя яєρℓу тσ α тєχт] : ¢нαиgє тнє αѕѕιѕтαит α¢¢συит иαмє.
๏ /setbio [тєχт σя яωρℓу тσ α тєχт] : ¢нαиgє тнє вισ σf тнє αѕѕιѕтαит α¢¢συит.
๏ /setpfp [яєρℓу тσ α ρнσтσ] : ¢нαиgє тнє ρfρ σf тнє αѕѕιѕтαит α¢¢συит.
๏ /delpfp : ∂єℓєтє тнє ¢υяяєит ρfρ σf тнє αѕѕιѕтαит α¢¢συит.
"""

HELP_DEV = f"""
<u>✨ **σωиєя ¢σммαи∂ѕ ιи {BOT_NAME} :**</u>

๏ /config : тσ gєт αℓℓ ¢σиfιg ναяιєвℓє∂ σf вσт.
๏ /broadcast [мєѕѕαgє σя яєρℓу тσ α мєѕѕαgє] : вяσα∂¢αѕт тнє мєѕѕαgє тσ ѕєяνєя ¢нαт σf тнє вσт.
๏ /rmdownloads : ¢ℓєαиѕ тнє ¢α¢нє fιℓє∂ ∂σωиℓσѕ∂є∂ σи тнє вσт'ѕ ѕєяνєя.
๏ /leaveall : σя∂єя тнє αѕѕι∂тαит α¢¢συит тσ ℓєανє αℓℓ ¢нαтѕ.

๏ /addsudo [υ∂яяиαмє σя яєρℓу тσ α υѕєя] : α∂∂ тнєя υѕєя тσ ѕυ∂σ υѕєяѕ ℓιѕт.
๏ /rmsudo [υѕєяиαмє σя яєρℓу тσ α υѕєя] : яємσνє тнє υѕєя fяσм ѕυ∂ι υѕєяѕ ℓι∂т.
"""
