# Custom Shell Emulator
#### Video Demo: https://drive.google.com/file/d/1FoTgXFhXyB5WNlUkGITa-3XnwmvjCSro/view?usp=sharing


## Description
This program is a simple shell emulator written in Python. It provides basic shell functionalities, including built-in commands and the ability to execute external commands. The shell also supports output redirection and tab completion for convenience.

## Features
- Built-in commands: `exit`, `echo`, `type`, `pwd`, `cd`
- Execution of external commands found in system `PATH`
- Tab completion for built-in and executable commands
- Command history navigation
- Output redirection (`>`, `>>`, `1>`, `2>`)

## Prerequisites
- Python 3.x
- A Unix-like environment (Linux or macOS recommended, partial Windows support)

## Installation
1. Clone or download the repository.
2. Ensure you have Python installed (`python3 --version`).
3. Run the script:
   ```sh
   python3 main.py
   ```

## Usage
Once the shell is running, you can enter commands just like in a standard terminal. Example commands:
- `pwd` → Prints the current working directory.
- `echo Hello` → Prints "Hello" to the console.
- `cd /home/user` → Changes the directory.
- `ls` → Lists files (if available in system PATH).
- `exit 0` → Exits the shell with status code 0.

### Output Redirection Examples
- `echo Hello > output.txt` → Writes "Hello" to `output.txt`.
- `ls 1> stdout.log 2> stderr.log` → Redirects standard output and error to separate files.

## Key Bindings
- `Tab` → Auto-completes commands
- `Ctrl + A` → Moves cursor to the beginning of the line
- `Ctrl + E` → Moves cursor to the end of the line
- `Ctrl + R` → Reverse search history
- `Alt + B` → Moves cursor backward by a word
- `Alt + F` → Moves cursor forward by a word
- `Ctrl + U` → Clears the current command line

## Known Issues
- Windows doesn't support the auto completion feature yet comment the lines using the readline library in the main function.

