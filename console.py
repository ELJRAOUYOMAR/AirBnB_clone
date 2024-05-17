#!/usr/bin/python3
"""

"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage 

class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_quit(self, argument):
        """command to exit the program"""
        return True
    
    def do_EOF (self, argument):
        """EOF (Ctrl+D) signal to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) 
        and prints the id. Ex: $ create BaseModel
        -If the class name is missing, print ** class name missing ** (ex: $ create)
        -If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)
        
        shlex class makes it easy to write lexical analyzers for simple
        syntaxes resembling that of the Unix shell.s
        """
        
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes: 
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{args[0]}()")
            storage.save()
            print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
