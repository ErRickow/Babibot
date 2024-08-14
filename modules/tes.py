import os 
import sys
from time import get_readable_time

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix

def get_readable_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += f"{time_list.pop()}, "

    time_list.reverse()
    readable_time += ":".join(time_list)

    return readable_time

@Client.on_message(filters.command(["tes", "t"], prefix) & filters.me)
async def tes(_, message: Message):
uptime = get_readable_time((time.time() - time.time()))
start = dt.now()
end = dt.now()
duration = (end - start).microseconds / 1000

await message.reply_text(
        f" **Pong !!** " f"`%sms` \n" f" **Uptime** - " f"`{uptime}` " % (duration)
    )
    
    modules_help["tes"] = {
    "tes": "Check ping to Telegram servers",
}