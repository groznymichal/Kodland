import discord
import random

#zmienna intents, ktora przechowuje uprawnienia bota

intents = discord.Intents.default()

#do odczytu wiadomosci
intents.message_content = True

#obiekt Client
client = discord.Client(intents=intents)

def gen_pass(pass_len):
    elements = 'abcdefghijklmnoprstuwxyz1234567890'
    password = ''
    for i in range(pass_len):
        password += random.choice(elements)
    
    return password

def flip_coin():
    elements = ['Orzeł', 'Reszka', 'Kant']
 
    return random.choice(elements)


@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('co'):
        await message.channel.send('nic ' + message.author.display_name)
    elif message.content.startswith('!smile'):
        await message.channel.send(':sunglasses:')
    elif message.content.startswith('!haslo'):
        await message.channel.send('Hasło ' + gen_pass(10))
    elif message.content.startswith('!coin'):
        await message.channel.send('Wypadło ' + flip_coin())         
        
client.run('token')




