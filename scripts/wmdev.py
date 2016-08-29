#!/usr/bin/python3

import i3ipc
import time
import os
from argparse import ArgumentParser

i3 = i3ipc.Connection()

def main():
    parser = ArgumentParser()
    parser.add_argument('-d');
    args = parser.parse_args()
    path = args.d;
    if path is None:
        path = os.getcwd()
    
    do_cmd("split v")
    do_cmd("exec i3-sensible-terminal -cd " + path)
    do_cmd("split v")
    do_cmd("layout tabbed")
    do_cmd("exec i3-sensible-terminal -cd " + path)
    do_cmd("exec i3-sensible-terminal -cd " + path)
    do_cmd("exec i3-sensible-terminal -cd " + path)
    do_cmd("focus up")
    do_cmd("split v")
    do_cmd("layout tabbed")
    do_cmd("exec i3-sensible-terminal -cd " + path)
    do_cmd("exec i3-sensible-terminal -cd " + path)
    do_cmd("exec i3-sensible-terminal -cd " + path)
    do_cmd("focus left")
    do_cmd("focus left")

def do_cmd(command):
    #I am ignorant on how to do python async, so here is some shit code
    i3.command(command)
    time.sleep(.1)

main()
