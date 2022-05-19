import os
import discord

import glob, random

#Se crea una instancia del cliente, esta es la conexión con Discord. 
#Es parte de la librería de discord.py
client = discord.Client()

#Registrar un evento
@client.event

#Este evento se llamará cuando el bot esté listo para usarse
async def on_ready(): 
  print('Iniciado como {0.user}'.format(client))

#Evento cuando recibe un mensaje, es case sensitive y si no le coloco lo específico que dice, colapsa
@client.event

async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$img'):
    file_path_type = ['./Fuente/*.png', './Fuente/*.jpeg', './Fuente/*.jpg']
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)

    
    await message.channel.send(file=discord.File(random_image))



client.run(os.getenv('discToken'))