#!/usr/bin/python3
"""

"""
import cmd
from models.base_model import BaseModel


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

    def create(self):
        """Creates a new instance of BaseModel, saves it (to the JSON file) 
        and prints the id. Ex: $ create BaseModel
        -If the class name is missing, print ** class name missing ** (ex: $ create)
        -If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        """
        base_model = BaseModel()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
