import discord
from discord.ext import commands
from googletrans import Translator

bot = discord.Client()
bot = commands.Bot(command_prefix = '?')
bot.remove_command('help')

langc = ['en']
print(langc[0])

@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed=discord.Embed()
            embed.set_author(name='TranslatorBot help page',icon_url='https://cdn.discordapp.com/attachments/700737308189523969/741973242188922940/worldwide.png')   
            embed.add_field(name='Use `?lang` to pick server-wide language. After that simply start translating using   `?translate` or `?t` and you\'re good to go! Stay safe out there!', value= 'Check out the [official page](https://top.gg/bot/741909258878058546) to learn more about LanguageBot.', inline=False)
            await channel.send(embed=embed)
        break

@bot.command(aliases = ['t'])
async def translate(ctx, *, uinput = None):

    translator = Translator()
    text = str(uinput)
    try:
        translation = translator.translate(text, dest=str(langc[0]))
    except:
        await ctx.send('Language `' + langc[0] + '` does not exist, double check the languages with `!list`🌍')

    author_mention =ctx.message.author.mention
    author = ctx.message.author

    embed=discord.Embed()
    embed.set_author(name=str(author)[:-5],icon_url=author.avatar_url)   
    embed.add_field(name=translation.text + '   *(' + langc[0] + ')*', value='Translation of ' + '"' + text + '"', inline=False)
    msg = await ctx.send(embed=embed)
    await ctx.message.delete()
    await msg.add_reaction('🌍')
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')


@bot.command(aliases = ['l', 'language'])
async def lang(ctx, language = None):

    with open('languages.txt', 'r') as f:
        if language == None:
            language = 'en'
            langc[0] = language
            await ctx.send('Language has been set to `' + str(language) + '`👍')
        elif language in f.read():
            await ctx.send('Language has been set to `' + str(language) + '`👍')
            langc[0] = language
        elif language not in f.read():
            await ctx.send('Language `' + language + '` does not exist, double check the languages with `!list`🌍')
        await ctx.message.delete()

@bot.command(aliases=['list'])
async def ls(ctx):

    embed=discord.Embed()
    embed.set_author(name='List of supported countries',icon_url='https://cdn.discordapp.com/attachments/700737308189523969/741973242188922940/worldwide.png')   
    embed.add_field(name='TranslatorBot supports over a hundrer different languages, simply pick one of them and type in `?lang [your choice]`. Happy translating!', value= 'Use the [country codes](https://cloud.google.com/translate/docs/languages) to pick the server-wide language.', inline=False)
    msg = await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def help(ctx):

    embed=discord.Embed()
    embed.set_author(name='TranslatorBot help page',icon_url='https://cdn.discordapp.com/attachments/700737308189523969/741973242188922940/worldwide.png')   
    embed.add_field(name='Use `?lang` to pick server-wide language. After that simply start translating using   `?translate` or `?t` and you\'re good to go! Stay safe out there!', value= 'Check out the [official page](https://top.gg/bot/741909258878058546) to learn more about LanguageBot.', inline=False)
    msg = await ctx.send(embed=embed)
    await ctx.message.delete()


bot.run('TOKEN')
