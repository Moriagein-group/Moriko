# from ebi_test.testebi import TOKEN
import discord
from discord.ext import commands
#pip install discord-buttons-plugin
from discord_buttons_plugin import *
#pip install requests
import requests
bot = commands.Bot(command_prefix = "!")
buttons = ButtonsClient(bot)
TOKEN = "token"
# 好きなトークンを入れてね！

@bot.event
async def on_ready():
	print("準備完了")
  
@buttons.click
async def button_hello(ctx):
	ctx.guild.voice_client.play(discord.FFmpegPCMAudio("yeah.mp3"))

@buttons.click
async def button_ephemeral(ctx):
	await ctx.reply("このメッセージはあなたにしか見えていません！", flags = MessageFlags().EPHEMERAL)

@buttons.click
async def button_c(ctx):
	await ctx.reply("こんにちは！")

@buttons.click
async def button_d(ctx):
	await ctx.reply("こんにちは！")

@buttons.click
async def button_e(ctx):
	await ctx.reply("こんにちは！")

# @buttons.click
# async def button_f(ctx):
# 	await ctx.reply("こんにちは！")

@bot.command()
async def hikakin(ctx):
    
    if ctx.author.voice is None:
        await ctx.channel.send("どのボイスチャンネルに入れば良いのかしら？")
        return
    # ボイスチャンネルに接続する
    await ctx.author.voice.channel.connect()

    # hikakin boxを生成
    await buttons.send(
		content = "これがヒカ〇ンBOXですわ！", 
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					label="yeah!", 
					style=ButtonType().Primary, 
					custom_id="button_hello"
				),
                Button(
					label="ﾊﾟﾌﾊﾟﾌ",
					style=ButtonType().Primary,
					custom_id="button_ephemeral"
				),
                Button(
					label="拍手",
					style=ButtonType().Primary,
					custom_id="button_c"
				)
			]),
            # 三つ区切りにしてます（深い意味はないよ）
            ActionRow([
				Button(
					label="笑い声",
					style=ButtonType().Primary,
					custom_id="button_d"
				),
				Button(
					label="ﾃﾞﾃﾞﾄﾞﾝ!",
					style=ButtonType().Primary,
					custom_id="button_e"
				)
			])
		]
	)

bot.run(TOKEN)