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
     - `-f`: making the deletion process immediate and without asking for user confirmation. 
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



## `find` and `locate`
## `find` Command

### Basic Usage

- **Search by name:**
  ```bash
  find /home/user/Documents -name "report.txt"
  ```
  *Example:* Search for a file named `report.txt` in the `Documents` directory.

- **Case-insensitive search:**
  ```bash
  find /var/log -iname "error.log"
  ```
  *Example:* Search for a file named `error.log` in the `/var/log` directory, ignoring case.

- **Search by file type:**
  ```bash
  find /tmp -type f
  ```
  *Example:* Find all regular files in the `/tmp` directory.

  ```bash
  find /etc -type d
  ```
  *Example:* Find all directories in the `/etc` directory.

- **Search by size:**
  ```bash
  find /home/user -size +100M
  ```
  *Example:* Find all files larger than 100MB in the `/home/user` directory.

  ```bash
  find /var/tmp -size -10k
  ```
  *Example:* Find all files smaller than 10KB in the `/var/tmp` directory.

- **Search by modification time:**
  ```bash
  find /home/user -mtime -7
  ```
  *Example:* Find files in the `/home/user` directory modified within the last 7 days.

  ```bash
  find /var/backups -mtime +30
  ```
  *Example:* Find files in the `/var/backups` directory modified more than 30 days ago.

- **Search by permissions:**
  ```bash
  find /home/user -perm 644
  ```
  *Example:* Find files with `644` permissions in the `/home/user` directory.

- **Execute a command on found files:**
  ```bash
  find /var/log -name "*.log" -exec rm {} \;
  ```
  *Example:* Find and delete all `.log` files in the `/var/log` directory.

### Advanced Usage

- **Search with multiple conditions (AND):**
  ```bash
  find /home/user -name "*.log" -size +1M
  ```
  *Example:* Find `.log` files larger than 1MB in the `/home/user` directory.

- **Search with multiple conditions (OR):**
  ```bash
  find /home/user \( -name "*.jpg" -o -name "*.png" \)
  ```
  *Example:* Find files that are either `.jpg` or `.png` in the `/home/user` directory.

- **Exclude directories:**
  ```bash
  find /home/user -path "/home/user/exclude_dir" -prune -o -name "*.txt" -print
  ```
  *Example:* Search for `.txt` files in `/home/user` but exclude the `exclude_dir` directory.

## `locate` Command

### Basic Usage

- **Simple search:**
  ```bash
  locate report.txt
  ```
  *Example:* Find all files named `report.txt` across the system.

- **Case-insensitive search:**
  ```bash
  locate -i error.log
  ```
  *Example:* Search for files named `error.log` without considering case.

### Database and Indexing

- **Update the locate database:**
  ```bash
  sudo updatedb
  ```
  *Example:* Manually update the `locate` command's database to ensure it reflects the latest file changes.

### Practical Examples

- **Find a file by partial name:**
  ```bash
  locate report
  ```
  *Example:* Locate files containing `report` in their name.

- **Find a file within a specific directory:**
  ```bash
  locate /home/user/Documents/report
  ```
  *Example:* Locate files with `report` in their name within the `Documents` directory.

- **List only a specific number of results:**
  ```bash
  locate -n 10 report.txt
  ```
  *Example:* Show only the first 10 results for `report.txt`.


 #### Additional Note on `find` and `locate`
`find` is flexible and powerful but searches in real-time across all file systems, making it slower compared to `locate`, which searches within a pre-built database.


## Linux File Permissions 

## Basic Concepts

- **File Permissions**: Each file or directory in Linux has associated permissions that determine who can read, write, or execute the file.

- **User Types**:
  - **Owner (u)**: The user who owns the file.
  - **Group (g)**: Users who are members of the file's group.
  - **Others (o)**: All other users on the system.

- **Permission Types**:
  - **Read (r)**: Permission to read the file or list the directory contents.
  - **Write (w)**: Permission to modify the file or directory.
  - **Execute (x)**: Permission to execute the file (if it’s a script or binary) or access the directory.

## Viewing Permissions

- **View file permissions**:
  ```bash
  ls -l
  ```
  *Example:* Displays a long listing of directory contents, including permissions, owner, group, and other details.

  Output:
  ```
  -rwxr-xr-- 1 user group 1024 Aug 16 08:00 myscript.sh
  ```
  *Explanation:* The first character represents the file type (`-` for regular files, `d` for directories). The next nine characters are the permissions for owner, group, and others.

## Changing Permissions

- **Using `chmod` command**:
  - **Change permissions using symbolic mode**:
    ```bash
    chmod u+rwx,g+rx,o-r myfile.txt
    ```
    *Example:* Grants read, write, and execute permissions to the owner, read and execute permissions to the group, and removes read permission for others.

  - **Change permissions using numeric mode (octal)**:
    ```bash
    chmod 755 myscript.sh
    ```
    *Example:* Sets the permissions to `rwxr-xr-x` (owner can read, write, execute; group and others can read and execute).

  - **Make a file executable**:
    ```bash
    chmod +x myscript.sh
    ```
    *Example:* Adds execute permissions to the file for everyone.

  - **Remove write permission for group and others**:
    ```bash
    chmod go-w myfile.txt
    ```
    *Example:* Removes write permission for the group and others.

## Changing Ownership

- **Using `chown` command**:
  - **Change file owner**:
    ```bash
    sudo chown newowner myfile.txt
    ```
    *Example:* Changes the owner of `myfile.txt` to `newowner`.

  - **Change file owner and group**:
    ```bash
    sudo chown newowner:newgroup myfile.txt
    ```
    *Example:* Changes the owner to `newowner` and the group to `newgroup`.

  - **Change group ownership**:
    ```bash
    sudo chgrp newgroup myfile.txt
    ```
    *Example:* Changes the group ownership of `myfile.txt` to `newgroup`.

## Special Permissions

- **Setuid (Set User ID)**:
  - **Usage**:
    ```bash
    chmod u+s /path/to/file
    ```
    *Example:* Allows a file to be executed with the permissions of the file owner.

- **Setgid (Set Group ID)**:
  - **Usage**:
    ```bash
    chmod g+s /path/to/directory
    ```
    *Example:* New files created within the directory inherit the group of the directory.

- **Sticky Bit**:
  - **Usage**:
    ```bash
    chmod +t /path/to/directory
    ```
    *Example:* Ensures that only the file owner can delete or rename the files in the directory.

## Viewing Special Permissions

- **View special permissions**:
  ```bash
  ls -l /path/to/file
  ```
  *Example:* Look for `s`, `S`, or `t` in the permission field:
  ```
  -rwsr-xr-x 1 root root 12345 Aug 16 08:00 /usr/bin/sudo
  drwxrwxrwt 2 root root 4096 Aug 16 08:00 /tmp
  ```

## Recursively Changing Permissions

- **Using `chmod` recursively**:
  ```bash
  chmod -R 755 /path/to/directory
  ```
  *Example:* Recursively change permissions for all files and directories within `/path/to/directory`.

- **Using `chown` recursively**:
  ```bash
  sudo chown -R newowner:newgroup /path/to/directory
  ```
  *Example:* Recursively change ownership for all files and directories within `/path/to/directory`.

## Shell Redirections

## Basic Concepts

- **Standard Input (stdin)**: File descriptor 0, usually refers to input from the keyboard.
- **Standard Output (stdout)**: File descriptor 1, usually refers to the output on the terminal.
- **Standard Error (stderr)**: File descriptor 2, used for error messages.


## Redirection Operators

### Redirecting Output

- **Redirect stdout to a file**:
  ```bash
    command > file.txt
  ```
  Example: Writes the output of command to file.txt, overwriting the file.

- **Append stdout to a file**:

  ```bash
  command >> file.txt
  ```
    Example: Appends the output of command to file.txt, preserving the existing content.

### Redirecting Input

- **Redirect stdin from a file**:

  ```bash
    command < file.txt
  ```
    Example: Takes input for command from file.txt.

### Redirecting stderr

- **Redirect stderr to a file**:

  ```bash
    command 2> error.log
  ```
  Example: Writes the error messages of command to error.log.

- **Append stderr to a file**:

  ```bash
  command 2>> error.log
  ```
  
  Example: Appends the error messages of command to error.log.

### Redirecting stdout and stderr

- **Redirect stdout and stderr to the same file**:

  ```bash
  command > file.txt 2>&1
  ```

  Example: Writes both output and error messages of command to file.txt.

- **Redirect stdout and stderr to separate files**:

  ```bash
  command > output.log 2> error.log
  ```

  Example: Writes output to output.log and errors to error.log.

- **Redirect both stdout and stderr to the same file (shorthand)**:

  ```bash
  command &> file.txt
  ```

  Example: In bash, redirects both stdout and stderr to file.txt.

### Combining Commands with Redirections

- **Pipe (|)**:

  ```bash
  command1 | command2
  ```

  Example: Takes the output of command1 and uses it as the input for command2.

- **Tee Command**:

  ```bash
  command | tee file.txt
  ```

  Example: Writes the output of command to both file.txt and the terminal.

### Advanced Redirections

- **Redirect stdout to /dev/null**:

  ```bash
  command > /dev/null
  ```

  Example: Discards the output of command.

- **Redirect stderr to /dev/null**:

  ```bash
  command 2> /dev/null
  ```

  Example: Discards the error messages of command.

- **Suppress both stdout and stderr**:

  ```bash
  command &> /dev/null
  ```

  Example: Discards both output and error messages of command.

### Heredoc and Here Strings

- **Heredoc (<<)**:

  ```bash
  command << EOF
  This is a multiline string.
  It is used as input for the command.
  EOF
  ```

  Example: Sends the multiline string as input to command.

- **Here String (<<<)**:

  ```bash
  command <<< "This is a string."
  ```

  Example: Sends a single string as input to command.


## Linux User and Group Management 

## User Management

### Creating a User
- **Create a new user**:
  ```bash
  sudo useradd username
  ```
  Example: Creates a user with the name `username`.

- **Create a user with a home directory**:
  ```bash
  sudo useradd -m username
  ```
  Example: Creates a user and generates a home directory (`/home/username`).

- **Assign a password to a user**:
  ```bash
  sudo passwd username
  ```
  Example: Sets a password for the user `username`.

### Modifying a User
- **Modify an existing user**:
  ```bash
  sudo usermod -l new_name old_name
  ```
  Example: Changes the username from `old_name` to `new_name`.

- **Add a user to a group**:
  ```bash
  sudo usermod -aG group_name username
  ```
  Example: Adds `username` to the group `group_name`.

### Deleting a User
- **Delete a user**:
  ```bash
  sudo userdel username
  ```
  Example: Deletes the user `username`.

- **Delete a user and their home directory**:
  ```bash
  sudo userdel -r username
  ```
  Example: Deletes the user and their home directory (`/home/username`).

## Group Management

### Creating and Managing Groups
- **Create a group**:
  ```bash
  sudo groupadd group_name
  ```
  Example: Creates a group named `group_name`.

- **Add a user to a group**:
  ```bash
  sudo usermod -aG group_name username
  ```
  Example: Adds `username` to the group `group_name`.

- **Change a user's primary group**:
  ```bash
  sudo usermod -g group_name username
  ```
  Example: Sets `group_name` as the primary group for `username`.

### Deleting a Group
- **Delete a group**:
  ```bash
  sudo groupdel group_name
  ```
  Example: Deletes the group `group_name`.

## Permissions and Ownership Management

### Change Ownership of a File or Directory
- **Change the owner of a file or directory**:
  ```bash
  sudo chown username file_or_directory
  ```
  Example: Changes the owner of `file_or_directory` to `username`.

- **Change the owner and group**:
  ```bash
  sudo chown username:group_name file_or_directory
  ```
  Example: Changes the owner to `username` and the group to `group_name`.

### Change Permissions
- **Change the permissions of a file or directory**:
  ```bash
  sudo chmod 755 file_or_directory
  ```
  Example: Sets specific permissions (`rwxr-xr-x`) on `file_or_directory`.

- **Recursively change permissions on a directory**:
  ```bash
  sudo chmod -R 755 directory
  ```
  Example: Applies `755` permissions to all files and subdirectories within `directory`.

## User and Group Information

### View User Information
- **Display information about a user**:
  ```bash
  id username
  ```
  Example: Shows the user ID and group details for `username`.

- **See currently logged-in users**:
  ```bash
  who
  ```
  Example: Displays users currently logged into the system.

- **Display the last logged-in users**:
  ```bash
  last
  ```
  Example: Lists the last users who logged in.

### View Available Groups
- **List all groups**:
  ```bash
  getent group
  ```
  Example: Displays all groups available on the system.

### Modify User and Group Configuration Files
- **User file (/etc/passwd)**:
  ```bash
  sudo nano /etc/passwd
  ```
  Example: Contains user information.

- **Group file (/etc/group)**:
  ```bash
  sudo nano /etc/group
  ```
  Example: Contains group information.

## Security and Advanced Management

### Lock and Unlock a User Account
- **Lock a user account**:
  ```bash
  sudo usermod -L username
  ```
  Example: Locks the account `username`.

- **Unlock a user account**:
  ```bash
  sudo usermod -U username
  ```
  Example: Unlocks the account `username`.

### Password Expiration
- **Set password expiration**:
  ```bash
  sudo chage -E YYYY-MM-DD username
  ```
  Example: Sets the password expiration date for `username`.

- **Check password expiration settings**:
  ```bash
  sudo chage -l username
  ```
  Example: Displays expiration settings for `username`.

## Package Management System
## 1. apt-get 
- **`apt-get update`**: Updates the list of available packages.
- **`apt-get upgrade`**: Installs the latest versions of installed packages.
- **`apt-get install <package>`**: Installs a specific package.
- **`apt-get remove <package>`**: Removes a package without deleting its configuration files.
- **`apt-get purge <package>`**: Removes a package along with its configuration files.
- **`apt-get autoremove`**: Removes unused dependencies.
- **`apt-get clean`**: Deletes downloaded package archive files.

### a. Dependency Management

- `apt-cache depends <package>`: Lists dependencies of a package.
- `apt-mark hold <package>`: Prevents a package from being upgraded.
- `apt-mark unhold <package>`: Allows a package to be upgraded again.

### b. Package Search

- `apt-cache search <keyword>`: Searches for packages by keyword.
- `apt-cache show <package>`: Displays detailed information about a package.

### c. Package Source Management

- `/etc/apt/sources.list`: Main file where package repositories are defined.
- `add-apt-repository <repository>`: Adds a new package repository.

### d. Local Package Management

- `dpkg -i <package>.deb`: Installs a local .deb package.
- `dpkg -r <package>`: Removes a locally installed package.
- `dpkg -P <package>`: Purges a locally installed package, including configuration files.

### e. Diagnostics and Repair

- `apt-get -f install`: Fixes missing or broken dependencies.
- `dpkg --configure -a`: Configures unconfigured packages.
- `dpkg --audit`: Checks for packages that are not completely installed.

### f. Pinning (Package Prioritization)

- `/etc/apt/preferences`: Configuration file for pinning, allowing specification of preferred package versions.
  - Example:
    ```yaml
    Package: *
    Pin: release a=stable
    Pin-Priority: 1001
    ```

### g. Managing GPG Keys

- `apt-key list`: Lists GPG keys.
- `apt-key add <keyfile>`: Adds a new GPG key.
- `apt-key del <key>`: Removes a GPG key.

### h. Broken Packages and Rollbacks

- `apt-get install <package>=<version>`: Installs a specific version of a package.
- `apt-cache policy <package>`: Displays available versions of a package.
## 2. apt 

- **`sudo apt update`**: Update Package List
- **`sudo apt upgrade`**: Upgrade Packages
- **`sudo apt install <package>`**: Install Package
- **`sudo apt remove <package>`**: Remove Package
- **`sudo apt purge <package>`**: Purge Package
- **`sudo apt autoremove`**: Autoremove
- **`sudo apt clean`**: Clean Cache

## 3. Using Aptitude

- `aptitude update`: Updates the list of available packages.
- `aptitude upgrade`: Upgrades installed packages.
- `aptitude install <package>`: Installs a package.
- `aptitude remove <package>`: Removes a package.

## Package Management Tool Usage Summary

### `apt-get`
- **Use Case**: Ideal for scripts and automation due to its stability. Best for detailed package management tasks such as installing specific versions and handling broken packages.

### `apt`
- **Use Case**: Suitable for everyday package management with a more user-friendly interface. Good for common tasks like installing, upgrading, and removing packages with improved readability.

### `aptitude`
- **Use Case**: Useful for advanced dependency management and conflicts. Provides a text-based user interface for interactive package management, making it ideal for complex scenarios.
