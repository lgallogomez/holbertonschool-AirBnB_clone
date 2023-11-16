import cmd
import string, sys

class CLI(cmd.Cmd):

    prompt = "cli:"

    def do_quit(self, arg):
        sys.exit(1)



if __name__ == "__main__":
    CLI().cmdloop()