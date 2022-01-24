# @Copyright (c) 2022 Organ13at0r

import sys, time, subprocess
try:
    from rich import print as rprint
    from rich.progress import track
except ImportError:
    print("Not founded modules!")
    print("Please start: python3 install -r requirements.txt")
    sys.exit()

def getHashType():
    with open("typesOfHash", "r") as file:
        types = file.read()

    rprint(f"[italic yellow]{types}[/italic yellow]") # Print the list of hash types

    while True:
        try:
            typesId = int(input("Id >>> "))

            if typesId == 0:
                subprocess.call("clear")
                break

            subprocess.call("clear")
            return typesId
        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].\n")
            continue

def getAttackType():
    while True:
        rprint("[bold yellow]Attack mode:[/bold yellow]")
        rprint("\t[reverse blue][1][/reverse blue] -> Wordlist")
        rprint("\t[reverse blue][2][/reverse blue] -> BruteForce")
        rprint("\t[reverse red][0][/reverse red] -> Main menu")

        try:
            attackId = int(input("\nId >>> "))
            if attackId == 1:
                subprocess.call("clear")
                return "Wordlist"
            elif attackId == 2:
                subprocess.call("clear")
                return "Bruteforce"
            elif attackId == 0:
                subprocess.call("clear")
                break

        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].\n")
            continue

def getWordlist():
    while True:
        try:
            wordlist = str(input("\nPath to the wordlist [Q to exit]: "))

            if wordlist.lower() == "q":
                subprocess.call("clear")
                break

            subprocess.call("clear")
            return wordlist

        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Path must be a string[/italic].\n")
            continue

def getDevices():
    while True:
        rprint("[bold yellow]Devices:[/bold yellow]")
        rprint("\t[reverse blue][1][/reverse blue] CPU")
        rprint("\t[reverse blue][2][/reverse blue] GPU")
        rprint("\t[reverse blue][3][/reverse blue] CPU and GPU")
        rprint("\t[reverse red][0][/reverse red] -> Main menu")

        try:
            devicesId = int(input("\nId >>> "))

            if devicesId == 1:
                subprocess.call("clear")
                return 1
            elif devicesId == 2:
                subprocess.call("clear")
                return 2
            elif devicesId == 3:
                subprocess.call("clear")
                return 3
            elif devicesId == 0:
                subprocess.call("clear")
                break

        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].\n")
            continue

def attackWithWordlist(hashType, devices, wordlist):
    subprocess.call("clear")
    try:
        sessionName = input("Enter a session name: ")
        fileWithHash = input("Enter file with hash for decrypt: ")
        if devices == 3:
            subprocess.call(["xterm", "-e", "hashcat", "-m", str(hashType), "-a", "0", fileWithHash, wordlist, "--force", "-D", "1,2", "--status", "--session", sessionName])
        else:
            subprocess.call(["xterm", "-e", "hashcat", "-m", str(hashType), "-a", "0", fileWithHash, wordlist, "--force", "-D", str(devices), "--status", "--session", sessionName])
    except ValueError:
        rprint("[bold red]Error![/bold red] -> [italic]Session name, and Hash file must be a string[/italic].\n")

def main():
    try:
        rprint("[bold green]Hashcat version[/bold green]")
        subprocess.call(["sudo", "hashcat", "--version"])
        print()
    except:
        rprint("[bold red]Error![/bold red] -> [italic]You must intall the hashcat[/italic]\n")
        sys.exit()

    for i in track(range(100)):
        time.sleep(0.01)

    subprocess.call("clear")

    rprint("""[blink green]
    |||         |||       //---||           /----------|||         |||  |||||||||||       //---|| ||||||||||||
    |||         |||      //    ||          //----------|||         |||  |||              //    ||     \  /
    |||         |||     //     ||         //           |||         |||  |||             //     ||      ||
    |||---------|||    //------||        //            |||---------|||  |||            //------||      ||
    |||---------|||   //-------||       //             |||---------|||  |||           //-------||      ||
    |||         |||  //        ||      //              |||         |||  |||          //        ||      ||
    |||         ||| //         ||-----//               |||         |||  |||         //         ||      ||
    |||         |||//          ||----//                |||         |||__|||||||||||//          ||______||
    [/blink green]""")

    hashType = None
    attackType = None
    devices = None # CPY, GPU or both
    wordlist = None
    mask = None

    while True:
        rprint(f"[bold blue]Hash type:[/bold blue] {hashType}")
        rprint(f"[bold blue]Attack type:[/bold blue] {attackType}")
        rprint(f"[bold blue]Devices:[/bold blue] {devices} -> (1) CPU, (2) GPU, (3) Both")
        rprint(f"[bold blue]Wordlist:[/bold blue] {wordlist}")
        rprint(f"[bold blue]Mask:[/bold blue] {mask}")

        rprint("\n[reverse blue][1][/reverse blue] -> Choose hash type.")
        rprint("[reverse blue][2][/reverse blue] -> Choose attack type.")
        rprint("[reverse blue][3][/reverse blue] -> Choose CPU, GPU, or both.")
        rprint("[reverse blue][4][/reverse blue] -> Set wordlist.")
        rprint("[reverse blue][5][/reverse blue] -> Start attack.")
        rprint("[reverse blue][0][/reverse blue] -> Exit.")

        try:
            response = int(input("\nResponse >>> "))
        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Response must be a digit[/italic].\n")
            continue

        if response == 0:
            rprint("\n[bold red]Cancelled...[/bold red]")
            time.sleep(1)

            subprocess.call("clear")

            sys.exit()

        elif response == 1:
            hashType = getHashType()

        elif response == 2:
            attackType = getAttackType()

        elif response == 3:
            devices = getDevices()

        elif response == 4:
            wordlist = getWordlist()

        elif response == 5:
            if attackType == "Wordlist":
                if not None in [hashType, devices, wordlist]:
                    attackWithWordlist(hashType, devices, wordlist)
                else:
                    rprint("[bold red]Error![/bold red] -> [italic]You must correct the parameters for attack.[/italic]\n")

            elif attackType == "Bruteforce":
                if not None in [hashType, devices, mask]:
                    ...
                else:
                    rprint("[bold red]Error![/bold red] -> [italic]You must correct the parameters for attack.[/italic]\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        rprint("\n[bold red]Cancelled...[/bold red]")
        time.sleep(1)

        subprocess.call("clear")

        sys.exit()
