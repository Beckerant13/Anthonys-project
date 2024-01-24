import discord 
from config import TOKEN
from config import user_id_to_track
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)
user_id_to_track = user_id_to_track
disconnect_count = {user_id_to_track: 0}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
@bot.command(name='disconnect_count', help='Get the disconnect count for a specific user')
async def get_disconnect_count(ctx):
    if ctx.author.id == user_id_to_track:
        await ctx.send(f"Disconnect count for {ctx.author.name}: {disconnect_count[user_id_to_track]}")
    else:
        await ctx.send("You are not authorized to use this command.")

@bot.event 
async def on_voice_state_update(member, before, after):
    if before.channel is not None and after.channel is None and member.id == user_id_to_track:
        async for entry in member.guild.audit_logs(action=discord.AuditLogAction.member_disconnect):
            disconnect_initiator = entry.user
            if disconnect_initiator.id != user_id_to_track:
                disconnect_count[user_id_to_track] += 1
                print(f"{member.name} was disconnected by {disconnect_initiator.name}. Count: {disconnect_count[user_id_to_track]}")

# Remove the break statement here

bot.run(TOKEN)