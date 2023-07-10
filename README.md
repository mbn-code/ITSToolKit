# ITSToolKit

This is the Indian Tech Support Tool Kit "ITSToolKit". Click [here](https://github.com/CollinEdward/ITSToolKit/releases/tag/ITSToolKit) to go to the v1.080 release, which is the first stable build tested on multiple operating systems and different hardware.

**Note:** This toolkit requires Python 3.10. You cannot use any other version because it utilizes the new `match` "case" feature introduced in Python 3.10.

If you want to use the toolkit by simply typing "ITSToolKit" in the terminal, follow these steps:

1. Add `ITSToolKit.py` and `ITSToolKit.sh` to the `/bin/` folder.
2. You can do this manually or use the `AptInstaller.py` or `PacmanInstallerReq.py` (depending on your distribution) file to automate the process. These files will also install all the required dependencies for the toolkit.

Thank you for using ITSToolKit. Enjoy the toolkit!

## Autostart Help

![README file](AutoStart_TerminalHelp/README_help.md)

## Future Updates

Adding an update command or file so you can easily get the newest version of the ToolKit, and don't have to manually download the script and run the Apt installer.

![Screenshot](Other-python-icon.png)

## Instructions for Installing (CLI)

To install ITSToolKit via the command line interface (CLI), follow these steps:

```bash
git clone https://github.com/CollinEdward/ITSToolKit.git
cd ITSToolKit
python3 AptInstaller.py or python3 PacmanInstallerReq.py
```


Preview for toolkit

![Screenshot](Preview_colours_help.png)

## Note

When using this software, you need to install additional tools for it to work properly. If these tools are not already installed, the software may break. You have two options for installing the secondary software:

1. Manual Installation: Install the software listed below manually by executing the respective commands in your command shell.
2. Automatic Installation: Use the provided scripts to install the software automatically.

To install the required software using pip3, run the following command:

pip3 install -r requirements.txt

For Debian-based systems, use the "AptInstallRequirements.py" script:

python3 AptInstallRequirements.py

For Arch Linux-based systems, use the "PacmanInstallRequirements.py" script:

python3 PacmanInstallRequirements.py

### Software to Install Manually

#### PIP3
You can install the following packages using pip3:
```bash
pip3 install os
pip3 install time
pip3 install platform
pip3 install calendar
pip3 install hashlib
```

Debian

To install the required package on Debian, use the following command:

apt install neofetch

Arch Linux

To install the required package on Arch Linux, use the following command:

pacman -S neofetch
