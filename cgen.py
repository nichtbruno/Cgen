import os
import sys

###############
# DEFINITIONS #
###############
working_dir = os.getcwd()+"/"
home_dir = "$HOME/Scripts/Cgen/"
forced = False

#############
# TEMPLATES #
#############
gitignore_temp = """# Prerequisites
*.d

# Object files
*.o
*.ko
*.obj
*.elf

# Linker output
*.ilk
*.map
*.exp

# Precompiled Headers
*.gch
*.pch

# Libraries
*.lib
*.a
*.la
*.lo

# Shared objects (inc. Windows DLLs)
*.dll
*.so
*.so.*
*.dylib

# Executables
*.exe
*.out
*.app
*.i*86
*.x86_64
*.hex

# Debug files
*.dSYM/
*.su
*.idb
*.pdb

# Kernel Module Compile Results
*.mod*
*.cmd
.tmp_versions/
modules.order
Module.symvers
Mkfile.old
dkms.conf

# Build directory
build/
"""
makefilec_temp = """CC := gcc

SRC_DIR := .
BUILD_DIR := build

SRC := $(shell find $(SRC_DIR) -name '*.c')
HEADERS := $(shell find $(SRC_DIR) -name '*.h')
OBJ := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(SRC))

TARGET := $(BUILD_DIR)/main

CFLAGS := -std=c17 -Wall -lm

all: $(TARGET)
	@echo "Build complete 😎"

-include $(OBJ:.o=.d)

$(TARGET): $(OBJ) | $(BUILD_DIR)
	$(CC) $(OBJ) $(CFLAGS) -o $(TARGET)

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -c $< -o $@

$(BUILD_DIR)/%.d: $(SRC_DIR)/%.c | $(BUILD_DIR)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -MM -MT $(@:.d=.o) $< > $@

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

clean:
	rm -rf $(BUILD_DIR)

run: $(TARGET)
	./$(TARGET)

.PHONY: all clean run
"""
makefilesdl_temp = """CC := gcc

SRC_DIR := .
BUILD_DIR := build

SRC := $(shell find $(SRC_DIR) -name '*.c')
HEADERS := $(shell find $(SRC_DIR) -name '*.h')
OBJ := $(patsubst $(SRC_DIR)/%.c,$(BUILD_DIR)/%.o,$(SRC))

TARGET := $(BUILD_DIR)/main

CFLAGS := -std=c17 -Wall
LDFLAGS := -lSDL2main -lSDL2

all: $(TARGET)
	@echo "Build complete 😎"

-include $(OBJ:.o=.d)

$(TARGET): $(OBJ) | $(BUILD_DIR)
	$(CC) $(OBJ) $(CFLAGS) $(LDFLAGS) -o $(TARGET)

$(BUILD_DIR)/%.d: $(SRC_DIR)/%.c | $(BUILD_DIR)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -MM -MT $(@:.d=.o) $< > $@

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) -c $< -o $@

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

clean:
	rm -rf $(BUILD_DIR)

run: $(TARGET)
	./$(TARGET)

.PHONY: all clean run
"""
header_temp = """#ifndef PLACE_H
#define PLACE_H



#endif
"""
main_temp = """
int main() {

    return 0;
}
"""
readme_temp = """# NAME
### DESC
"""

###########
# OPTIONS #
###########
options = {
        "-hlp --help": "Invokes help",
        "-p --project": "Generates a C project acording to user input",
        "-sdl --make-sdl": "Generates a SDL Makefile (use with C)",
        "-mc --make-c": "Generates a Makefile for pure C",
        "-m --main": "Generates a file with the main function",
        "-s --source": "Generates only a source [.c] file",
        "-h --header": "Generates only a header [.h] file",
        "-sh --src-hdr": "Generates a source [.c] and a header [.h] file",
        "-rmd --readme": "Generates a README file",
        "-ign --ignore": "Generates a .gitignore file",
        }
commands = {
        "-f --force": "Force the operation, overwriting existing files if necessary",
        }


#############
# FUNCTIONS #
#############
def failed_start():
    print("Wrong use of: cgen [OPTION] [COMMAND]")
    print("Use 'cgen --help' for more info.")
    exit(1)


def already_exists(what):
    print("\nWARNING:")
    print(f"File {what} already exists.\n")
    print("You can use the -f command to complete the task")
    print("Use 'cgen --help' for more info.")


def check(dir) -> bool:
    global forced
    return not forced and os.path.exists(dir)


def get_needed_option() -> str:
    global forced
    try:
        f = False
        for k in options.keys():
            if sys.argv[1] in k.split(" "):
                f = True
                break
        if not f:
            failed_start()
    except IndexError:
        print("a")
        failed_start()

    if sys.argv[1] in list(options.keys())[0].split(" "):
        print("Usage: cgen [OPTION] [COMMAND]")
        print()
        print("Options:")
        for k, v in options.items():
            k = k.split(" ")
            print(f"{k[0]}{" "*(7-len(k[0]))}{k[1]}{" "*(20-len(k[1]))}{v}")
        print()
        print("Commands:")
        for k, v in commands.items():
            k = k.split(" ")
            print(f"{k[0]}{" "*(7-len(k[0]))}{k[1]}{" "*(20-len(k[1]))}{v}")
        exit(0)

    try:
        if sys.argv[2] == "-f":
            forced = True
    except IndexError:
        pass

    return sys.argv[1]


def makefile(option):
    if check(working_dir+"Makefile"):
        already_exists("Makefile")
        return
    else:
        if forced:
            os.system(f"rm {working_dir}Makefile")

    os.system(f"touch {working_dir}Makefile")
    with open(f"{working_dir}Makefile", "w") as file:
        if option in ["-mc", "--make-c"]:
            file.write(makefilec_temp)
        else:
            file.write(makefilesdl_temp)


def srchdr():
    usr = str(input("Name of the file [without .type]? "))
    if check(working_dir+usr+".c"):
        already_exists(usr+".c")
        return
    elif check(working_dir+usr+".h"):
        print(f"File {usr}.h already exists")
        return
    else:
        if forced:
            os.system(f"rm {working_dir}{usr}.c {working_dir}{usr}.h")

    os.system(f"touch {working_dir}{usr}.c {working_dir}{usr}.h")
    with open(f"{working_dir}{usr}.h", "w") as file:
        file.write(header_temp.replace("PLACE", usr.upper()))


def header():
    usr = str(input("Name of the file [without .type]? "))
    if check(working_dir+usr+".h"):
        print(f"File {usr}.h already exists")
        return
    else:
        if forced:
            os.system(f"rm {working_dir}{usr}.c {working_dir}{usr}.h")

    os.system(f"touch {working_dir}{usr}.h")
    with open(f"{working_dir}{usr}.h", "w") as file:
        file.write(header_temp.replace("PLACE", usr.upper()))


def source():
    usr = str(input("Name of the file [without .type]? "))
    if check(working_dir+usr+".c"):
        print(f"File {usr}.c already exists")
        return
    else:
        if forced:
            os.system(f"rm {working_dir}{usr}.c {working_dir}{usr}.h")

    os.system(f"touch {working_dir}{usr}.c")


def main():
    if check(working_dir+"main.c"):
        already_exists("main.c")
        return

    with open(f"{working_dir}main.c", "w") as file:
        file.write(main_temp)


def readme():
    if check(working_dir+"README.md"):
        already_exists("README.md")
        return
    else:
        if forced:
            os.system(f"rm {working_dir}README.md")

    name = str(input("Name for README? "))
    desc = str(input("Short description for README? "))
    os.system(f"touch {working_dir}README.md")
    with open(f"{working_dir}README.md", "w") as file:
        file.write(readme_temp.replace("NAME", name).replace("DESC", desc))


def create_project():
    sdl = str(input("Is this an SDL project [Y/n]? "))
    rea = str(input("Do you want to include a README file [Y/n]? "))
    if rea in ["y", "Y"]:
        if check(working_dir+"README.md"):
            already_exists("README.md")
        else:
            if forced:
                os.system(f"rm {working_dir}README.md")
            name = str(input("Name of your project? "))
            desc = str(input("Short description of your project? "))
            os.system(f"touch {working_dir}README.md")
            with open(f"{working_dir}README.md", "w") as file:
                file.write(readme_temp.replace("NAME", name).replace("DESC", desc))

    if sdl in ["y", "Y"]:
        makefile("-MakeSDL")
    else:
        makefile("-MakeC")
    main()

    ignore = str(input("Do you want a gitignore [y/n]? "))
    if ignore in ["y", "Y"]:
        gitignore()


def gitignore():
    if check(working_dir+".gitignore"):
        already_exists(".gitignore")
        return
    else:
        if forced:
            os.system(f"rm {working_dir}.gitignore")

    os.system(f"touch {working_dir}.gitignore")
    with open(f"{working_dir}.gitignore", "w") as file:
        file.write(gitignore_temp)


#####
# ? #
#####
option = get_needed_option()
match option:
    case "-p" | "--project":
        create_project()
    case "-sdl" | "--make-sdl":
        makefile(option)
    case "-mc" | "--make-c":
        makefile(option)
    case "-m" | "--main":
        main()
    case "-s" | "-source":
        source()
    case "-h" | "--header":
        header()
    case "-sh" | "--src-hdr":
        srchdr()
    case "-rmd" | "--readme":
        readme()
    case "-ign" | "--ignore":
        gitignore()
    case _:
        exit(1)
