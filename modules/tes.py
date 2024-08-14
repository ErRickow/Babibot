import os 
import sys
import time

uptime = get_readable_time((time.time() - time.time()))
start = dt.now()
end = dt.now()
duration = (end - start).microseconds / 1000

await message.reply_text(
        f" **Pong !!** " f"`%sms` \n" f" **Uptime** - " f"`{uptime}` " % (duration)
    )