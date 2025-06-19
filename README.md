# 🐍 PySh — A Python Shell

![Static Badge](https://img.shields.io/badge/Language-Python-blue) 
![Static Badge](https://img.shields.io/badge/License-MIT-green)

**PySh** (Python Shell) is a simple command-line shell implemented in Python. It replicates the feel of Unix-like shells such as Bash or Zsh, while supporting all basic shell commands. 



This was built using notepad++.

---

## Features

-  **Basic Shell Operations**: Navigate directories, list files, and manage the filesystem.
- **Pipe Support**: Chain commands together using the pipe operator (`|`)
- **Built-in Commands**: Essential commands implemented natively in Python
- **External Command Support**: Execute commands and programs
-  **Cross Platform**: Works on *Windows*, *macOS*, and *Linux*

---

## Getting Started

### Requirements

- Python 3.6 or later

###  Installation

Clone the repository:

```bash
git clone https://github.com/lukras-exe/pysh.git
cd pysh
```

Ensure Python 3.x is installed:
```bash
python --version
```

Run the Shell:
```bash
python pysh.py
```
On Unix-based systems, you can also make it executable:
```bash
chmod +x pysh.py
./pysh.py
```
## Built-in Commands

| Command | Description | Usage |
|---------|-------------|--------|
| `help` / `man` | Display help information | `help` |
| `exit` | Exit the shell | `exit` |
| `cd [dir]` | Change directory (defaults to current if no path) | `cd /path/to/directory` |
| `pwd` | Print current working directory | `pwd` |
| `ls [dir]` | List files and directories | `ls` or `ls /path/to/directory` |
| `mkdir [dir]` | Create a new directory | `mkdir new_folder` |
| `rm [file/dir]` | Remove files or directories | `rm file.txt` or `rm -r folder/` |

## Usage Examples
### Basic Navigation
```bash
$ pwd
/home/user
$ ls
Documents  Downloads  Pictures  Videos
$ cd Documents
$ pwd
/home/user/Documents
```
### File Operations
```bash
$ mkdir test_folder
$ ls 
test_folder
$ rm -r test_folder
```
### Piping Commands
```bash
$ ls | grep txt
documents.txt
notes.txt
```

### External Commands
```bash
$ ping google.com
$ ssh user@server.com
$ git status
```

## How It Works
PySh is built using Python's standard library modules:
- `os`: For directory operations and file system interaction
- `subprocess`: For executing external commands
- `shutil`: For advanced file operations like recursive deletion

**The shell implements a simple REPL (Read-Eval-Print Loop) that**:
1. Reads user input
2. Parses built-in vs external commands
3. Handles pipe operations by manipulating file descriptors
4. Executes commands and displays output

## Current Limitations
- No support for command flags (except `-r` for `rm`)(coming soon!)
- Limited pipe functionality (basic implementation)
- No tab completion (coming soon!)

## License
This project is open source and available under the MIT License
