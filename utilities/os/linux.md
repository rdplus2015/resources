# Linux System 

## Root Directories in Linux

- **`/`** The root directory. All other directories and files are contained within this directory
.
- **`/bin`** Contains essential user command binaries (executables), such as `ls`, `cp`, `mv`, etc. 
These are simply our programs, our scripts which will be translated into binary since the
machines can only speak in binary

- **`/etc`** Contains configuration files for the system and applications. For example, `/etc/passwd` stores user account information. Allow the system to function correctly.

- **`/home`** Contains the home directories for all user accounts. Each user typically has a subdirectory under `/home`, where personal files and configurations are stored.

- **`/usr`** This directory contains the majority of files and programs used by users, as well as applications installed via the system package manager

- **`/tmp`** A directory for temporary files that are created and deleted by programs during execution. This directory is typically cleared on boot.

- **`/opt`** Contains optional software packages that are not part of the default installation. This is typically used for third-party software. For example, if you want to install the Google Chrome browser, it will be installed by default, in the directory `/opt`.

- **`/var`** Contains variable data files, such as logs, mail spools, and databases. The content of this directory is expected to grow in size as the system is used.


## Basic Commands

- **`sudo`** - Executes a command with superuser (root) privileges.
  - **Example**:
    ```bash
    sudo apt-get update
    ```

- **`sudo su`** - Switches the current user to the superuser (root).
  - **Example**:
    ```bash
    sudo su
    ```

- **`nautilus`** - Opens the GNOME file manager, allowing you to browse files and directories through a graphical interface.
  - **Usage**:
    - `nautilus`: Opens the file manager in the current directory.
    - `nautilus /path/to/directory`: Opens the file manager in a specific directory.
  - **Example**:
    ```bash
    nautilus /home/user/Documents
    ```

- **`ls`** - Lists files and directories in a directory.
  - **Useful options**:
    - `-l`: Displays files in a long format.
    - `-a`: Shows all files, including hidden ones.
    - `ls -lh`: shows the folder items, but shows us the size of the items in a more "readable"
    - `ls -R`: displays the items in each directory recursively starting from where we are

  - **Example**:
    ```bash
    ls -la
    ```

- **`cd`** - Changes the current directory.
  - **Usage**:
    - `cd /path/to/directory`: To navigate to a specific directory.
    - `cd ..`: To move up one directory level.
  - **Example**:
    ```bash
    cd /home/user/documents
    ```

- **`pwd`** - Prints the full path of the current directory.
  - **Example**:
    ```bash
    pwd
    ```

- **`cp`** - Copies files or directories.
  - **Useful options**:
    - `-r`: Recursively copies all subdirectories and files.
  - **Example**:
    ```bash
    cp -r source_directory/ destination_directory/
    ```

- **`cpy`** - [The description of this command depends on the specific utility or alias used for copying.]
  - **Example**:
    ```bash
    cpy file1.txt /path/to/destination/
    ```

- **`mv`** - Moves or renames files or directories.
  - **Usage**:
    - `mv file1 file2`: Renames `file1` to `file2`.
    - `mv file /new/path/`: Moves the file to a different directory.
  - **Example**:
    ```bash
    mv oldname.txt newname.txt
    ```

- **`rm`** - Removes files or directories.
  - **Useful options**:
    - `-r`: Recursively removes a directory and its contents.
  - **Example**:
    ```bash
    rm -r unwanted_directory/
    ```

- **`mkdir`** - Creates a new directory.
  - **Useful options**:
    - `-p`: Creates parent directories as needed.
  - **Example**:
    ```bash
    mkdir -p new_directory/sub_directory/
    ```

- **`touch`** - Creates a new empty file or updates the timestamp of an existing file.
  - **Example**:
    ```bash
    touch newfile.txt
    ```

- **`echo`** - Displays a line of text.
  - **Usage**:
    - `echo "Text"`: Displays "Text" in the terminal.
    - `echo "Text" > file.txt`: Writes "Text" to a file.
  - **Example**:
    ```bash
    echo "Hello, World!" > greeting.txt
    ```

- **`cat`** - Concatenates and displays the content of files.
  - **Example**:
    ```bash
    cat file.txt
    ```

## Alias for bash

1. **Open your `.bashrc` file** (for regular users) or `.bash_profile` (for login shells) in a text editor:

    ```bash
    nano ~/.bashrc
    ```

2. **Add your alias** at the end of the file. For example:

    ```bash
    alias ll='ls -la'
    ```

3. **Save and close** the file.

4. **Apply the changes** by running:

    ```bash
    source ~/.bashrc
    ```

- **Use the alias as needed within this session. The alias will disappear once you close the terminal session.**
    ```bash
    alias ll='ls -la'
    ```

## Nano 

### Basic Commands

- **Open a file:** `nano filename`
- **Save changes:** `Ctrl + O`, then press `Enter`
- **Exit Nano:** `Ctrl + X`
- **Cut text:** `Ctrl + K`
- **Paste text:** `Ctrl + U`
- **Search for text:** `Ctrl + W`, then type search term and press `Enter`
- **Replace text:** `Ctrl + \`, then type search term, press `Enter`, then type replacement text, and press `Enter`
- **Go to a specific line:** `Ctrl + _`, then enter the line number and press `Enter`
- **Undo last action:** `Alt + U`
- **Redo last undone action:** `Alt + E`

### Navigation

- **Move cursor up:** `Ctrl + P`
- **Move cursor down:** `Ctrl + N`
- **Move cursor left:** `Ctrl + B`
- **Move cursor right:** `Ctrl + F`
- **Move to beginning of line:** `Ctrl + A`
- **Move to end of line:** `Ctrl + E`
- **Move to the top of the file:** `Ctrl + Y`
- **Move to the bottom of the file:** `Ctrl + V`

## Vim Cheatsheet

### Navigation

- **Move cursor left:** `h`
- **Move cursor down:** `j`
- **Move cursor up:** `k`
- **Move cursor right:** `l`

- **Move forward by one word:** `w`
- **Move backward by one word:** `b`

- **Move to the beginning of the line:** `^`
- **Move to the end of the line:** `$`

### Insertion and Deletion

- **Insert text before the cursor:** `i`
- **Insert text at the beginning of the line:** `I`
- **Insert text after the cursor:** `a`
- **Insert text at the end of the line:** `A`

- **Delete the character under the cursor:** `x`
- **Delete the word under the cursor:** `dw`
- **Delete (cut) the entire line:** `dd`
- **Delete from the cursor to the end of the line:** `D`

- **Copy the current line:** `yy`
- **Paste the contents of the clipboard:** `p`
- **Undo the last action:** `u`

### Main Commands

- **Save the file:** `:w`
- **Quit Vim:** `:q`
- **Save and quit:** `:wq` or `:x`
- **Show line numbers:** `:set nu`
- **Hide line numbers:** `:set nonu`


