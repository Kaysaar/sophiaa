import lightbulb
class Custodian(lightbulb.DefaultHelpCommand):
    async def send_bot_help(self, context):
        lines = [
            ">>> ```adoc",
            "====   S.O.P.H.I.A   ====",
            "Welcome",
            f"How can i Serve you today? ",
            ""
            f"If you want to get inforamtion about command use:\n"
            ""
            f"{context.prefix}help command",
            f"np: {context.prefix}help ping",
            "====   Have a Nice day    ===="
            "```",

        ]
        pages = "\n".join(lines)

        await context.respond(pages)

    async def send_command_help(self, context, command):
        long_help = command.get_help(context)

        lines = [
            ">>> ```adoc",
            "==== Iniciate Custodes Protocol ====",
            f"{command.name} - {command.description}",
            "",
            f"Usage: {context.prefix}{command.signature}",
            "",
            long_help if long_help else "There are no futher informations.",
            "==== Protocol Closed ===="
            "```",
        ]
        pages = "\n".join(lines)
        await context.respond(pages)


