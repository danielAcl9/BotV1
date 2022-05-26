import os
import discord
import glob, random
import requests, json

client = discord.Client()

optionsHola = [
  'Hola mi amor!',
  'Días, porque buena estás tú',
  'Buenas buenaaaas',
  'Hola hermosa',
  'Hola mi peque',
  'Hola mi princesa'
]

optionsRom = [
  'Tú estás arreglando mi corazón cuando tú no lo rompiste, estás quitando inseguridades qué tú no causaste, y cumpliendo con cosas que nadie más logró.',
  'Tú eres siempre la respuesta cuando me preguntan que estoy pensando', 
  'Gracias por entenderme sin preguntar, por apoyarme sin pedírtelo y por quererme como soy',
  'Los mejores regalos no vienen envueltos, tú por ejemplo',
  'Gracias por aguantarte mis dolores de abuelito', 
  'Nunca dudes que te amo',
  'Estoy enamorado de ti y no me negaré el placer de decir cosas verdaderas. Estoy enamorado de ti',
  'Te quiero no por quien eres, sino por quien soy cuando estoy contigo'
]

#Función de las frases
def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)

@client.event
async def on_ready(): 
  print('Iniciado como {0.user}'.format(client))

#Evento cuando recibe un mensaje, es case sensitive y si no le coloco lo específico que dice, colapsa
@client.event
async def on_message(message):
  msg = message.content
  
  if message.author == client.user:
    return

  #Mensaje de saludo
  if msg.startswith('$hola'):
    await message.channel.send(random.choice(optionsHola))

  if msg.startswith('$<3'):
    await message.channel.send(random.choice(optionsRom))

  #Genera una frase
  if msg.startswith('$motiv'):
    frase = get_quote()
    await message.channel.send(frase)

  #Generar una imagen aleatoria
  if msg.startswith('$img'):
    file_path_type = ['./Fuente/*.png', './Fuente/*.jpeg', './Fuente/*.jpg']
    images = glob.glob(random.choice(file_path_type))
    random_image = random.choice(images)
    
    await message.channel.send(file=discord.File(random_image))
    
client.run(os.getenv('discToken'))