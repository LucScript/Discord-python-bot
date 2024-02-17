import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot has been loged')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('salut'):
        time.sleep(0.3)
        await message.channel.send('Salut')
        
