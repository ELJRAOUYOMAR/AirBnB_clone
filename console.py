#!/usr/bin/python3
"""

"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "

    def do_quit(self, argument):
        """command to exit the program"""
        return True
    
    def do_EOF (self, argument):
        """EOF (Ctrl+D) signal to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
