#!/usr/bin/python3

import i3ipc
import time

i3 = i3ipc.Connection()

def main():
    do_cmd("split v")
    do_cmd("exec i3-sensible-terminal")
    do_cmd("focus up")
    do_cmd("split v")
    do_cmd("layout tabbed")
    do_cmd("exec i3-sensible-terminal")
    do_cmd("exec i3-sensible-terminal")
    do_cmd("focus left")
    do_cmd("focus left")

def do_cmd(command):
    #python shit async
    i3.command(command)
    time.sleep(.1)

main()
