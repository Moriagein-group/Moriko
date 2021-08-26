
import discord
import requests
from discord.ext import commands
from pprint import pprint
import aiohttp

TOKEN = "token"

AuthB = "Bot " + TOKEN

headers = {
    "Authorization": AuthB
}


def returnNormalUrl(channelId):
    return "https://discordapp.com/api/channels/" + str(channelId) + "/messages"


async def notify_callback(id, token):
    url = "https://discord.com/api/v8/interactions/{0}/{1}/callback".format(id, token)
    json = {
        "type": 6
    }
    async with aiohttp.ClientSession() as s:
        async with s.post(url, json=json) as r:
            if 200 <= r.status < 300:
                return


async def on_socket_response(msg):
    if msg["t"] != "INTERACTION_CREATE":
        return

    pprint(msg)


class MyBot(commands.Bot):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_listener(on_socket_response)


bot = MyBot(command_prefix='$', description='discord bot')


@bot.event
async def on_message(msg):
    if msg.content == "hello":
        normal_url = "https://discordapp.com/api/channels/" + str(msg.channel.id) + "/messages"
        json = {
            "content": "Hello World",
            "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "label": "1st",
                            "style": 1,
                            "custom_id": "click_one",
                        },
                        {
                            "type": 2,
                            "label": "2nd",
                            "style": 3,
                            "custom_id": "click_two",
                        },
                    ]

                }
            ]
        }
        r = requests.post(normal_url, headers=headers, json=json)



bot.run(TOKEN)