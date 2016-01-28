import discord
import safygiphy
import requests
import json

client = discord.Client()
client.login("", "")


@client.event
def on_member_join(member):
    server = member.server
    client.send_message(server, 'Welcome {0} to {1.name}!'.format(member.mention(), server))

@client.event
def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    #hello
    if message.content.startswith('Hello ava') or message.content.startswith('Hello Ava'):
        client.send_message(message.channel, 'Hello {}!'.format(message.author.mention()))

    #echo
    if message.content.startswith('Ava echo') or message.content.startswith('ava echo'):
        client.send_message(message.channel, message.content.replace(message.content[:8], ''))

    #gif me
    if message.content.startswith('Ava gif me ') or message.content.startswith('ava gif me '):
        msg = message.content.replace(message.content[:11], '')
        s = safygiphy.Giphy()
        ssearch = s.random(tag=msg)
        try:
            gif_url = ssearch['data']['image_url']
            client.send_message(message.channel, gif_url.format(message.author.mention()))
        except:
            client.send_message(message.channel, "I couldn't find that".format(message.author.mention()))


    #cat fact
    if message.content.startswith('Ava cat fact') or message.content.startswith('ava cat fact'):
        r=requests.get('http://catfacts-api.appspot.com/api/facts?number=5')
        jsn = json.loads(r.text)
        fact = jsn['facts'][0]
        client.send_message(message.channel, fact.format(message.author.mention()))

    #help
    if message.content.startswith('Ava help') or message.content.startswith('ava help'):
    	help_message = " I know many things:\ngif me (string)\ncat fact\necho (string)...\nI'll be learning more soon!"
    	client.send_message(message.channel, help_message.format(message.author.mention()))



@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
