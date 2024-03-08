<h1 align="center">AirBnB Clone</h1>

## A clone of the AirBnB app with a console to help in executing some of the commands!

This project is meant to help understand and cover some fundamental concepts of the higher level programming track.

At the end of the entire project we would have composed:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Here's a diagram overview of the entire project
![AirBnB2](https://github.com/Munjogu123/AirBnB_clone/assets/116668797/31670531-8671-4a5c-b51f-405218163092)

## The Command Interpreter
1. How to start the command interpreter

    `./console.py`

    or

    `python3 console.py`

2. How to use the command interpreter

    * To create a new instance

        `create <classname>`

    * To print a string representation of an instance based on class name and id

        `show <classname> <id>`

    * To delete an instance based on the class name and id

        `destroy <classname> <id>`

    * To print all string representations of all instances based or not on the class name

        `all`

        or 

        `all <classname>`

    * To update an instance based on the class name and id by adding or updating attribute

        `update <class name> <id> <attribute name> "<attribute value>"`

    * To quit type

        `quit`