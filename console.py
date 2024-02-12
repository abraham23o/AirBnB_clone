#!/usr/bin/python3
"""

"""
import cmd
import re

from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class to define the HolbertonBNB command interpreter
    """
    prompt = "(hbnb) "

    __classes = {
        "BaseModel"
    }

    def do_EOF(self, line):
        """
        EOF signal to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def split_(self, line):
        """
        tokenization - split line into substrings based on double
        quotes and spaces
        """
        regex = r'("[^"]+"|\{[^}]*\}|\S+)'
        result = re.findall(regex, line)
        for i in range(len(result)):
            try:
                value = eval(result[i])
                if type(value) in (int, float, str, dict):
                    result[i] = value
            except (SyntaxError, NameError, TypeError):
                continue
        return result

    def emptyline(self):
        """
        Do nothing upon receiving an empty line
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        words = self.split_(line)
        if not words:
            return print("** class name missing **")
        clas = words[0]
        if clas not in self.__classes:
            return print("** class doesn't exist **")
        obj = eval(clas)()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        words = self.split_(line)
        if not words:
            return print("** class name missing **")
        if words[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(words) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(words[0], words[1])
        new_instance = storage.all().get(key)
        if not new_instance:
            return print("** no instance found **")
        print(new_instance)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into
        the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        words = self.split_(line)
        if not words:
            return print("** class name missing **")
        if words[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(words) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(words[0], words[1])
        new_instance = storage.all().get(key)
        if not new_instance:
            return print("** no instance found **")
        del new_instance
        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class
        name. Ex: $ all BaseModel or $ all
        """
        words = self.split_(line)
        if not words:
            return print([str(new_instance) for k, new_instance in
                          storage.all().items()])
        clas = words[0]
        if clas not in self.__classes:
            return print("** class doesn't exist **")
        new_instances = [str(new_instance) for k, new_instance in storage.all().items()
                         if k.startswith("{}.".format(clas))]
        print(new_instances)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email
        "aibnb@mail.com"
        """
        words = self.split_(line)
        if not words:
            return print("** class name missing **")
        if words[0] not in self.__classes:
            return print("** class doesn't exist **")
        if len(words) < 2:
            return print("** instance id missing **")
        key = "{}.{}".format(words[0], words[1])
        new_instance = storage.all().get(key)
        if not new_instance:
            return print("** no instance found **")
        if len(words) < 3:
            return print("** attribute name missing **")
        kwargs = {}
        if type(words[2]) is dict:
            kwargs = words[2]
        if not kwargs and len(words) < 4:
            return print("** value missing **")
        if not kwargs:
            kwargs = {words[2] : words[3]}
            for k, v in kwargs.items():
                setattr(new_instance, k, v)
            new_instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
