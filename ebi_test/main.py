# coding: utf-8

import discord
import requests
from discord.ext import commands
from pprint import pprint
import aiohttp
TOKEN = 'token'
#えび用テストボットのトークンなのでトークンの書き換えが必要です

headers = {
    "Authorization": "Bot AAAAA"
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


def normalMessage(msg, content):
    normal_url = returnNormalUrl(msg["d"]["channel_id"])
    json = {
        "content": content
    }
    r = requests.post(normal_url, headers=headers, json=json)


async def on_socket_response(msg):
    if msg["t"] != "INTERACTION_CREATE":
        return

    pprint(msg)
    custom_id = msg["d"]["data"]["custom_id"]

    if custom_id == "click_one":
        normal_url2 = returnNormalUrl(msg["d"]["channel_id"]) + "/" + msg["d"]["message"]["id"]
        json2 = {
            "content": "LEFT",
            "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "label": "<",
                            "style": 1,
                            "custom_id": "click_one",
                            "disabled": True
                        },
                        {
                            "type": 2,
                            "label": ">",
                            "style": 3,
                            "custom_id": "click_two",
                            "disabled": False
                        },
                    ]
                }
            ]
        }
        r2 = requests.patch(normal_url2, headers=headers, json=json2)
        pprint(r2)
        await notify_callback(msg["d"]["id"], msg["d"]["token"])
    elif custom_id == 'click_two':
        normal_url2 = returnNormalUrl(msg["d"]["channel_id"]) + "/" + msg["d"]["message"]["id"]
        json2 = {
            "content": "Right",
            "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "label": "<",
                            "style": 1,
                            "custom_id": "click_one",
                            "disabled": False
                        },
                        {
                            "type": 2,
                            "label": ">",
                            "style": 3,
                            "custom_id": "click_two",
                            "disabled": True
                        },
                    ]

                }
            ]
        }
        r2 = requests.patch(normal_url2, headers=headers, json=json2)
        pprint(r2)
        await notify_callback(msg["d"]["id"], msg["d"]["token"])


class MyBot(commands.Bot):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_listener(on_socket_response)


bot = MyBot(command_prefix='$', description='slash test')


@bot.event
async def on_ready():
    print("Boot")
    await bot.change_presence(activity=discord.Game("プロセカ"))


@bot.event
async def on_message(msg):
    if msg.content == "うんこ":
        normal_url = returnNormalUrl(msg.channel.id)
        json = {
            "content": "LEFT",
            "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "label": "<",
                            "style": 1,
                            "custom_id": "click_one",
                            "disabled": True
                        },
                        {
                            "type": 2,
                            "label": ">",
                            "style": 3,
                            "custom_id": "click_two"
                        },
                    ]

                }
            ]
        }
        r = requests.post(normal_url, headers=headers, json=json)


bot.run(TOKEN)