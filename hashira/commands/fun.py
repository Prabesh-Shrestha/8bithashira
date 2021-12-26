import lightbulb
import hikari 
import hashira
import random 
fun_plug = lightbulb.Plugin("fun")
fun_plug.description = f'''
pp: 
shows that member's pp size
>pp @user
'''


@fun_plug.command()
@lightbulb.option("member", "member", type=hikari.Member)
@lightbulb.command("pp", "shows the pp size")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def pp_size(ctx: lightbulb.Context):
    member = ctx.options.member
    size = f'B{"="*random.randint(1,10)}D'
    embed = hikari.Embed(title=f"{member}'s pp")
    embed.add_field(name=':',value=size)
    embed.set_footer(icon=member.avatar_url, text=str(member))
    await ctx.respond(embed=embed)


def load(bot):
    bot.add_plugin(fun_plug)

def unload(bot):
    bot.remove_plugin(fun_plug)
