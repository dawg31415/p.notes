#!/bin/python

import argparse

def init() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog = 'notes',
        description = '<encrypted>',
    )
    
    parser.add_argument('command',
        choices=['init', 'view', 'add'],
        help=
        """
        init     :   (BE CAUTIOUS) init / re-init notes .json
        view     :   view existing notes
        add      :   add a note
        """
    )
    # init
    parser.add_argument('-nc', '--no-copy', 
        help = "init: override existing .json",
        action = 'store_true',
    )
    parser.add_argument('-bk', '--back-up', 
        help = "init: make backup of existing .json",
        action = 'store_true',
    )
    # view
    parser.add_argument('-tm', '--tomorrow', 
        help = "view notes of tomorrow",
        action = 'store_true',
    )
    parser.add_argument('-ys', '--yesterday', 
        help = "view notes of yesterday",
        action = 'store_true',
    )
    # add
    parser.add_argument('-n', '--name', 
        help = "new note's name",
    )
    parser.add_argument('-c', '--content', 
                        help = "new note's content",
    )
    parser.add_argument('-t', '--time', 
                        help = "new note's time . format : {hh:mm}",
    )

    return parser


def syntaxis_check(args: argparse.Namespace) -> None:
    args_list = vars(args).values()
    for arg in args_list:
        if not arg or type(arg) is not str: continue
        if arg.lower() != arg:
            raise(ValueError, "args has to be lower.case")


def validate_arguments(args: argparse.Namespace) -> ValueError:
    # TODO make or remove
    pass

def parse_args() -> (str, str):
    parser = init()
    args = parser.parse_args()

    syntaxis_check(args)
    validate_arguments(args)

    view = args.command == 'view' 
    initcmd = args.command == 'init' 

    to_return = ('view', args.tomorrow, args.yesterday) if view else ('add', args.time, args.name, args.content)
    if initcmd: to_return = ('init', args.no_copy, args.back_up)

    return to_return
