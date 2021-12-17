# This has not been tested yet.

import os

def install():


    # Move the ITSToolKit.sh to the /bin/ directory
    os.system("mv ITSToolKit.py ~bin/")
    os.system("mv ITSToolKit.sh ~bin/")
    
    # Install the pip3 requirements
    os.system("pip3 install os")
    os.system("pip3 install time")
    os.system("pip3 install platform")
    os.system("pip3 install calendar")
    os.system("pip3 install hashlib")
    
    # Now install brew requirements
    os.system(" brew install neofetch")
    os.system(" brew install base64")
    
    
def uninstall():
    
    # remove the pip3 requirements
    os.system("pip3 uninstall os")
    os.system("pip3 uninstall time")
    os.system("pip3 uninstall platform")
    os.system("pip3 uninstall calendar")
    os.system("pip3 uninstall hashlib")
    
    # Now uninstall brew requirements
    os.system("brew remove neofetch")
    os.system("brew remove base64")
    
    # remove the ITSToolKit py and sh
    os.system("sudo rm -r ~/bin/ITSToolKit.py")
    os.system("sudo rm -r ~/bin/ITSToolKit.sh")
    

if __name__ == "__main__":
    xinput = input("Install or uninstall: ")
    
    if xinput.lower() == "i" or "install":
        install()
    else: uninstall()