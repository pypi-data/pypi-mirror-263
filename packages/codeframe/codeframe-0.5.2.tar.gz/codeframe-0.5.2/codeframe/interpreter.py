#!/usr/bin/env python3

from fire import Fire
import sys
from codeframe.version import __version__
from codeframe import config
import os
from codeframe.config import  move_cursor
import subprocess as sp
from console import fg,bg
import glob

KNOWN_COMMANDS = ['ll','ls','load','zoom','unzoom','connect','reset']


def exclude(cmd=""):
    bad = False
    if cmd.find("&")>=0:  bad = True
    if cmd.find("|")>=0:  bad = True
    if cmd.find("'")>=0:  bad = True
    if cmd.find('$')>=0:  bad = True
    if cmd.find('%')>=0:  bad = True
    if cmd.find('#')>=0:  bad = True
    if cmd.find('!')>=0:  bad = True
    if cmd.find('(')>=0:  bad = True
    if cmd.find(')')>=0:  bad = True
    if cmd.find(';')>=0:  bad = True
    #if cmd.find('"')>=0:  die() # for sed

    if bad:
        print( f"{fg.white}{bg.red}X... not allowed char in {cmd}", fg.default,bg.default)
    return bad

# =========================================================
#   shell (True or False...check it) run of the commands. with some basic protection
# =========================================================
def run_or_die( cmd , debug = False):
    #print()
    res = 0
    # if type(cmd)==list:
    #     print("i... LIST cmd .... unexpected....")
    #     try:
    #         if debug:  print("exe...", cmd)
    #         res = sp.check_call( cmd , shell = True)
    #     except:
    #         res= 1
    #         print(f"X... {fg.red} error running /{bg.white}{cmd}{bg.default}/{fg.default}")
    # if res != 0: die("")

    if exclude(cmd): return
    res = 0
    #print()
    try:
        if debug: print("Exe...", cmd)
        cmd2 = cmd.split()
        for i in range(len(cmd2)):
            #print(i, cmd2[i])
            cmd2[i] = cmd2[i].strip('"')
        newcmd = []
        newcmd.append( cmd2[0] )
        for i in range(1,len(cmd2)):
            # print(">>>",cmd2[i] )
            if '*' in cmd2[i]:
                for j in glob.glob( cmd2[i] ):
                    newcmd.append(j)
            else:
                newcmd.append(cmd2[i])
        #print(cmd2)
        if debug: print("Exe...",  newcmd)
        res = sp.check_call( newcmd )#, shell = True)
        if debug: print("ok",res)
    except:
        res =1
        print(f"X... {fg.red} error running /{bg.white}{cmd}{bg.default}/{fg.default}")
    #print()
    #if res != 0: die("")
# =========================================================

def termline(txt):
    termsize3 = os.get_terminal_size().columns
    cont = f"#... ________ {txt} "
    cont = cont + "_"*(termsize3 - len(cont)-2)
    print(f"{fg.orange}{cont}{fg.default}")


def main( cmd ):
    kw1 = cmd.split()[0]
    kw2 = " ".join(cmd.split()[1:])
    if not kw1 in KNOWN_COMMANDS:
        print(f"{fg.red}X... unknown command /{cmd}/    {fg.default}")
        return
    termline(cmd)
    match kw1:
        case 'reset':
            #print("RESET:",cmd,"    ")
            os.system("reset")
            move_cursor(3,1)
            return 1
        case 'ls':
            run_or_die(cmd)
            return 1
        case 'll':
            run_or_die("ls -l "+kw2)
            return 1
        case 'load':
            #print("LOAD:",cmd,"    ")
            return 2
        case 'zoom':
            #print("ZOOM:",cmd,"    ")
            return 2
        case 'unzoom':
            #print("UNZOOM:",cmd,"    ")
            return 2
        case 'connect':
            #print("CONNECT:",cmd,"    ")
            return 2
        case _:
            return 0   # 0 is the default case if x is not found
    pass
    #print()

if __name__=="__main__":
    Fire(main)
