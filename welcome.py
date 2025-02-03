# Created By MmdSrp
import discord
from discord.ext import tasks, commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Welcome message embed
WELCOME_EMBED = discord.Embed(title="🎉 New Member ",
                                description="🎇",
                                color=discord.Color.green())

# Replace with the actual welcome channel ID
WELCOME_CHANNEL_ID = 123456789012345678  # Replace with your actual welcome channel ID
TOKEN = 'Your Bot Token'

@tasks.loop(seconds=5)
async def check_new_members():
    global new_members  # Declare new_members as a global variable
    for guild in client.guilds:
        for member in guild.members:
            if member.joined_at > client.launch_time and member.id not in new_members:
                new_members.append(member.id)  # Add member ID to the list
                await send_welcome_message(guild, member)

@client.event
async def on_ready():
    print(f"{client.user} is online!")
    global new_members  # Initialize new_members as an empty list
    new_members = []
    client.launch_time = discord.utils.utcnow()  # Record bot launch time
    check_new_members.start()

async def send_welcome_message(guild, member):
    global WELCOME_CHANNEL_ID  # Declare WELCOME_CHANNEL_ID as a global variable
    welcome_channel = guild.get_channel(WELCOME_CHANNEL_ID)  # Get the welcome channel
    WELCOME_EMBED.set_thumbnail(url=member.avatar.url)
    WELCOME_EMBED.description = f"**Hello, {member.mention}!** 🎊🎊 Welcome to the server! Wishing you great moments here."
    WELCOME_EMBED.set_footer(text="Good luck! 🍀")

    await welcome_channel.send(embed=WELCOME_EMBED)

client.run("TOKEN") 
# Created By MmdSrp
