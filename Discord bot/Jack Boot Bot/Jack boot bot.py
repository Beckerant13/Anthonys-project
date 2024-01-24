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
last_disconnect_time = {user_id_to_track: None}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='disconnect_count', help='Get the disconnect count for a specific user')
async def get_disconnect_count(ctx):
    await ctx.send(f"Disconnect count for {ctx.author.name}: {disconnect_count[user_id_to_track]}")

@bot.event 
async def on_voice_state_update(member, before, after):
    if before.channel is not None and after.channel is None and member.id == user_id_to_track:
        async for entry in member.guild.audit_logs(action=discord.AuditLogAction.member_disconnect):
            disconnect_initiator = entry.user
            disconnect_time = entry.created_at
            
            # Check if the disconnect initiator is not the specified user and enough time has passed
            if disconnect_initiator.id != user_id_to_track and (last_disconnect_time[user_id_to_track] is None or disconnect_time > last_disconnect_time[user_id_to_track]):
                disconnect_count[user_id_to_track] += 1
                last_disconnect_time[user_id_to_track] = disconnect_time
                print(f"{member.name} was disconnected by {disconnect_initiator.name}. Count: {disconnect_count[user_id_to_track]}")
                
            break

bot.run(TOKEN)