import discord
from discord.ext import commands
import requests
import pyttsx3

intents = discord.Intents.default()
intents.message_content =True
bot = commands.Bot(command_prefix="!", intents=intents )

@bot.command()
async def start(ctx):
    await ctx.send("Merhaba ben size her zaman değişen yeni bir bilgi veren botum")
    base_url = "https://uselessfacts.jsph.pl/random.json"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        fact = data.get("text")
        await ctx.send(fact)

        speak(fact)
    else:
        return("bilginiz alınamadı")
    
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



#@bot.command()
#async def weather(ctx, *, city:str):
    #weather_info = get_weather(city)
    #await ctx.send(weather_info)
    #speak(weather_info)

    

bot.run("")
