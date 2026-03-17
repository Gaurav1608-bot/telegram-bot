from telethon import TelegramClient, events

api_id = 33902671
api_hash = "9d748a99c7d19cf6487c998d6bd45b01"

source_channel = "@Bachat_Bazaarr"   # jaha se lena hai
target_channel = "@lootdealsgujju"  # jaha bhejna hai

client = TelegramClient("session", 33902671, 9d748a99c7d19cf6487c998d6bd45b01)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await client.send_message(target_channel, event.message)

client.start()
print("Bot Running Successfully...")
client.run_until_disconnected()
