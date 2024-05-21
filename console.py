#!/usr/bin/python3
"""Module for HBNBCommand class."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
