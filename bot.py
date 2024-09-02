import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from captain_planet_game import CaptainPlanetGame

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
game_instances = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='start')
async def start_game(ctx):
    game_instances[ctx.author.id] = CaptainPlanetGame()
    await ctx.send(game_instances[ctx.author.id].start_game())

@bot.command(name='action')
async def game_action(ctx, action: int):
    if ctx.author.id not in game_instances:
        await ctx.send("You haven't started a game yet! Use !start to begin.")
        return
    
    game = game_instances[ctx.author.id]
    result = game.game_loop(action)
    await ctx.send(result)
    
    if "Congratulations" in result or "Oh no! You've been defeated" in result:
        del game_instances[ctx.author.id]

bot.run(TOKEN)
