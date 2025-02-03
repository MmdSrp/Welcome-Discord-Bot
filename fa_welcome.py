# Created By MmdSrp
import discord
from discord.ext import tasks, commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# پیام خوش آمد گویی
WELCOME_EMBED = discord.Embed(title="🎉 عضو جدید ",
                                description="🎇",
                                color=discord.Color.green())

WELCOME_CHANNEL_ID = 123456789012345678  # جایگزین با آیدی واقعی کانال خوش آمد گویی
TOKEN = 'Your Bot Token'

@tasks.loop(seconds=5)
async def check_new_members():
    global new_members  # اعلام متغیر new_members به عنوان یک متغیر سراسری
    for guild in client.guilds:
        for member in guild.members:
            if member.joined_at > client.launch_time and member.id not in new_members:
                new_members.append(member.id)  # افزودن شناسه عضو به لیست
                await send_welcome_message(guild, member)

@client.event
async def on_ready():
    print(f"{client.user} آنلاین است!")
    global new_members  # راه‌اندازی new_members به عنوان یک لیست خالی
    new_members = []
    client.launch_time = discord.utils.utcnow()  # زمان راه‌اندازی ربات را ثبت کن
    check_new_members.start()

async def send_welcome_message(guild, member):
    global WELCOME_CHANNEL_ID  # اعلام WELCOME_CHANNEL_ID به عنوان یک متغیر سراسری
    welcome_channel = guild.get_channel(WELCOME_CHANNEL_ID)  # دریافت کانال خوش آمد گویی
    WELCOME_EMBED.set_thumbnail(url=member.avatar.url)
    WELCOME_EMBED.description = f"**سلام, {member.mention}!** 🎊🎊خوش اومدی به سرور لحظه های خوبی رو برای شما آرزومندم"
    WELCOME_EMBED.set_footer(text="موفق باشی 🍀")

    await welcome_channel.send(embed=WELCOME_EMBED)

client.run("TOKEN")  # جایگزین با توکن واقعی ربات خود
# Created By MmdSrp
