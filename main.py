


# ##################################################################################################################################
# ##################################################################################################################################
# IMPORT:

import numpy as np
import matplotlib.pyplot as plt

import modules.visualize as visualize

# ##################################################################################################################################
# ##################################################################################################################################
# VARIABLES:
ACTIVE = True

FIGURES = {}

# ##################################################################################################################################
# ##################################################################################################################################
# MAIN:

def main():
    
    while ACTIVE:
        inp = input("< ")
        cmd = process_command_line(inp)

        if cmd[0] in COMMANDS:
            print('args', cmd[1:])
            COMMANDS[cmd[0]](cmd[1:])
        else:
            print("unknown command")

# ##################################################################################################################################
# ##################################################################################################################################
# VARIABLKES:


# ##################################################################################################################################
# ##################################################################################################################################
# METHODS:

def process_command_line(line):
    return line.split(" ")

def help_command(args):
    print(f'help: {str(args)}')
    for cmd in COMMANDS:
        print(f'- {cmd}')

def exit_command(args):
    global ACTIVE
    print("EXIT")
    ACTIVE = False



def creat_figure(args:list):

    if len(args) < 1:
        title = f'figure{str(len(FIGURES))}'
    else:
        title = str(args[0])
    
    print(f'opening new window: {title}')
    fig, axes = visualize.creat_figure(title=title)
    FIGURES[title] = fig
    return 0


def load_image(args):
    if len(args) < 2:
        print('filename and figure name is needed !!!')
        return 1
    
    filepath = args[0]
    figname = args[1]

    fig = FIGURES[figname]
    axes = fig.axes
    visualize.load_image(filepath, fig, axes[0])

    return 0

# ##################################################################################################################################
# ##################################################################################################################################
COMMANDS = {'help': help_command, 'exit':exit_command, 'FIGURE':creat_figure, 'IMAGE':load_image}

if __name__ == '__main__':
    main()