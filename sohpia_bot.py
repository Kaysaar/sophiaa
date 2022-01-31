import os
import hikari
import lightbulb
from HelpHandler import Custodian


with open("./Secret/token") as tok:
    _token = tok.read().strip()
    
GUILD_ID= [870732066147401778]
STDOUT_CHANNEL_IP=937690282118512640

sophia = lightbulb.BotApp(
    token=_token,
    prefix="/",
    default_enabled_guilds=GUILD_ID,
    intents=hikari.Intents.ALL,
    help_class=Custodian,
    help_slash_command=True

)

@sophia.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent) -> None:
    channel = (await sophia.rest.fetch_channel(STDOUT_CHANNEL_IP))
    await channel.send("S.O.P.H.I.A Initialization")

@sophia.listen()
async def starting_load_extensions(_: hikari.StartingEvent) -> None:
    sophia.load_extensions("music")



if __name__ == '__main__':
    if os.name != 'nt':
        import uvloop

        uvloop.install()

sophia.run()
