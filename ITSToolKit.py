# Imports
import calendar
import os
import platform
import re
import socket
import time
import uuid
import psutil
import hashlib
import whois
from ipwhois import IPWhois
import dns.resolver
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.progress import Progress, BarColumn, TextColumn
from rich.spinner import Spinner

console = Console()
session = PromptSession()

def animate_loading(message: str):
    spinner = Spinner("dots")
    with console.status(f"[bold green]{message}...", spinner=spinner):
        time.sleep(2)

def display_banner():
    banner = """
    ████████╗████████╗███████╗████████╗ ██████╗ ██████╗ ██╗     ██╗  ██╗███████╗████████╗
    ╚══██╔══╝╚══██╔══╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║     ██║  ██║██╔════╝╚══██╔══╝
       ██║      ██║   █████╗     ██║   ██║   ██║██████╔╝██║     ██║  ██║█████╗     ██║   
       ██║      ██║   ██╔══╝     ██║   ██║   ██║██╔══██╗██║     ██║  ██║██╔══╝     ██║   
       ██║      ██║   ███████╗   ██║   ╚██████╔╝██████╔╝███████╗╚██████╔╝███████╗   ██║   
       ╚═╝      ╚═╝   ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   
    """
    console.print(Panel(Align.center(banner), border_style="bold green"))

def display_main_menu():
    menu = """
    [bold cyan]Main Menu[/bold cyan]
    [1] System Information
    [2] Hashing
    [3] Fibonacci Numbers
    [4] Whois Lookup
    [5] IP Lookup
    [6] DNS Query
    [7] Calculator
    [8] Base64 Encode/Decode
    [9] Network Scan
    [10] Ping Test
    [11] Disk Usage
    [12] Current Weather
    [13] Exit
    """
    console.print(Panel(menu, title="[bold magenta]ITSToolKit[/bold magenta]", border_style="bold blue"))

def get_user_choice():
    choice = Prompt.ask("[bold yellow]Select an option (1-13)[/bold yellow]")
    return choice

def system_information():
    ToolVersion = "1.79"
    addrs = psutil.net_if_addrs()

    table = Table(title="System Information", box=box.DOUBLE_EDGE)
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("ToolKit version", ToolVersion)
    table.add_row("Computer name", platform.node())
    table.add_row("Operating system", platform.platform())
    table.add_row("Operating system version", platform.version())
    table.add_row("Release", platform.release())
    table.add_row("Architecture", platform.machine())
    table.add_row("Python compiler", platform.python_compiler())
    table.add_row("Processor", platform.processor())
    table.add_row("RAM", str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
    table.add_row("IP address", socket.gethostbyname(socket.gethostname()))
    table.add_row("MAC address", ':'.join(re.findall('..', '%012x' % uuid.getnode())))

    console.print(table)

def hashing():
    console.print("Hashing types:", style="bold magenta")
    hash_types = ["md5", "sha1", "sha256", "sha512"]
    for ht in hash_types:
        console.print(f"- {ht}", style="bold cyan")

    which_hash_type = Prompt.ask("[bold yellow]Which hash type do you want to hash your string in?[/bold yellow]")
    hashinput = Prompt.ask("[bold yellow]Plain text:[/bold yellow]")

    def md5_hash(data):
        hash_object = hashlib.md5()
        hash_object.update(str(data).encode())
        console.print(f"[bold green]Hash:[/bold green] {hash_object.hexdigest()}")

    def sha1_hash(data):
        hash_object = hashlib.sha1()
        hash_object.update(str(data).encode())
        console.print(f"[bold green]Hash:[/bold green] {hash_object.hexdigest()}")

    def sha256(data):
        hash_object = hashlib.sha256()
        hash_object.update(str(data).encode())
        console.print(f"[bold green]Hash:[/bold green] {hash_object.hexdigest()}")

    def sha512(data):
        hash_object = hashlib.sha512()
        hash_object.update(str(data).encode())
        console.print(f"[bold green]Hash:[/bold green] {hash_object.hexdigest()}")

    def choose():
        if not hashinput:
            console.print("[bold red]Enter hash type md5, sha1, sha256, or sha512[/bold red]")
        elif which_hash_type.lower() == "md5":
            md5_hash(data=hashinput)
        elif which_hash_type.lower() == "sha1":
            sha1_hash(data=hashinput)
        elif which_hash_type.lower() == "sha256":
            sha256(data=hashinput)
        elif which_hash_type.lower() == "sha512":
            sha512(data=hashinput)

    choose()

def fibonacci_numbers():
    numbs2Print = Prompt.ask("[bold yellow]Fibonacci numbers to print:[/bold yellow]", default="10")

    console.print(f"[bold blue]Printing the first {numbs2Print} Fibonacci numbers[/bold blue]")
    
    def print_fibonacci_numbers(n: int) -> None:
        f1, f2 = 0, 1
        if n < 1:
            return
        console.print(f"[bold green]{f1}[/bold green]")
        for x in range(1, n):
            console.print(f"[bold green]{f2}[/bold green]")
            f1, f2 = f2, f1 + f2

    print_fibonacci_numbers(int(numbs2Print))

def whois_lookup(domain: str):
    try:
        w = whois.whois(domain)
        table = Table(title=f"Whois Information for {domain}", box=box.ROUNDED)
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="magenta")
        
        for key, value in w.items():
            table.add_row(str(key), str(value))
        
        console.print(table)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def ip_lookup(ip: str):
    try:
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        table = Table(title=f"IP Whois Information for {ip}", box=box.ROUNDED)
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="magenta")
        
        for key, value in res.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    table.add_row(f"{key} - {sub_key}", str(sub_value))
            else:
                table.add_row(str(key), str(value))
        
        console.print(table)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def dns_query(domain: str):
    try:
        result = dns.resolver.resolve(domain, 'A')
        table = Table(title=f"DNS A Records for {domain}", box=box.ROUNDED)
        table.add_column("Name", style="cyan")
        table.add_column("Address", style="magenta")

        for ipval in result:
            table.add_row(domain, ipval.to_text())

        console.print(table)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def calculator():
    operation = Prompt.ask("[bold yellow]Choose an operation (+, -, *, /):[/bold yellow]")
    num1 = Prompt.ask("[bold yellow]Enter first number:[/bold yellow]", default="0")
    num2 = Prompt.ask("[bold yellow]Enter second number:[/bold yellow]", default="0")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        console.print("[bold red]Invalid input! Please enter numbers only.[/bold red]")
        return

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            console.print("[bold red]Cannot divide by zero![/bold red]")
            return
        result = num1 / num2
    else:
        console.print("[bold red]Invalid operation![/bold red]")
        return

    console.print(f"[bold green]Result:[/bold green] {result}")

def base64_encode_decode():
    choice = Prompt.ask("[bold yellow]Choose (encode/decode):[/bold yellow]")
    filepath = Prompt.ask("[bold yellow]Enter file path:[/bold yellow]")

    if choice == "encode":
        os.system(f"base64 {filepath}")
    elif choice == "decode":
        os.system(f"base64 -d {filepath}")
    else:
        console.print("[bold red]Invalid choice![/bold red]")

def network_scan():
    ip_range = Prompt.ask("[bold yellow]Enter IP range (e.g., 192.168.1.0/24):[/bold yellow]")
    console.print(f"[bold green]Scanning network: {ip_range}...[/bold green]")
    os.system(f"nmap -sP {ip_range}")

def ping_test():
    ip = Prompt.ask("[bold yellow]Enter IP address to ping:[/bold yellow]")
    console.print(f"[bold green]Pinging {ip}...[/bold green]")
    
    with console.status("[bold cyan]Executing ping command...[/bold cyan]", spinner="dots"):
        result = os.popen(f"ping -c 4 {ip}").read()
    
    console.print(f"[bold blue]Ping Results for {ip}[/bold blue]")
    console.print(result)

def disk_usage():
    usage = psutil.disk_usage('/')
    table = Table(title="Disk Usage", box=box.ROUNDED)
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Total", f"{usage.total / (1024**3):.2f} GB")
    table.add_row("Used", f"{usage.used / (1024**3):.2f} GB")
    table.add_row("Free", f"{usage.free / (1024**3):.2f} GB")
    table.add_row("Percentage", f"{usage.percent}%")

    console.print(table)

def current_weather():
    city = Prompt.ask("[bold yellow]Enter city name:[/bold yellow]")
    console.print(f"[bold green]Fetching weather for {city}...[/bold green]")
    # Placeholder for weather API integration
    console.print(f"[bold blue]Weather information for {city}[/bold blue]")
    console.print("Temperature: 20°C\nCondition: Clear")

def main() -> None:
    display_banner()
    while True:
        display_main_menu()
        choice = get_user_choice()
        if choice == "1":
            system_information()
        elif choice == "2":
            hashing()
        elif choice == "3":
            fibonacci_numbers()
        elif choice == "4":
            domain = Prompt.ask("[bold yellow]Enter the domain to look up:[/bold yellow]")
            whois_lookup(domain)
        elif choice == "5":
            ip = Prompt.ask("[bold yellow]Enter the IP address to look up:[/bold yellow]")
            ip_lookup(ip)
        elif choice == "6":
            domain = Prompt.ask("[bold yellow]Enter the domain to query DNS:[/bold yellow]")
            dns_query(domain)
        elif choice == "7":
            calculator()
        elif choice == "8":
            base64_encode_decode()
        elif choice == "9":
            network_scan()
        elif choice == "10":
            ping_test()
        elif choice == "11":
            disk_usage()
        elif choice == "12":
            current_weather()
        elif choice == "13":
            console.print("[bold red]Exiting ITSToolKit...[/bold red]")
            break
        else:
            console.print("[bold red]Invalid choice! Please select a valid option.[/bold red]")

if __name__ == "__main__":
    main()
