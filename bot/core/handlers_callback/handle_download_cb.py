from bot.core.get_vars import get_val
from pyrogram import filters
from bot.downloaders.telegram_download import down_load_media_pyro


async def handle_download_cb(client, query):
        data= query.data
        list = data.split(" ")
        message= query.message
        tag = f"@{message.reply_to_message.from_user.username}"
        media= get_val("MEDIA")

        if "default" in list[1]:
            await down_load_media_pyro(client, message, media, tag)

        if "rename" in list[1]: 
            question= await message.reply(
                 text= "Send the new name /ignore to cancel"
             )
            reply_message = await client.listen.Message(filters.text, id='1', timeout= 30)

            if "/ignore" in reply_message.text:
                await message.reply("Cancelled")
                await client.listen.Cancel("1")
            else:
                await question.delete()
                await down_load_media_pyro(client, message, media, tag, reply_message.text, True)
