#⟶̽ जय श्री ༢།म >𝟑🙏🚩

from pyrogram import filters
from pyrogram.types import Message

from RiteshMusic import app
from RiteshMusic.core.call import Anony

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Anony.stop_stream_force(message.chat.id)
