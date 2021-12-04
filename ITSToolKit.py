# | pIPe symbol 
import os
import time            
import platform
import calendar

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


        case _:
            if __name__ == "__main__":
                print(f"If the system command {command!r} did not run, try installing with sudo apt install {command!r} or sudo pacman -S {command!r}")
                print(f"If you are running mac, try installing with brew: brew install {command!r}")
                os.system(command)
                
              
def main() -> None:
    while 1:
        command = input(platform.node() + " ~$ ")
        ITSToolKit(command)
        
        
if __name__ == "__main__":
    os.system("neofetch")
    print("Welcome " + platform.node())
    main()