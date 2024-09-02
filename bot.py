import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from captain_planet_game import CaptainPlanetGame

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

game_instances = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="start", description="Start a new Captain Planet game")
async def start_game(interaction: discord.Interaction):
    game_instances[interaction.user.id] = CaptainPlanetGame()
    await interaction.response.send_message(game_instances[interaction.user.id].start_game())

@bot.tree.command(name="action", description="Perform an action in the Captain Planet game")
@app_commands.describe(action="Choose a number between 1 and 5")
async def game_action(interaction: discord.Interaction, action: int):
    if interaction.user.id not in game_instances:
        await interaction.response.send_message("You haven't started a game yet! Use /start to begin.")
        return
    
    if action < 1 or action > 5:
        await interaction.response.send_message("Invalid action! Choose a number between 1 and 5.")
        return
    
    game = game_instances[interaction.user.id]
    result = game.game_loop(action)
    await interaction.response.send_message(result)
    
    if "Congratulations" in result or "Oh no! You've been defeated" in result:
        del game_instances[interaction.user.id]

bot.run(TOKEN)
