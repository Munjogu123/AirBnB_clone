#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def emptyline(self):
       pass

    do_EOF = do_quit
    help_EOF = help_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
