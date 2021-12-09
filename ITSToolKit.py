# | pIPe symbol 
import os
import time            
import platform
import calendar
import socket
import platform,socket,re,psutil

def hashing():
    import hashlib

    print("hashing types:")
    print("md5\nsha1\n")


    which_hash_type = input("Which hash type do you want to hash your string in?: ")

    hashinput = input("plain text: ")

    def md5_hash(data):
        hash_object = hashlib.md5()
        hash_object.update(str(data).encode())
        print("hash ", hash_object.hexdigest())


    def sha1_hash(data):
        hash_object = hashlib.sha1()
        hash_object.update(str(data).encode())
        print("hash ", hash_object.hexdigest())


    def choose():
        if hashinput == None:
            print("Enter hash type md5, or sha1")
        elif which_hash_type.lower() == "md5":
            md5_hash(data=hashinput)
        elif which_hash_type.lower() == "sha1":
            sha1_hash(data=hashinput)
        else:
            pass
            
    if __name__ ==  '__main__':
        choose()

def FibNums():
    global numbs2Print
    numbs2Print = input("Fibonacci numbers to print: ")
    print(f"Printing the first {numbs2Print} fibonacci numbers")
    def printFibonacciNumbers(n: int) -> None:
        f1 = 0
        f2 = 1
        if (n < 1):
            return
        print(f1)
        for x in range(1, n):
            print(f2)
            next = f1 + f2
            f1 = f2
            f2 = next

    printFibonacciNumbers(int(numbs2Print))


def Computer_information_specific():
    global ToolVersion
    ToolVersion = "1.55"
    print(f"""
ITSToolKit version: {ToolVersion}
Computer name: {platform.node()}
Operating system: {platform.platform()}
Operating system version: {platform.version()}
Release: {platform.release()}
Architecture: {platform.machine()} 
Python compiler: {platform.python_compiler()}
Processor: {platform.processor()}
Ram: {str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"}

{"-"*len(platform.processor())}
Networking information - private.

Ip address: {socket.gethostbyname(socket.gethostname())}
Mac address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}


    """)


def ITSToolKit(command: str) -> None:
    match command.split():
        case ["help"]:
            print("""
help, -h - show this menu.
whois, -ws - gain information about a domain or ip.
dig, -dg - query dns or ip.
exit, quit, stop - exit/quit/stop the Tool.
cat, -sc - show the contense of a file.
hash, -hs - hash encode a plain text string.
calculator, cal - simple calculator.
cd - change directory to another path.
ls, l, ll - show the contense of current folder.
python, python3 - run python shell in the toolkit (2 and 3) - you are able to run python files from terminal.
date - show the current time and calender.
time - only get the current time without the calender preview.
neofetch - shows system specifications, uptime, Kernel, GPU, CPU, Resolution etc.
base64 - encrypt or decrypt any contense within a file with the base64 (path) command. 
fib, fibonacci - This will print the amount given numbers of the fobinacci numbers.
whatis - This should be a native command in macOS
                  """)
        case ["clear" | "cls" | "clean"]:
            print("exec: " + str(command))
            time.sleep(0.1)
            os.system("clear")
        
        case ["-ws"]:
            IP_input = input("IP, or domain: ")
            
            if IP_input == None:

                os.system(f"whois {IP_input}")
        
        case ["-dg"]:
            IP_input = input("IP or domain: ")
            
            if IP_input == None:
                print("Please input IP or domain (ex: 1.1.1.1 or google.com) ")
            else:
                os.system(f"dig {IP_input}")
        
        case ["whoami" | "-ami" | "ami"]:
            print(f"ITSToolKit $ user $ {platform.node()}")
        
        case ["-sc"]:
            filepath = input("Path/ : ")
            os.system(f"cat {filepath}")
        
        case ["exit" | "quit" | "stop"]:
            ask = input("Do you really want to quit?(y/n): ")
            if ask.lower() == "n" or "no":
                quit()
            elif ask.lower() == "y" or "yes":        
                print("Quitting ITSToolKit")
                time.sleep(0.2)
                quit()

            
        case ["ls" | "l" | "ll"]:
            os.system("ls")
        case ["ls", path, *rest]:
            if "-l" in rest:
                os.system("ls -l")
        
        case ["hash" | "-hs"]:
            hashing() 
        
        
        case ["cal" | "calculator"]:
            math_option = input("Which math option do you want (+/-/*/'/')?: ")

            if math_option.lower() == "+":
                num1 = input("Num1: ")
                num2 = input("Num2: ")
                print("Sum: ", int(num1) + int(num2))

            
            elif math_option.lower() == "-":
                num1 = input("Num1: ")
                num2 = input("Num2: ")
                print("Sum: ", int(num1) - int(num2))
            
            
            elif math_option.lower() == "*":
                num1 = input("Num1: ")
                num2 = input("Num2: ")
                print("Sum: ", int(num1) * int(num2))
            
            
            elif math_option.lower() == "/":
                num1 = input("Num1: ")
                num2 = input("Num2: ")
                print("Sum: ", int(num1) / int(num2))


        case ["cd", path]:
            if path == None:
                print(f"No directory {path}")
            elif FileNotFoundError:
                print(f"No Directory {path}")
            else:
                os.chdir(str(path))

        case ["python", *rest]:
            if "3" in rest:
                os.system("python3")
            else:
                os.system("python")

        case ["date"]:            
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            print(f"Current date is {current_time}")
            
            year = input("Year: ")
            month = input("Month: ")
            day = input("Day: ")
            print(calendar.month(int(year),int(month)), int(day))
            
        case ["time"]:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            print(f"Current date is {current_time}")

        case ["neofetch"]:
            os.system("neofetch")

        case ["base64", path]:
            if path == None or "" or " ":
                print(f"No directory {path}")
            else:
                os.system(f"base64 {path}")

        
        case ["ping" | "-p", ip]:
            os.system(f"ping {ip}")


        case ["Fib" | "fib" | "Fibonacci" | "-fn"]:
            FibNums()
            print(f"Done printing {numbs2Print} fibonacci numbers.")

        case ["inf" | "Information" | "-if", *rest]:
            # This just means that there will be more specific information given about the computer.
            # This should maybe not be used in public as if someone sees the output, and you have a outdated version of something
            # Then they can exploit it
            Computer_information_specific()

        case ["version"]:
            ToolVersion_1 = ToolVersion 
            print(f"Version {ToolVersion_1}")
            
        case _:
            if __name__ == "__main__":
                print(f"If the system command {command!r} did not run, try installing with sudo apt install {command!r} or sudo pacman -S {command!r}")
                print(f"If you are running mac, try installing with brew: brew install {command!r}")
                os.system(command)

              
def main() -> None:
    while 1:
        CRED = '\033[91m'
        CEND = '\033[0m'
        CBLUE   = '\33[34m'
        print(CRED + "_"*len(platform.node()) + CRED)
        command = input(CRED + str(platform.node()) + CEND + CBLUE + " ~$ " + CBLUE)
        print(CRED + "_"*len(platform.node()) + CRED)
        ITSToolKit(command)
        
        
if __name__ == "__main__":
    CRED = '\033[91m'
    os.system("neofetch")
    print(CRED + "_"*40 + CRED)
    print("Welcome " + platform.node())
    print(CRED + "_"*40 + CRED)
    main()