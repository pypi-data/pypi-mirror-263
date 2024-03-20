#!/usr/bin/env python3

from fire import Fire
import sys
from codeframe.version import __version__
from codeframe import config

KNOWN_COMMANDS = ['ls','load','zoom','unzoom','connect']

def main( cmd ):
    kw1 = cmd.split()[0]
    if not kw1 in KNOWN_COMMANDS:
        print(f"X... unknown command /{cmd}/      ")
        return
    match kw1:
        case 'ls':
            print("LS:",cmd,"    ")
            return 1
        case 'load':
            print("LOAD:",cmd,"    ")
            return 2
        case 'zoom':
            print("ZOOM:",cmd,"    ")
            return 2
        case 'unzoom':
            print("UNZOOM:",cmd,"    ")
            return 2
        case 'connect':
            print("CONNECT:",cmd,"    ")
            return 2
        case _:
            return 0   # 0 is the default case if x is not found
    pass
    #print()

if __name__=="__main__":
    Fire(main)
