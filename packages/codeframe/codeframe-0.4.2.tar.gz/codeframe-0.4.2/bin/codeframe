#!/usr/bin/env python3

# to override print <= can be a big problem with exceptions
#
# colors in df_table _fg _bg columns:
# see
# https://github.com/mixmastamyk/console/blob/master/console/color_tables_x11.py#L112
#
# from __future__ import print_function  # must be 1st
# import builtins
import sys
from fire import Fire
from codeframe.version import __version__
# from codeframe import unitname
from codeframe import config
from codeframe import topbar
from codeframe import key_enter
from codeframe import installation
# from codeframe  import df_table
from codeframe.df_table import create_dummy_df, show_table, \
    inc_dummy_df, move_cursor
from codeframe import mmapwr
from codeframe import interpreter

import time
import datetime as dt
from console import fg, bg, fx
from blessings import Terminal
import os
from pyfiglet import Figlet
import signal

# ====================== for separate terminal keyboard using mmap

from prompt_toolkit import PromptSession, prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

# ========================
SHOW_LOGO_TABLE = True
SHOW_COMMAND_LINE = True
RUN_MMAP_INPUT = True
RUN_SELECT_FROM_TABLE = False

# import pandas as pd
# import numpy as np
# from terminaltables import SingleTable

# ------- this defended the project from winch error
# from simple_term_menu import TerminalMenu


def handle_sigwinch(signum: signal.Signals, qqq):
    # pylint: disable=unused-argument
    # print(type(qqq), qqq)
    return None


# ----this DOES IT
#  for FONTS in `pyfiglet -l`; do echo $FONTS; pyfiglet $FONTS -f $FONTS; done | less
figlet = Figlet(font="slant")
# figle2 = Figlet(font="roman")
# figle2 = Figlet(font="standard")
figle2 = Figlet(font="ansi_regular")


def print_logo():
    """
    print fromt page + time
    """
    # global figlet, filg
    termsize = os.get_terminal_size().columns

    word = " codeframe"
    # os.system('reset')
    print("")
    print(figlet.renderText(word))
    print(figle2.renderText(dt.datetime.now().strftime("%H:%M:%S ")))
    print(
        f"installation: do you want to install me?... Run me with your  \
{fg.green}'projectname'{fg.default} as a parameter"
    )
    print("do you want to quit    me? (q)")
    print(f"    terminal width = {termsize} ")


def main(projectname=None, debug=False, keyboard_mode = False):
    """
    Main function of the project. When 'projectname' given: new project is created
    """

    # GLobal clear terminal
    if debug:
        print(__version__)
    else:
        os.system("reset")

    signal.signal(signal.SIGWINCH, handle_sigwinch)

    # ======== DEFINE THE CONFIG FILE HERE ========

    config.CONFIG["filename"] = "~/.config/codeframe/cfg.json"
    config.CONFIG["history"] = "~/.config/codeframe/history"
    # solely LOAD will create ....from_memory files
    # config.load_config()
    # solely  SAVE will create cfg.json only
    # config.save_config()

    # ==================================================== #########################
    if keyboard_mode:
        prompt_completer = WordCompleter( interpreter.KNOWN_COMMANDS )
        multilineinput = False
        config.myPromptSession = PromptSession(
            history=FileHistory( os.path.expanduser(config.CONFIG["history"]) )
        ) #, multiline=Trueinp
        inp = ""
        while (inp!="q"):
            inp = config.myPromptSession.prompt("> ",
                                                multiline=multilineinput,
                                                completer=prompt_completer,
                                                complete_while_typing=False,
                                                wrap_lines=True, # no noew lines
                                                mouse_support=False,  # i want middlemouse
                                                auto_suggest=AutoSuggestFromHistory()
                                                )
            mmapwr.mmwrite(inp)
        # print(inp)
        return
    # ==================================================== #########################


    if projectname is None:
        print()
    elif projectname == "usage":
        print(
            """ ... usage:
            _
        """
        )
        sys.exit(0)
    # ----------------------- installation with this name ----------
    else:
        installation.main(projectname)
        sys.exit(0)

    # ===================== top bar and commads from kdb ==========

    top = topbar.Topbar(bgcolor=bg.blue)
    top2 = top.add(bgcolor=bg.black)

    top.print_to(
        10,
        f" {fg.white}{fx.bold}{dt.datetime.now().strftime('%H:%M:%S')}\
{fx.default}{fg.default} ",
    )
    top.place()
    # start after top

    # ========================= INITIAL cmd key setting....
    cmd = ""
    enter = False
    key = None
    a, b = (" ", " ")

    # KEYTHREAD THIS MUST BE HERE.....toi catch 1st letter
    #   only return         key, enter, abc = kthread.get_global_key()
    #                       key:mayreact on q;     enter==hit ; abc=>(a,b) for display.
    kthread = None
    if RUN_MMAP_INPUT:
        kthread = key_enter.MmapSimulatedKeyboard(ending="q")
    else:
        kthread = key_enter.KeyboardThreadSsh(ending="q")
    #
    # whatabout to have other terminal feeding mmapfile
    #

    df = create_dummy_df()
    terminal = Terminal()
    selection = None
    while True:  # ================================= LOOP
        termsize = os.get_terminal_size().columns

        if (SHOW_LOGO_TABLE):
            terminal.clear()
            move_cursor(2, 9)
            print_logo()

            # time.sleep(0.05)
            show_table(df, selection)
        df = inc_dummy_df(df)

        key, enter, abc = kthread.get_global_key()
        (a, b) = abc  # unpack tuple

        if enter:
            print()
            print("--------------------------------------ENTER pressed")
            if len(key.strip()) == 0:
                pass
            elif key.strip() == "q":
                break
            else:
                cmd = key.strip()
                # ======================================================== INTERPRETER
                interpreter.main( cmd )
                if RUN_SELECT_FROM_TABLE:
                    # list of row numbers from column 'n' :  assume whole word is list of rows:
                    if selection is not None and selection != "":
                        selection = ""
                    else:
                        selection = cmd
                # ======================================================== INTERPRETER
            print(f"----------------------- {cmd} sel:{selection}--------------------- ***")
        else:
            cmd = ""

        termsize = os.get_terminal_size().columns
        top.print_to(
            10,
            f" {fg.white}{fx.bold}{dt.datetime.now().strftime('%H:%M:%S')}\
{fx.default}{fg.default}",
        )

        #
        #  commandline at TOP#2, cursor  a_b; option not to show
        #
        if (not SHOW_COMMAND_LINE) or (  (key is not None) and (len(key) == 0) ):
            top2.print_to(0, f"{fg.cyan}{bg.black}{' '*termsize}{bg.black}")
        else:
            top2.print_to(
                0,
                f"{fg.white}{bg.red} > {fx.bold}{a}{fg.yellow}_{fg.white}{b}\
{fx.default}{fg.default}{bg.default} ",
            )

        # PLACE THE TOPBAR INPLACE
        top.place()
        time.sleep(0.1)


# ====================================================================


if __name__ == "__main__":
    Fire(main)
