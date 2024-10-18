import os
import sys

###############
# DEFINITIONS #
###############
working_dir = os.getcwd()+"/"
home_dir = os.getenv("HOME")+"/Cgen/"
forced = False

#############
# TEMPLATES #
#############

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
        "-dd --default-defs": "Generates a default define header file with few integer definitions",
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
    print("Wrong use of: cgen [OPTION] [COMMAND] [LOCATION]")
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


def read_temps(dir) -> str:
    f = ""
    with open(f"{home_dir}{dir}", "r") as file:
        f = file.read()
    return f


def update_working_dir(dir):
    global working_dir
    if os.path.exists(f"{working_dir}{dir}"):
        working_dir = working_dir+dir+"/"
    else:
        print(f"Location {dir} doesn't exsit in this working directory\n")
        failed_start()


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
        print("Usage: cgen [OPTION] [COMMAND] [LOCATION]")
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
        print()
        print("Location:\nLocation of the new files")
        print("examples: cgen -h -f headers (this creates a header file inside a headers directory)")
        exit(0)

    try:
        if sys.argv[2] == "-f":
            forced = True
            if sys.argv[3]:
                if not os.path.exists(working_dir+sys.argv[3]):
                    os.system(f"mkdir {working_dir}{sys.argv[3]}")
                update_working_dir(sys.argv[3])
        else:
            update_working_dir(sys.argv[2])
    except IndexError:
        pass

    return sys.argv[1]


def makefile(option):
    if check(working_dir+"Makefile"):
        already_exists("Makefile")
        return

    def write(text):
        with open(f"{working_dir}Makefile", "w") as file:
            file.write(text)

    if option in ["-mc", "--make-c"]:
        write(read_temps("makefilec_temp"))
    else:
        write(read_temps("makefilesdl_temp"))


def srchdr():
    usr = str(input("Name of the file [without .type]? "))
    if check(working_dir+usr+".c"):
        already_exists(usr+".c")
        return
    elif check(working_dir+usr+".h"):
        print(f"File {usr}.h already exists")
        return

    header_temp = read_temps("header_temp")
    with open(f"{working_dir}{usr}.h", "w") as file:
        file.write(header_temp.replace("PLACE", usr.upper()))


def header():
    usr = str(input("Name of the file [without .type]? "))
    if check(working_dir+usr+".h"):
        print(f"File {usr}.h already exists")
        return

    header_temp = read_temps("header_temp")
    with open(f"{working_dir}{usr}.h", "w") as file:
        file.write(header_temp.replace("PLACE", usr.upper()))


def source():
    usr = str(input("Name of the file [without .type]? "))
    if check(working_dir+usr+".c"):
        print(f"File {usr}.c already exists")
        return
    else:
        if forced and not os.path.exists(working_dir+usr+".c"):
            os.system(f"rm {working_dir}{usr}.c")

    os.system(f"touch {working_dir}{usr}.c")


def main(src=""):
    if check(working_dir+src+"main.c"):
        already_exists("main.c")
        return

    main_temp = read_temps("main_temp")
    with open(f"{working_dir}{src}main.c", "w") as file:
        file.write(main_temp)


def readme():
    if check(working_dir+"README.md"):
        already_exists("README.md")
        return

    readme_temp = read_temps("readme_temp")
    name = str(input("Name for README? "))
    desc = str(input("Short description for README? "))
    with open(f"{working_dir}README.md", "w") as file:
        file.write(readme_temp.replace("NAME", name).replace("DESC", desc))


def create_project():
    sdl = str(input("Is this an SDL project [Y/n]? "))
    rea = str(input("Do you want to include a README file [Y/n]? "))
    if rea in ["y", "Y"]:
        if check(working_dir+"README.md"):
            already_exists("README.md")
        else:
            name = str(input("Name of your project? "))
            desc = str(input("Short description of your project? "))

            readme_temp = read_temps("readme_temp")
            with open(f"{working_dir}README.md", "w") as file:
                file.write(readme_temp.replace("NAME", name).replace("DESC", desc))

    if sdl in ["y", "Y"]:
        makefile("-sdl")
    else:
        makefile("-mc")

    if check(working_dir+"src"):
        already_exists("src directory")
    else:
        os.system(f"mkdir {working_dir}src")
        if forced:
            os.system(f"rm -r {working_dir}src")
    main("src/")

    ignore = str(input("Do you want a gitignore [y/n]? "))
    if ignore in ["y", "Y"]:
        gitignore()

    default = str(input("Do you want a default define header [y/n]? "))
    if default in ["y", "Y"]:
        define_d("src/")


def gitignore():
    if check(working_dir+".gitignore"):
        already_exists(".gitignore")
        return

    gitignore_temp = read_temps("gitignore_temp")
    with open(f"{working_dir}.gitignore", "w") as file:
        file.write(gitignore_temp)


def define_d(edir=""):
    if check(working_dir+edir+"defs.h"):
        print("File defs.h already exists")
        return

    defs_temp = read_temps("defs_temp")
    with open(f"{working_dir}{edir}defs.h", "w") as file:
        file.write(defs_temp)


#############
# main loop #
#############
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
    case "-dd" | "--default-defs":
        define_d()
    case "-rmd" | "--readme":
        readme()
    case "-ign" | "--ignore":
        gitignore()
    case _:
        exit(1)
