import subprocess

class tcolor:
    try:
        red    = subprocess.check_output("tput setaf 1".split())
        green  = subprocess.check_output("tput setaf 2".split())
        yellow = subprocess.check_output("tput setaf 3".split())
        blue   = subprocess.check_output("tput setaf 4".split())
        purple = subprocess.check_output("tput setaf 5".split())

        bold = subprocess.check_output("tput bold".split())
        endc = subprocess.check_output("tput sgr0".split())
    except subprocess.CallProcessError as e:
        red    = ""
        green  = ""
        yellow = ""
        blue   = ""
        purple = ""

        bold = ""
        endc = ""

print tcolor.blue + "blue"
print tcolor.green + "green"
print tcolor.red + "red"
print tcolor.yellow + "yellow"
print tcolor.purple + "purple"
print tcolor.endc + "none"
print tcolor.bold + "bold"
