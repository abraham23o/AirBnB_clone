#!/usr/bin/python3
"""

"""
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """
    class to define the HolbertonBNB command interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """
        EOF signal to exit the program
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing upon receiving an empty line
        """
        pass

    def _split(self, arg):
        """
        split line into substrings based on double
        quotes and spaces
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
