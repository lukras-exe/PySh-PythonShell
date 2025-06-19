"""PySh: a simple shell written in Python"""

import os
import subprocess
import shutil


def execute_command(command):
    """execute commands and handle piping"""
    try:
        if "|" in command:
            # save for restoring later on
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            # first command takes commandut from stdin
            fdin = os.dup(s_in)

            # iterate over all the commands that are piped
            for cmd in command.split("|"):
                # fdin will be stdin if it's the first iteration
                # and the readable end of the pipe if not.
                os.dup2(fdin, 0)
                os.close(fdin)

                # restore stdout if this is the last command
                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                # redirect stdout to pipe
                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print("psh: command not found: {}".format(cmd.strip()))

            # restore stdout and stdin
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split(" "))
    except Exception:
        print("psh: command not found: {}".format(command))


def sh_cd(path=None): #change directory
    """Change directory, default to home if no path provided"""
    try:
        os.chdir(path)
    except Exception:
        print("cd: no such file or directory: {}".format(path))


def sh_help(): #print help/man page
    print("""\
    
    
    PySh - A simple shell implementation in Python
    Supports all basic shell commands.
    
    Usage: 
        [command] [arguments] 
    
    Built-in Commands:
        help/man        Show this help/manual message
        exit            Exit the shell
        cd [dir]        Change the current directory
        pwd             Print the current working directory
        ls [dir]        List files iand directories (like Unix 'ls')
        mkdir [dir]     Create a new directory
        rm [dir]        Remove a file or directory
        
    Notes:
        - This shell supports simple piping: ls | grep keyword
        - Most external commands (ssh, ping, etc..) work if available in your system
        - There is currently no support for flags in commands

    Type 'exit' to quit.
    
    
    """)
          

def sh_pwd(): 
    """Print current working directory"""
    print(os.getcwd())
    
def sh_ls(path="."):
    try:
        items = os.listdir(path)
        items.sort()
        for item in items:
            if not item.startswith("."):  # Skip hidden files (like Bash default)
                print(item, end="\t")
        print()
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")
    except NotADirectoryError:
        print(path)
    except Exception as e:
        print(f"ls: error: {e}")
    
def sh_mkdir(path):
    """Create a new directory at the given path"""
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"mkdir: cannot create directory '{path}': File exists")
    except FileNotFoundError:
        print(f"mkdir: cannot create directory '{path}': No such file or directory")
    except Exception as e:
        print(f"mkdir: error: {e}")
        
def sh_rm(path, recursive=False):
    """Remove a file or directory"""
    try:
        if recursive:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                print(f"rm: cannot remove '{path}': Not a directory")
        else:
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                print(f"rm: cannot remove '{path}': Is a directory (use -r to delete)")
            else:
                print(f"rm: cannot remove '{path}': no such file or directory")
    except Exception as e:
        print(f"rm: error {e}")
     

def main():
    while True:
        inp = input("$ ")
        if not inp:
            continue #skip empty input, just show prompt again
        if inp == "exit":
            break
        elif inp[:3] == "cd ":
            sh_cd(inp[3:])
        elif inp == "help" or inp == "man":
            sh_help()
        elif inp == "pwd":
            sh_pwd()
        elif inp == "ls":
            args = inp.split(maxsplit=1)
            path = args[1] if len(args) > 1 else "."
            sh_ls(path)
        elif inp.startswith("mkdir "):
            args = inp.split(maxsplit=1)
            if len(args) > 1:
                sh_mkdir(args[1])
            else:
                print("mkdir: missing operand")
        elif inp.startswith("rm"):
            args = inp.split()[1:]
            recursive = "-r" in args
            paths = [arg for arg in args if not arg.startswith("-")]

            if not paths:
                print("rm: missing operand")
            else:
                for path in paths:
                    sh_rm(path, recursive)
        else:
            execute_command(inp)


if '__main__' == __name__:
    main()