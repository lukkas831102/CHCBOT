import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.command()
async def roll(ctx, arg):
    try:
        num_dice = int(arg)
    except ValueError:
        await ctx.send("請輸入正確的骰子數量")
        return
    if num_dice > 10:
        await ctx.send("請輸入 10 個或更少的骰子")
        return
    results = [random.randint(1, 6) for _ in range(num_dice)]
    await ctx.send(f"擲出的骰子數字：{results}, 總和：{sum(results)}")

bot.run("TOKEN")