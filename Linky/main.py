# Linky - nextcord
# loading
print('\nLoading...')
import nextcord
import asyncio
import os
import random
import getpass
import socket
import datetime
import pytz
import json
import pymongo
import dns.resolver
from time import monotonic
import environ
environ.token()
never_gonna_give_you_up = os.getenv('TOKEN')
environ.connectDB()
conDB = os.getenv('connectDB')
u = getpass.getuser()
H = socket.gethostname()
userHost = u + '@' + H
client = nextcord.Client(intents=nextcord.Intents.all())
# connecting to db
print('Connecting to DB...')
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
cluster = pymongo.MongoClient(conDB)
db = cluster["linkydb"]
print('Connected!\n')

# on ready
@client.event
async def on_ready():
    UP = monotonic()
    os.environ['UP'] = str(UP)
    p = os.getenv('prefix')
    if p == None: os.environ['prefix'] = 'l!'
    p = os.getenv('prefix')
    print(f'Connected to Discord!')
    print(f'Logged in as {str(client.user)}!')
    print(f'Running on {userHost}!')
    print('')
    wait = asyncio.sleep
    rldinf = os.getenv('reloadinfo')
    channel = os.getenv('channel')
    if rldinf == 'reloading':
        channel = client.get_channel(int(channel))
        os.environ['reloadinfo'] = 'connected'
        await channel.send('**Reloaded!**')
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'Reloaded!'), status=nextcord.Status.idle)
        await wait(5)
    else: await wait(1.5)
    guilds = len(client.guilds)
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'{guilds} servers! | {p}help'), status=nextcord.Status.online)

# on message
@client.event
async def on_message(message):
    # to prevent lag:
    # Section a) checks if message starts with bot prefix or message is equal to bot ping
    p = os.getenv('prefix')
    if p == None: os.environ['prefix'] = 'l!'
    p = os.getenv('prefix')
    lowp = p.lower()
    cum2 = client.user.mention.replace('<@', '<@!')
    if message.content.startswith(lowp) or message.content == client.user.mention or message.content == cum2: pass
    else: return
    # Section b) checks if message is from DMs
    if message.guild == None:
       await reply('**{no} You cannot use this command in DMs!**')
       return
    
    # shortcuts
    msg = message.content
    sendmsg = message.channel.send
    author = message.author
    mention = message.author.mention
    reply = message.reply
    typing = message.channel.trigger_typing
    delete = message.delete
    wait = asyncio.sleep
    lowmsg = msg.lower()
    edit = message.edit
    react = message.add_reaction
    cum = client.user.mention
    prefix = p
    yes = '<a:Animated_Checkmark:901803000861966346>'
    no = '<a:no:901803557014077480>'
    
    # colours
    c = nextcord.Colour
    blue = c.blue()
    blurple = c.blurple()
    brand_green = c.brand_green()
    brand_red = c.brand_red()
    dark_blue = c.dark_blue()
    dark_gold = c.dark_gold()
    dark_gray = c.dark_gray()
    dark_green = c.dark_green()
    dark_grey = c.dark_grey()
    dark_magenta = c.dark_magenta()
    dark_orange = c.dark_orange()
    dark_purple = c.dark_purple()
    dark_red = c.dark_red()
    dark_teal = c.dark_teal()
    dark_theme = c.dark_theme()
    darker_gray = c.darker_gray()
    darker_grey = c.darker_grey()
    default = c.default()
    fuchsia = c.fuchsia()
    gold = c.gold()
    green = c.green()
    greyple = c.greyple()
    light_gray = c.light_gray()
    light_grey = c.light_grey()
    lighter_gray = c.lighter_gray()
    lighter_grey = c.lighter_grey()
    magenta = c.magenta()
    red = c.red()
    teal = c.teal()
    yellow = c.yellow()
    
    # top role colour
    if author.top_role.colour == default:  trc = dark_theme
    else: trc = author.top_role.colour
    
    ####################
    # start of functions define #
    
    # ping to member id
    def ping_replace(mem):
        if '<' in mem and '@' in mem and '>' in mem:
            mem = mem.replace('<', '')
            mem = mem.replace('@', '')
            mem = mem.replace('>', '')
            if '!' in mem: mem = mem.replace('!', '')
        return int(mem)
    
    # remove prefix
    def remprefix(msg):
        p = os.getenv('prefix')
        lowp = p.lower()
        if msg.startswith(p):
            msg = msg.split(p, 1)[1]
            msg = msg.lstrip()
        elif msg.startswith(lowp):
            msg = msg.split(lowp, 1)[1]
            msg = msg.lstrip()
        return msg
    
    # time rn
    def timenow(debug=True):
        os.environ['time'] = '-[!] Error-'
        current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')) 
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second
        if debug == True:
            time = f'[ {hour}:{minute}:{second} ]'
            os.environ['time'] = time
        elif debug == False:
            time = f'{hour}:{minute}:{second}'
            os.environ['time'] = time
        time = os.getenv('time')
        return time
    
    # intro
    async def intro():
        cServ = await client.fetch_guild(919110751103361084)
        alexy = await cServ.fetch_member(697323031919591454)
        sqd = await cServ.fetch_member(477683725673693184)
        intro = f'''Hey! I am **Linky Bot**. Created by **`{alexy}`** and **`{sqd}`**.
My prefix is **`{p}`**.
Coded in `Python` using the `nextcord` library.
(short introduction of the bot here)
**Join the community server here: https://discord.gg/E4CDUJBUm5**'''
        return intro
    
    # community server
    async def cServ():
        cServ = await client.fetch_guild(919110751103361084)
        alexy = await cServ.fetch_member(697323031919591454)
        sqd = await cServ.fetch_member(477683725673693184)
        return [cServ, alexy, sqd]
    
    # end of functions define #
    ###################
     
    # emoji servers
    emojiServers = [901800331204259870]
    if message.guild.id in emojiServers:
        is_emojiServer = True
        msg = remprefix(msg)
        if msg == 'emojis':
            await reply('**List of emojis:**')
            for emoji in message.guild.emojis:
                await sendmsg(f'{emoji} - {emoji.id}')
                await sendmsg(f'\{emoji}')
                await sendmsg('`-------`')
            return
     
    # if author is bot itself
    if author == client.user: return
    
    # if lowmessage starts with lowprefix
    lowprefix = prefix.lower()
    if lowmsg.startswith(lowprefix):
        # removing prefix from msg
        msg = remprefix(msg)
        
        # ''
        if msg == '':
            intro = await intro()
            await reply(intro)
        
        #############################
        ### type commands below this line ###
        
        # help
        elif msg == 'help':
            emb = nextcord.Embed(title=f'Commands - Help - {client.user.name}', description=f'''
```
Prefix: {prefix}
```
**`{p}help`** - Replies with a list of commands
**`{p}aliases`** - Shows aliases for commands
''', color=trc)
            emb.add_field(name='Links', value=f'''
```py
# pretty empty ay?
```
''', inline=False)
            emb.add_field(name='Bot', value=f'''
**`{p}ping`** - Replies with the bot latency
**`{p}sourcecode`** - Replies with the bot's source code
**`{p}stats`** - Replies with bot stats
''', inline=False)
            emb.set_author(name=client.user.name, icon_url=client.user.avatar.url)
            await reply(embed=emb)
        
        # aliases
        elif msg == 'aliases':
            emb = nextcord.Embed(title=f'Aliases - {client.user.name}', description=f'''
```
Prefix: {prefix}
```
**`{p}ping`** - {p}latency
**`{p}sourcecode`** - {p}source, {p}source-code, {p}sc, {p}code
''', color=trc)
            emb.set_author(name=client.user.name, icon_url=client.user.avatar.url)
            await reply(embed=emb)
        
        # reload
        elif msg == 'reload' or msg == 'r':
             E = await cServ()
             alexy = E[1]
             sqd = E[2]
             if author == alexy or author == sqd:
               channel = message.channel.id
               os.environ['reloadinfo'] = 'reloading'
               os.environ['channel'] = str(channel)
               await reply('**Reloading...**')
               await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'Reloading!'), status=nextcord.Status.dnd)
               time = timenow()
               print(f'\n{time} Reloading Bot...\n')
               os.system('python3 main.py')
               os._exit(1)
             else:
                 if guild.id == cServ.id: await reply(f'**{no} You do not have permission to use this command!**')
                 else: await reply(f'**Command `{p}{msg}` not found!**')
         
         # ping
        elif msg == 'ping' or msg == 'latency':
            emb = nextcord.Embed(title=client.user.name, description='''
Checking...
''', color=trc)
            emb.set_author(name=client.user.name, icon_url=client.user.avatar.url)
            before = monotonic()
            pingmsg = await reply(embed=emb)
            ping = round((monotonic() - before) * 1000, 2)
            cping = round(client.latency * 1000, 2)
            avg_ping = sum([ping, cping]) / 2
            if avg_ping <= 15: colour = dark_green
            elif avg_ping <= 115 and ping > 15: colour = green
            elif avg_ping <= 275 and ping > 115: colour = yellow
            elif avg_ping <= 500 and ping > 275: colour = red
            elif avg_ping <= 750 and ping > 500: colour = dark_orange
            else: colour = dark_red
            emb = nextcord.Embed(title='Pong! 🏓', description=f'''
**Latency:** {ping} ms
**Client Latency:** {cping} ms

*Currently running on **`{userHost}`**.*
''', color=colour)
            emb.set_author(name=client.user.name, icon_url=client.user.avatar.url)
            await pingmsg.edit(embed=emb)
         
        ### type commands above this line ###
        #############################
        else: await reply(f'**Command `{p}{msg}` not found!**')
    
    # if message is bot mention
    if msg == cum or msg == cum2:
        intro = await intro()
        await reply(intro)
    
    # update status lol
    guilds = len(client.guilds)
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f'{guilds} servers! | {p}help'), status=nextcord.Status.online)

# logging into Linky
print('Logging into Linky...\n\n')
client.run(never_gonna_give_you_up)