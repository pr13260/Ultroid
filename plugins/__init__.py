# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import time

from pyUltroid import *
from pyUltroid.dB import *
from pyUltroid.dB.core import *
from pyUltroid.functions import *
from pyUltroid.functions.all import *
from pyUltroid.functions.broadcast_db import *
from pyUltroid.functions.gban_mute_db import *
from pyUltroid.functions.goodbye_db import *
from pyUltroid.functions.google_image import googleimagesdownload
from pyUltroid.functions.sudos import *
from pyUltroid.functions.welcome_db import *
from pyUltroid.utils import *

from strings import get_string

try:
    import glitch_me
except ModuleNotFoundError:
    os.system(
        "git clone https://github.com/1Danish-00/glitch_me.git && pip install -e ./glitch_me"
    )

start_time = time.time()
ultroid_version = "v0.0.5"
OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id


def grt(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


KANGING_STR = [
    "Sedlyf vro, I am kenging cuz I need it vro",
    "Sorry sir, I need this sticker in my pack please ",
]
