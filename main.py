import os
import discord

import glob, random

import requests, json

#Se crea una instancia del cliente, esta es la conexión con Discord. 
#Es parte de la librería de discord.py
client = discord.Client()

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)
  

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

  #Mensaje de saludo
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  #Mensaje de saludo
  if message.content.startswith('$frase'):
    frase = get_quote()
    await message.channel.send(frase)

  #Generar una imagen aleatoria
  if message.content.startswith('$img'):
    file_path_type = ['./Fuente/*.png', './Fuente/*.jpeg', './Fuente/*.jpg']
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)

    
    await message.channel.send(file=discord.File(random_image))



client.run(os.getenv('discToken'))