from discord.ext import commands

bot = commands.Bot(command_prefix='ch!')


@bot.command(name='math')
async def math(ctx, *args):
        await ctx.send(str(eval(str(" ".join(args)))))


@math.error
async def info_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('Solo puedes ingresar números enteros')


bot.run(open('TOKEN.txt', 'r').read())
