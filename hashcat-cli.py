# @Copyright (c) 2022 Organ13at0r
# https://t.me/Organ13at0r - Telegram

# |------------------------------------------------------------------------------------------------------------------------|
# |Псевдоинтерфейс командной строки для использования утилиты HashCat с дополнительными возможностями.                     |
# |Ее основная задача заключается в упрощение работы с HashCat.                                                            |
# |------------------------------------------------------------------------------------------------------------------------|

import sys, time, subprocess
try:
    from rich import print as rprint
    from rich.progress import track
except ImportError:
    print("Not founded modules!")
    subprocess.call(["pip3", "install", "-r", "requirements.txt"])
    sys.exit()

def getHashType() -> int:
    """
    Функция выводит список возможных типов хешей и возвращяет тип хеша выбранный пользователем.
    """
    with open("typesOfHash.txt", "r") as file:
        types = file.read()

    rprint(f"[italic yellow]{types}[/italic yellow]") # Отображение типов хешей

    while True:
        try:
            hashId = int(input("Id [-1 for quit] >>> ")) # Запрашиваем ID хеша
            if hashId == -1:
                subprocess.call("clear")
                break
            else:
                subprocess.call("clear")
                return hashId

        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].\n")
            continue

def getAttackType() -> str:
    """
    Функция возвращяет тип аттаки выбранный пользователем.
    """
    while True:
        rprint("\n[bold yellow]Attack mode:[/bold yellow]")
        rprint("\t[reverse blue][1][/reverse blue] -> Wordlist")
        rprint("\t[reverse blue][2][/reverse blue] -> BruteForce")
        rprint("\t[reverse red][-1][/reverse red] -> Main menu")

        try:
            attackId = int(input("\nId [-1 for quit] >>> ")) # Запрашиваем ID аттаки
            if attackId == 1:
                subprocess.call("clear")
                return "Wordlist"
            elif attackId == 2:
                subprocess.call("clear")
                return "Bruteforce"
            elif attackId == -1:
                subprocess.call("clear")
                break

        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].")
            continue

def getWordlist() -> str:
    """
    Функция запрашивает и возвращяет cписок паролей введенный пользователем.
    """
    while True:
        try:
            pathToWordlist = input("\nPath to the wordlist [Q to exit]: ") # Запрашиваем путь до списка
            if pathToWordlist.lower() == "q":
                subprocess.call("clear")
                break
            else:
                subprocess.call("clear")
                return pathToWordlist

        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Path must be a string[/italic].\n")
            continue

def getDevices() -> int:
    """
    Функция запрашивает и возвращяет тип устройства которое будет использоваться для взлома пароля.
    """
    while True:
        rprint("[bold yellow]Devices:[/bold yellow]")
        rprint("\t[reverse blue][1][/reverse blue] CPU")
        rprint("\t[reverse blue][2][/reverse blue] GPU")
        rprint("\t[reverse blue][3][/reverse blue] CPU and GPU")
        rprint("\t[reverse red][-1][/reverse red] -> Main menu")

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
            elif devicesId == -1:
                subprocess.call("clear")
                break

        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].\n")
            continue

def getMask() -> str:
    """
    Функция запрашивает и возвращяет маску
    """
    while True:
        rprint("""[bold yellow]
  ?l | abcdefghijklmnopqrstuvwxyz
  ?u | ABCDEFGHIJKLMNOPQRSTUVWXYZ
  ?d | 0123456789
  ?h | 0123456789abcdef
  ?H | 0123456789ABCDEF
  ?s | !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  ?a | ?l?u?d?s
  ?b | 0x00 - 0xff
        [/bold yellow]""")

        try:
            maskType = input("Mask [Q for quit] >> ")
            if maskType.lower() == "q":
                subprocess.call("clear")
                break
            else:
                subprocess.call("clear")
                return maskType

        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Mask must be a string[/italic].\n")
            continue

def attackWithWordlist(hashType: int, devices: int, wordlist: str) -> None:
    """
    Функция запускает процесс взлома на основе словаря.
    """
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

def attackWithMask(hashType: int, devices: int, mask: str) -> None:
    """
    Функция запускает процесс взлома на основе маски.
    """
    subprocess.call("clear")
    try:
        sessionName = input("Enter a session name: ")
        fileWithHash = input("Enter file with hash for decrypt: ")
        if devices == 3:
            subprocess.call(["xterm", "-e", "hashcat", "-m", str(hashType), "-a", "3", fileWithHash, mask, "--force", "-D", "1,2", "--status", "--session", sessionName])
        else:
            subprocess.call(["xterm", "-e", "hashcat", "-m", str(hashType), "-a", "3", fileWithHash, mask, "--force", "-D", str(devices), "--status", "--session", sessionName])
    except ValueError:
        rprint("[bold red]Error![/bold red] -> [italic]Session name, and Hash file must be a string[/italic].\n")

def restoreSession() -> None:
    """
    Функция востанавливает прерванную сессию.
    """
    subprocess.call("clear")
    try:
        sessionName = input("Enter a session name: ")
        subprocess.call(["xterm", "-e", "hashcat", "--session", sessionName, "--restore"])
    except ValueError:
        rprint("[bold red]Error![/bold red] -> [italic]Session name must be a string[/italic].\n")

def main():
    try:
        rprint("[bold green]Hashcat version[/bold green]")
        subprocess.call(["sudo", "hashcat", "--version"])
        print()
    except:
        rprint("[bold red]Error![/bold red] -> [italic]You must intall the hashcat[/italic]\n")
        sys.exit()

    for i in track(range(100)): # Прогресс бар
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

    rprint("[bold green]Made by Organ13at0r[/bold green]")

    hashType: int = None
    attackType: str = None
    devices: int = None # CPY, GPU или оба
    wordlist: str = None
    mask: str = None

    while True:
        rprint(f"\n[bold blue]Hash type:[/bold blue] {hashType}")
        rprint(f"[bold blue]Attack type:[/bold blue] {attackType}")
        rprint(f"[bold blue]Devices:[/bold blue] {devices} -> (1) CPU, (2) GPU, (3) Both")
        rprint(f"[bold blue]Wordlist:[/bold blue] {wordlist}")
        rprint(f"[bold blue]Mask:[/bold blue] {mask}")

        rprint("\n[reverse blue][1][/reverse blue]   -> Choose hash type.")
        rprint("[reverse blue][2][/reverse blue]   -> Choose attack type.")
        rprint("[reverse blue][3][/reverse blue]   -> Choose CPU, GPU, or both.")
        rprint("[reverse blue][4][/reverse blue]   -> Set wordlist.")
        rprint("[reverse blue][5][/reverse blue]   -> Start attack.")
        rprint("[reverse blue][6][/reverse blue]   -> Restore session.")
        rprint("[reverse blue][7][/reverse blue]   -> Set mask.")
        rprint("[reverse red][-1][/reverse red]  -> Exit.\n")

        try:
            response = int(input("Response >>> "))
        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Response must be a digit[/italic].")
            continue
        if response == -1:
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
                    attackWithMask(hashType, devices, mask)
                else:
                    rprint("[bold red]Error![/bold red] -> [italic]You must correct the parameters for attack.[/italic]\n")
        elif response == 6:
            restoreSession()
        elif response == 7:
            mask = getMask()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:   # Если нажата Ctrl-C
        rprint("\n[bold red]Cancelled...[/bold red]")
        time.sleep(1)

        subprocess.call("clear")
        sys.exit()
