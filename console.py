#!/usr/bin/python3
"""
The console, to manage everything
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Contains functionality of the console"""
    intro = 'Welcome to the interpreter! Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def do_create(self, line):
        """Creates a new object"""
        if not line:
            print("**PLease write the name of the class")
        elif line not in HBNBCommand.classes.keys():
            print("Class does not exist")
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_update(self, line):
        """Updates attributes of an object"""

    def do_destroy(self, line, args):
        """Destroys an object"""

        obj_list = []
        if len(line) == 0:
            for objs in storage.all().values():
                obj_list.append(objs)
                print(obj_list)
        elif args[0] in HBNBCommand.classes:
            for key, objs in storage.all().items():
                if args[0] in key:
                    obj_list.append(objs)
                    print(obj_list)
        else:
            print("class doesnt exist")

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_operations(self, args):
        """Do operations on objects"""
        print("Choose operation to use on object")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        return True

    def do_quit(self, args):
        """Quits the interpreter"""
        print("Goodbye!")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
