#!/usr/bin/python3
""" contains module console """


import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Defines the class and methods used to
    execute operations on the json file
    """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel,
               'User': User,
               'State': State,
               'City': City,
               'Amenity': Amenity,
               'Place': Place,
               'Review': Review
               }

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Exits console """
        return True

    def emptyline(self):
        """ moves to next line when 'enter' is pressed """
        return False

    def do_create(self, arg):
        """
        creates a new instance

        Usage: create <classname>
        """
        command = shlex.split(arg)

        if len(command) == 0:
            print("** class name missing **")
        else:
            if command[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, value in self.classes.items():
                    if key == command[0]:
                        inst = value()
                        inst.save()
                        print(inst.id)

    def do_show(self, arg):
        """
        prints string representation of an instance
        based on the class name and id

        Usage: show <classname> <id>
        """
        command = shlex.split(arg)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = command[0] + '.' + command[1]

            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Usage: destroy <classname> <id>
        """
        command = shlex.split(arg)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = command[0] + '.' + command[1]

            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name

        Usage: all or all <classname>
        """
        command = shlex.split(arg)
        obj = storage.all()

        if len(command) == 0:
            for key, value in obj.items():
                print([str(value)])
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in obj.items():
                name = key.split('.')[0]
                if name == command[0]:
                    print([str(value)])

    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        command = shlex.split(arg)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = command[0] + '.' + command[1]

            if key not in obj:
                print("** no instance found **")
            elif len(command) < 3:
                print("** attribute name missing **")
            elif len(command) < 4:
                print("** value missing **")
            else:
                obj_dict = obj[key]
                attr_name = command[2]
                attr_value = command[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass

                setattr(obj_dict, attr_name, attr_value)
                obj_dict.save()

    def default(self, arg):
        """ overrides the default command in cmd module """
        args = arg.split('.')
        command = args[1].split('(')
        command_1 = command[1].split(')')[0]
        attributes = command_1.split(',')

        commands = {'all': self.do_all,
                    'show': self.do_show,
                    'update': self.do_update,
                    'count': self.do_count,
                    'destroy': self.do_destroy
                    }

        if command[0] in commands.keys():
            if command[0] != 'update':
                return commands[command[0]](f'{args[0]} {command_1}')
            else:
                command_2 = attributes[0]
                command_3 = attributes[1]
                command_4 = eval(attributes[2])
                return commands[command[0]](
                    f'{args[0]} {command_2} {command_3} {command_4}')

        print(f'*** Uknown syntax: {arg}')
        return False

    def do_count(self, arg):
        """ counts the no of instances in a class """
        arg_list = shlex.split(arg)
        command = arg_list[0]
        objects = storage.all()
        count = 0

        if arg_list:
            if command in self.classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == command:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
