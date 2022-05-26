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

optionsMusic = [ """--- Mis favoritas ---
https://open.spotify.com/playlist/2BlfrsHONBiUHVWwrY2426?si=f747fedfc13a4271""",
                
                """--- Tu rubia favorita ---
https://open.spotify.com/playlist/37i9dQZF1DX5KpP2LN299J?si=86d6e73d567e4120""",

                """--- Benito God ---
https://open.spotify.com/playlist/37i9dQZF1DX2apWzyECwyZ?si=76b7093787fe449f""",

                """--- Musiquita en Francés <3 ---
https://open.spotify.com/playlist/62QlpG1CAeAc95UskqayH6?si=1340c96c7a0d428b"""
]

dates = """
**Marzo 11:** Comenzamos a salir
**Marzo 23**: Cumpleaños de Daniel
**Abril 2:** Se hizo oficial
**Abril 30:** Cita en la Ruitoca
**Mayo 23:** Adoptamos a Panqueque
**Agosto 12:** Cumpleaños de Camila
"""

helpMenu = """**$hola** - Pa' los buenos días
**$<3** - Frases lindas para ti
**$motiv** - Frases motivacionales
**$img** - Fotos tuyas o de nosotros que miro cuando te extraño
**$music** - Una playlist aleatoria de musica que nos gusta
**$dates** - Fechas especiales"""

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

  #Comando de ayudas
  if msg.startswith('$help'):
    await message.channel.send(helpMenu)
    
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

  #Música
  if msg.startswith('$music'):
    await message.channel.send(random.choice(optionsMusic))

  #Fechas
  if msg.startswith('$dates'):
    await message.channel.send(dates)

  
client.run(os.getenv('discToken'))