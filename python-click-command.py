#!/usr/bin/env python3
#
# python-click-command
#
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
# tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
# consequat.
#
import click


@click.command(context_settings=dict(help_option_names=["-h", "-?", "--help"]))
@click.option(
    "--argument",
    "-a",
    default="default_value",
    show_default=True,
    help="argument flag with long and short options",
)
@click.option(
    "--thing/--no-thing",
    default=False,
    help="Boolean option that defaults to False",
)
def main(argument, thing):
    pass


if __name__ == "__main__":
    main()
