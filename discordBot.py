from discord_easy_commands import EasyBot
import pyjokes
import discord




token = 'MTA1NzI0NTk4ODg2MDk4NTM2NQ.Ghh62y.kccHOicG-49JhKfQODLoNtnGRoEaEyeolIZ46M'


joke = pyjokes.get_jokes(language='es', category='all')
intents = discord.Intents.all()
bot = EasyBot(intents = intents)


bot.setCommand('!youtube', 'www.youtube.com')
bot.setCommand('!instagram','syscursos')
bot.setCommand('!chiste', joke)

bot.run(token)
