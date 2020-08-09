from discord.ext import commands
import DiscordPyMD.DiscordPyMD as dpymd


bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
	print("{bot.ready_message}")


@bot.command()
async def dpymd_try(ctx):
	await ctx.send(dpymd.bold("Some bold text."))
	await ctx.send(dpymd.code("Some code."))
	await ctx.send(dpymd.code_line("Some code single line."))
	await ctx.send(dpymd.italics("Some italics text."))
	await ctx.send(dpymd.strikethrough("Some strikethrough text."))
	await ctx.send(dpymd.underline("Some underlined text."))
	await ctx.send(dpymd.quote("Some quoted message."))
	await ctx.send(dpymd.quote_all("Some quoted messages (big text)."))

	# await ctx.send(dpymd.)


bot.run("{bot.token}")
