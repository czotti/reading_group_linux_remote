# Reading group on useful linux command line utility

This reading group focuses on some useful tools when you're remotely working on your main computer.

NB, to keep shh connection alive: 
> `ssh -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" username@server_address`

## Install & prepare


### Installation
Mainly you need these tools on the remote computer/server.

```bash
sudo apt-get install screen byobu renameutils ack-grep sshfs openssh
```

and on your client computer (Linux):

```bash
sudo apt-get install sshfs openssh
```

or (Windows) install [bitvise](https://www.bitvise.com/ssh-client-download).

### Generate sshkey

An ssh key is used to automatically authenticate you when you ssh into another computer instead of enter your password each time.
The ssh key work with all the tools that are built on top of ssh like `scp`, `git`, `rsync`, `ssh` and much more.

This is how you generate the key:
```bash
ssh-keygen
```

This will generate a new `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub` files that can be used to authenticate.

After the generation this key can be used in some ways, the first is to automatically authenticate you into a remote computer.
To do so you just need to enter this in a terminal:
```bash
ssh-copy-id username@remote_computer_ip_addres
```

#### ssh

Now that your keys is added into the remote computer you can ssh into it.

```bash
ssh username@remote_computer_ip_address
```

#### github & bitbucket
You can also add this key into your github or bitbucket account.

For [bitbucket](https://bitbucket.org) you need to:

- login into your bitbucket account
- click on your image face (top right corner of the bitbucket page)
- click on `Bitbucket Settings`
- click on `SSH keys` on the left side
- click on `add keys`
- You need to enter a unique label name and paste the ssh key you just generate

For [github](https://github.com) you need to:

- login into your github account
- click on your image face (top right corner of the github page)
- click on `Settings`
- click on `SSH and GPG keys` on the left side
- click on `New ssh key`
- You need to enter a unique label name and paste the ssh key you just generate

After that you are setup to use git without using the login password authentication each time.
When you want to clone a repository from these websites now the ssh clone will be the default.

So instead of having this:

- `git clone https://github.com/czotti/scripts.git`

You will have this:

- `git clone git@github.com:czotti/scripts.git`

If you already have cloned a repository with the https cloning you can always change to the ssh version with the following:

```bash
cd you/repository/path
git remote -v # this will display a list a the remote url for this repository
```

The output of this command look like that:

```bash
origin	https://bitbucket.org/czotti/reading_group_linux_remote.git (fetch)
origin	https://bitbucket.org/czotti/reading_group_linux_remote.git (push)
```

Now you can override this by doing:

```bash
git remote set-url origin git@bitbucket.org:czotti/reading_group_linux_remote.git 
```

## Tools

### 1. screen & byobu

These tools are used to do remote work on a computer and/or sharing session between different computer.

Just follow this tutorial [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-screen-on-an-ubuntu-cloud-server).

### 2. rename
A useful tool to rename massively a lot of files or directies using regex.

```bash
rename -n 's/aabb/bbcc/' *.txt
```

The `-n` option is here to display what change will be done, if you remove it he will apply these changes.

### 3. grep & ack(-grep)
These tools are used find content inside files, a lot of them are available to do this task like `awk`, it has also a nice printing system.

#### grep
Starting with `grep`, it comes installed with all major Unix distribution.

He can be used as parsing the output of a command line as well as parsing content of file.

Command line parsing:
```bash
cat file.txt | grep Tutorial
```

File parsing:
```bash
grep Tutorial file.txt
```

With these two commands you can almost find everything you want inside a file.
It supports regular expression as explained in the tutorial link below.

#### ack

Another tool know as `ack` or `ack-grep` (in ubuntu) is pretty neat to find content inside file.

`ack` is like grep but with more cool features. Let's see what it can do.

```bash
ack-grep Tutorial
```

This command will find recursively inside the current directory, without following symlink, all the file where the `Tutorial` sentence is 
present and print it a a nice way with a line number and the name of the file.

- `grep` [tutorial](http://www.panix.com/~elflord/unix/grep.html)
- `ack-grep` [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-ack-a-grep-replacement-for-developers-on-ubuntu-14-04)

### 4. sed
Tool to replace content inside files.

```bash
sed -i.bak 's/Tutorial/TUTORIAL/g' filename
```

This command saves the `filename` into `filename.bak` and change the matching content `Tutorial` to `TUTORIAL` directly inside `filename`.

- `sed` [tutorial](http://www.tutorialspoint.com/sed/sed_basic_syntax.htm)

### 5. find

It's a command line utility to find file and directory inside a given path.

- find all mp3 occurrence inside the directory structure.
> ```bash
> find random_structure -name "*mp3*"
> ```

- find only mp3 file inside the directory structure.
> ```bash
> find random_structure -type f -name "*mp3*"
> ```

- find file larger than x kB.
> ```bash
> find random_structure -type f -size +100k
> ```

- find file between x and y MB.
> ```bash
> find random_structure -type f -size +10k -size -30k
> ```

- find file with .mp3 and .txt extension.
> ```bash
> find random_structure -type f \( -name "*mp3*" -o -name "*.txt" \)
> ```

- find only directory.
> ```bash
> find random_structure -type d
> ```


- find only directory with Morales name.
> ```bash
> find random_structure -type d -name "*Morales*"
> ```

- find with insensitive to case.
> ```bash
> find random_structure -iname "*morales*"
> ```

- find files and execute a command.
> ```bash
> find random_structure -name "*.mp3" -exec rename -n 's/Lori/GOD_BLESS_THE_QUEEN/' {} \;
> ```

- find empty files and directory.
> ```bash
> find rename_structure -empty
> ```


What is pretty neat about this tools is that it can be combine with all the previous one(except `ack`) with it's `-exec` parameter.

- `find` [Tutorial](http://www.tecmint.com/35-practical-examples-of-linux-find-command/)

## Apendix

- [Link](http://datascienceatthecommandline.com/) to a lot of command line tools.
