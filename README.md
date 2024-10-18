# Cgen V2 😎
## A generator script for C projects. For faster project setup 🚀

#### New in version 2
 - Templates are now in seperate files
 - Can create files in a seperate location
    - Have to be very careful, it just continues from the working directory
    so something line
    ```cgen -c -f ~/directory``` wouldn't work
 - improved code
    - -> doesn't delete and create files but just rewrites them
 - Code is still 💩

This script can generate a couple of things when called.
```
Usage: cgen [OPTION] [COMMAND] [LOCATION]

Options:
-hlp   --help              Invokes help
-p     --project           Generates a C project acording to user input
-sdl   --make-sdl          Generates a SDL Makefile (use with C)
-mc    --make-c            Generates a Makefile for pure C
-m     --main              Generates a file with the main function
-s     --source            Generates only a source [.c] file
-h     --header            Generates only a header [.h] file
-sh    --src-hdr           Generates a source [.c] and a header [.h] file
-dd    --default-defs      Generates a default define header file with few integer definitions
-rmd   --readme            Generates a README file
-ign   --ignore            Generates a .gitignore file

Commands:
-f     --force             Forces an option into execution and rewrites the files

Location:
Location of the new files
examples: cgen -h -f headers (this creates a header file inside a headers directory)
```
**The templates are now in seperate files!!**

-----
# Install 🧩
```
git clone https://github.com/nichtbruno/Cgen.git ~/
```

Make sure to set an alias in your .bashrc or .zshrc file
```
alias cgen="python ~/Cgen/cgen.py"
```

-----
# Note 🗒️
I am currently not planning to change this to more convenient way
of installing and use. Maybe in the future but for now it works.

The code is horrible :|
