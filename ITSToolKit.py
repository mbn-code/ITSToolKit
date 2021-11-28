# | pIPe symb 
import os
import time            
import platform

def ITSToolKit(command: str) -> None:
    match command.split():
        case ["help"]:
            print("""
help, -h - show this menu
whois, -ws - gain information about a domain or ip
dig, -dg - query dns or ip
exit, quit, stop - exit/quit/stop the Tool
cat, -sc - show the contense of a file
                  """)
        case ["clear" | "cls" | "clean"]:
            print("exec: " + str(command))
            time.sleep(0.1)
            os.system("clear")
        
        case ["-ws"]:
            IP_input = input("IP, or domain: ")
            
            if IP_input == None:
                print("whois, missing parament (ex: IP, domain)")
            else:
                os.system(f"whois {IP_input}")
        
        case ["-dg"]:
            IP_input = input("IP or domain: ")
            
            if IP_input == None:
                print("Please input IP or domain (ex: 1.1.1.1 or google.com) ")
            else:
                os.system(f"dig {IP_input}")
        
        case ["whoami" | "-ami"]:
            print(f"ITSToolKit $ user $ {platform.node()}")
        
        case ["-sc"]:
            filepath = input("Path/ : ")
            os.system(f"cat {filepath}")
            
        
        case ["exit" | "quit" | "stop"]:
            print("Quitting ITSToolKit")
            time.sleep(0.2)
            quit()
            
        case ["ls"]:
            os.system("ls")
        case ["ls", *rest]:
            if "-l" in rest:
                os.system("ls -l")
        
        case _:
            if 1 == 1:
                print(f"If the system command {command!r} did not run, try installing with sudo apt install {command!r} or sudo pacman -S {command!r}")
                os.system(command)
            else:
                print(f"Unknown commmand: {command!r}.")
                    
              
def main() -> None:
    while 1:
        command = input("$ ")
        ITSToolKit(command)
        
        
if __name__ == "__main__":
    main()