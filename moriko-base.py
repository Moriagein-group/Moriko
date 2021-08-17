import discord

TOKEN = 'ODc3MDYxNTE2MDAyNzI1OTI4.YRtJMA.b7jLUyo-JGOIsz94SBFA9NEV3Kk'
client = discord.Client()

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('login successful')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "?盛子様":
        await message.channel.send('お呼びでしたか？　盛子ですの')

@client.event 
async def on_message(message):
    if message.content == "!joinmoriko":
        if message.author.voice is None:
            await message.channel.send("どのボイスチャンネルに入れば良いのかしら？")
            return
        # ボイスチャンネルに接続する
        await message.author.voice.channel.connect()

        await message.channel.send("ごきげんよう！盛子ですわ！")

    elif message.content == "!leavemoriko":
        if message.guild.voice_client is None:
            await message.channel.send("私はどこにも入っていませんわよ！！")
            return

        # 切断する
        await message.guild.voice_client.disconnect()

        await message.channel.send("ごきげんよう～")

client.run(TOKEN)