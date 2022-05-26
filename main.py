import os
import discord
import glob, random
import requests, json
from replit import db

#Se crea una instancia del cliente, esta es la conexión con Discord. 
#Es parte de la librería de discord.py
client = discord.Client()

#Lista de palabras que buscará 
sad_words = ['sad', 'mal']

starter_encour = [
  'Ánimo',
  'Si se puede',
  'Padelante es palla'
]

#Activar o desactivar que el bot responda a mensajes tirstes
if 'responding' not in db.keys():
  db['responding'] = True

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)

#Función para actualizar la BDD
def update_encour(encour_msg):
  if 'encour' in db.keys():
    encour = db['encour']
    encour.append(encour_msg)
    db['encour'] = encour
  else: 
    db['encour'] = [encour_msg]

#Borrar un mensaje de la BDD
def delete_encour(index):
  encour = db['encour']
  if len(encour) > index:
    del encour[index]
    db['encour'] = encour
        

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

  #Generar una imagen aleatoria
  if msg.startswith('$img'):
    file_path_type = ['./Fuente/*.png', './Fuente/*.jpeg', './Fuente/*.jpg']
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)
    
    await message.channel.send(file=discord.File(random_image))

  #Cambiar el respondeo
  if db['responding'] == True :
    options = starter_encour
    if 'encour' in db.keys():
      options += db['encour']

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith('$new'):
    encour_msg = msg.split('$new ', 1)[1]
    update_encour(encour_msg)
    await message.channel.send('New encour added')

  if msg.startswith('$del'):
    encour = []
    if 'encour' in db.keys():
      index = int(msg.split('$del', 1)[1])
      delete_encour(index)
      encour = db['encour']
    await message.channel.send(encour)

  if msg.startswith('$list'):
    encour = []
    if 'encour' in db.keys():
      encour = db['encour']
    await message.channel.send(encour)

  if msg.startswith('$responding'):
    value = msg.split('$responding ', 1)[1]

    if value.lower() == 'true':
      db['responding'] == True
      await message.channel.send('Respondiendo activado')
    else:
      db['responding'] == False
      await message.channel.send('Respondiendo desactivado')
#---------------------------- tutorial ai
  if msg.startswith('$aibot'):
    pass


    
client.run(os.getenv('discToken'))