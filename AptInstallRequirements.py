import os

def install():
    
    # Install the pip3 requirements
    os.system("pip3 install os")
    os.system("pip3 install time")
    os.system("pip3 install platform")
    os.system("pip3 install calendar")
    os.system("pip3 install hashlib")
    
    # Now install Apt requirements
    os.system("sudo apt install neofetch")
    
def uninstall():
    
    # remove the pip3 requirements
    os.system("pip3 uninstall os")
    os.system("pip3 uninstall time")
    os.system("pip3 uninstall platform")
    os.system("pip3 uninstall calendar")
    os.system("pip3 uninstall hashlib")
    
    # Now uninstall Apt requirements
    os.system("sudo apt remove neofetch")
    

if __name__ == "__main__":
    print("Apt installer / uninstaller")
    x_input = input("Do you want to install or uninstall?(I/UI): ")

    if x_input.lower == "i":
        install()
    elif x_input.lower() == "ui":
        uninstall()
