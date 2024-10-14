# Cgen 😎
## A generator script for C projects. For faster use 🚀

This script can generate a couple of things when called.
```
Use: cgen [OPTION] [COMMAND]

[OPTION]: '-help','-MakeSDL','-MakeC','-cc','-h','-c','-m','-r','-ig','-pp',
'-help':      Invokes help
'-MakeSDL':   Generates a SDL Makefile (use with C)
'-MakeC':     Generates a Makefile for pure C
'-cc':        Generates a source [.c] and a header [.h] file
'-h':         Generates only a header [.h] file
'-c':         Generates only a source [.c] file
'-m':         Generates a file with the main function
'-r':         Generates a README file
'-ig':        Generates a .gitignore file
'-pp':        Generates a C project acording to user input

[COMMAND]: '-f',
'-f':         Forces an option into execution and rewrites the files
```
**The templates for Makefiles and .gitignore and other are in the cgen.py file as multiline string.
You can change these at will.**

-----
# Install 🧩
```
git clone git@github.com:nichtbruno/Cgen.git
```

Make sure to set an alias in your .bashrc or .zshrc file
```
alias cgen="python ~/Cgen/cgen.py"
```

-----
# Note 🗒️
I am currently not planning to change this to more convenient way
of installing and use. Maybe in the future but for now it works.
