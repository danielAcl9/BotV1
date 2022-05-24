import os
import discord

import glob, random

import requests, json

#Se crea una instancia del cliente, esta es la conexión con Discord. 
#Es parte de la librería de discord.py
client = discord.Client()

#Lista de palabras que buscará 
sad_words = ['sad', 'deppresed', 'unhappy', 'angry', 'mal', 'miserable']

starter_encour = [
  'Ánimo',
  'Tu puedes',
  'Eres la mejor'
]

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

  msg = message.content
  
  if message.author == client.user:
    return

  #Mensaje de saludo
  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  #Genera una frase
  if msg.startswith('$frase'):
    frase = get_quote()
    await message.channel.send(frase)

  #Leer los mensajes en busca de palabras específicas
  if any (word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encour))

  #Generar una imagen aleatoria
  if msg.startswith('$img'):
    file_path_type = ['./Fuente/*.png', './Fuente/*.jpeg', './Fuente/*.jpg']
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)

    
    await message.channel.send(file=discord.File(random_image))


client.run(os.getenv('discToken'))