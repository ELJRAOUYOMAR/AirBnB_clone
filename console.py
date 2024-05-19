#!/usr/bin/python3
"""
command line code.
you can use your own command line for CRUD operation, that's all!   ko
"""
import cmd
import shlex
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage 


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "
    class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, argument):
        """command to exit the program"""
        return True
    
    def help_quit(self):
        """  """
        print("Quit command to exit the program\n")
    
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
        syntaxes resembling that of the Unix shell.
        """
        args = shlex.split(arg)

        if not args:
            print("** class name missing **")
        elif args[0] not in self.class_mapping: 
            print("** class doesn't exist **")
        else:
            """new_instance = eval(f"{args[0]}()")"""
            new_instance = self.class_mapping[args[0]]()
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        -If the class name is missing, print ** class name missing ** (ex: $ show)
        -If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ show MyModel)
        -If the id is missing, print ** instance id missing ** (ex: $ show BaseModel)
        -If the instance of the class name doesn’t exist for the id, print ** no instance 
         found ** (ex: $ show BaseModel 121212)
        """
        args = shlex.split(arg)

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_mapping:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])
    
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        -If the class name is missing, print ** class name missing ** (ex: $ destroy)
        -If the class name doesn’t exist, print ** class doesn't exist ** (ex:$ destroy MyModel)
        -If the id is missing, print ** instance id missing ** (ex: $ destroy BaseModel)
        -If the instance of the class name doesn’t exist for the id, 
         print ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        args = shlex.split(arg)

        if not arg:
            print("** class name missing **")
        elif args[0] not in self.class_mapping:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in objs:
                print("** no instance found **")
            else:
                del objs[key]
                storage.save()
    
    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all
        -The printed result must be a list of strings (like the example below)
        -If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ all MyModel)
        """
        objs = storage.all()
        args = shlex.split(arg)

        if len(args) == 0:
            for key, value in objs.items():
                print(str(value))
        elif args[0] not in self.class_mapping:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                if key.split('.')[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        - If the class name is missing, print ** class name missing **
        - If the class name doesn’t exist, print ** class doesn't exist **
        - If the id is missing, print ** instance id missing **
        - If the instance of the class name doesn’t exist for the id, print ** no instance found **
        - If the attribute name is missing, print ** attribute name missing **
        - If the value for the attribute name doesn’t exist, print ** value missing **
        """
        args = shlex.split(arg)
        
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.class_mapping:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name, instance_id, attribute_name, attribute_value = args[0], args[1], args[2], args[3]
        
        """Find the instance"""
        objs = storage.all()
        key = f"{class_name}.{instance_id}"
        
        if key not in objs:
            print("** no instance found **")
            return

        instance = objs[key]
        
        """Cast the attribute value to the correct type."""
        attribute_type = type(getattr(instance, attribute_name, str))
        if attribute_type is int:
            attribute_value = int(attribute_value)
        elif attribute_type is float:
            attribute_value = float(attribute_value)
        
        setattr(instance, attribute_name, attribute_value)
        instance.save()
        print(instance)

    def do_count(self, class_name):
        """Retrieve the number of instances of a class."""
        objs = storage.all()
        
        if class_name not in self.class_mapping:
            print("** class doesn't exist **")
            return

        count = sum(1 for key in objs if key.split('.')[0] == class_name)
        print(count)

    def default(self, line):
        """
        Catches commands not explicitly handled.
        Handles <class name>.all(), <class name>.show(<id>), <class name>.destroy(<id>),
        and <class name>.update(<id>, <attribute name>, <attribute value>) method calls.
        """
        args = line.split('.')
        
        if len(args) == 2:
            class_name = args[0]
            method_call = args[1]
            if class_name in self.class_mapping:
                if method_call == "all()":
                    self.do_all(class_name)
                elif method_call.startswith("show(") and method_call.endswith(")"):
                    id = method_call[5:-1]
                    self.do_show(f"{class_name} {id}")
                elif method_call.startswith("destroy(") and method_call.endswith(")"):
                    id = method_call[8:-1]
                    self.do_destroy(f"{class_name} {id}")
                elif method_call == "count()":
                    self.do_count(class_name)
                elif method_call.startswith("update(") and method_call.endswith(")"):
                    args = method_call[7:-1].split(', ')
                    if len(args) == 3:
                        self.do_update(f"{class_name} {args[0]} {args[1]} {args[2]}")
                    else:
                        print("*** Unknown syntax:", line)
                else:
                    print("*** Unknown syntax:", line)
            else:
                print("*** Unknown syntax:", line)
        else:
            print("*** Unknown syntax:", line)
        
    """
    def cast_value(self, attr_name, value, obj):
        '''Casts the value to the correct type based on the attribute's current type.'''
        current_value = getattr(obj, attr_name, None)
        
        if current_value is None:
            return value  # Fallback to string if attribute does not exist
        if isinstance(current_value, int):
            return int(value)
        elif isinstance(current_value, float):
            return float(value)
        return value
    """
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
