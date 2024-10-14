# Cgen 😎
## A generator script for C projects. For faster setup 🚀

This script can generate a couple of things when called.
```
Usage: cgen [OPTION] [COMMAND]

Options:
-hlp   --help              Invokes help
-p     --project           Generates a C project acording to user input
-sdl   --make-sdl          Generates a SDL Makefile (use with C)
-mc    --make-c            Generates a Makefile for pure C
-m     --main              Generates a file with the main function
-s     --source            Generates only a source [.c] file
-h     --header            Generates only a header [.h] file
-sh    --src-hdr           Generates a source [.c] and a header [.h] file
-rmd   --readme            Generates a README file
-ign   --ignore            Generates a .gitignore file

Commands:
-f     --force             Forces an option into execution and rewrites the files
```
**The templates for Makefiles and .gitignore and other are in the cgen.py file as multiline strings.
You can change these at will.**

-----
# Install 🧩
```
git clone https://github.com/nichtbruno/Cgen.git
```

Make sure to set an alias in your .bashrc or .zshrc file
```
alias cgen="python ~/Cgen/cgen.py"
```

-----
# Note 🗒️
I am currently not planning to change this to more convenient way
of installing and use. Maybe in the future but for now it works.
