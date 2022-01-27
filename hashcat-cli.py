# @Copyright (c) 2022 Organ13at0r
# https://t.me/Organ13at0r - Telegram

# |-----------------------------------------------------------------------------------------------------------------|
# |Псевдоинтерфейс командной строки для использования утилиты HashCat с дополнительными возможностями.              |
# |Ее основная задача заключается в упрощение работы с HashCat.                                                     |
# |-----------------------------------------------------------------------------------------------------------------|

import sys
import time
import subprocess
try:
    from rich import print as rprint
    from rich.progress import track
except ImportError:
    print("Not founded modules!")
    subprocess.call(["pip3", "install", "-r", "requirements.txt"])
    sys.exit()


def get_hash_type() -> int:
    """
    Функция выводит список возможных типов хешей и возвращяет тип хеша выбранный пользователем.
    """
    try:
        with open("typesOfHash.txt", "r") as file:
            types = file.read()
    except FileNotFoundError:
        rprint("[bold red]ERROR: File was't founded![/bold red]")

    rprint(f"[italic yellow]{types}[/italic yellow]")  # Отображение типов хешей

    while True:
        try:
            hash_id = int(input("Id [-1 for quit] >>> "))  # Запрашиваем ID хеша
            if hash_id == -1:
                subprocess.call("clear")
                break
            else:
                subprocess.call("clear")
                return hash_id
        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].\n")
            continue


def get_attack_type() -> str:
    """
    Функция возвращяет тип аттаки выбранный пользователем.
    """
    while True:
        rprint("\n[bold yellow]Attack mode:[/bold yellow]")
        rprint("\t[reverse blue][1][/reverse blue] -> Wordlist")
        rprint("\t[reverse blue][2][/reverse blue] -> BruteForce")
        rprint("\t[reverse red][-1][/reverse red] -> Main menu")
        try:
            attack_id = int(input("\nId [-1 for quit] >>> "))  # Запрашиваем ID аттаки
            if attack_id == 1:
                subprocess.call("clear")
                return "Wordlist"
            elif attack_id == 2:
                subprocess.call("clear")
                return "Bruteforce"
            elif attack_id == -1:
                subprocess.call("clear")
                break
        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].")
            continue


def get_wordlist() -> str:
    """
    Функция запрашивает и возвращяет cписок паролей введенный пользователем.
    """
    while True:
        try:
            path_to_wordlist = input("\nPath to the wordlist [Q to exit]: ")  # Запрашиваем путь до списка
            if path_to_wordlist.lower() == "q":
                subprocess.call("clear")
                break
            else:
                subprocess.call("clear")
                return path_to_wordlist
        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Path must be a string[/italic].\n")
            continue


def get_devices() -> int:
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
            devices_id = int(input("\nId >>> "))
            if devices_id == 1:
                subprocess.call("clear")
                return 1
            elif devices_id == 2:
                subprocess.call("clear")
                return 2
            elif devices_id == 3:
                subprocess.call("clear")
                return 3
            elif devices_id == -1:
                subprocess.call("clear")
                break
        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Id must be a digit[/italic].\n")
            continue


def get_mask() -> str:
    """
    Функция запрашивает и возвращяет маску
    """
    while True:
        rprint(r"""[bold yellow]
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
            mask_type = input("Mask [Q for quit] >> ")
            if mask_type.lower() == "q":
                subprocess.call("clear")
                break
            else:
                subprocess.call("clear")
                return mask_type
        except ValueError:
            rprint("[bold red]Error![/bold red] -> [italic]Mask must be a string[/italic].\n")
            continue


def attack_with_wordlist(hash_type: int, devices: int, wordlist: str) -> None:
    """
    Функция запускает процесс взлома на основе словаря.
    """
    subprocess.call("clear")
    try:
        session_name = input("Enter a session name: ")
        file_with_hash = input("Enter file with hash for decrypt: ")
        if devices == 3:
            subprocess.call(
                ["xterm", "-e", "hashcat", "-m", str(hash_type), "-a", "0", file_with_hash, wordlist, "--force", "-D",
                 "1,2", "--status", "--session", session_name])
        else:
            subprocess.call(
                ["xterm", "-e", "hashcat", "-m", str(hash_type), "-a", "0", file_with_hash, wordlist, "--force", "-D",
                 str(devices), "--status", "--session", session_name])
    except ValueError:
        rprint("[bold red]Error![/bold red] -> [italic]Session name, and Hash file must be a string[/italic].\n")


def attack_with_mask(hash_type: int, devices: int, mask: str) -> None:
    """
    Функция запускает процесс взлома на основе маски.
    """
    subprocess.call("clear")
    try:
        session_name = input("Enter a session name: ")
        file_with_hash = input("Enter file with hash for decrypt: ")
        if devices == 3:
            subprocess.call(
                ["xterm", "-e", "hashcat", "-m", str(hash_type), "-a", "3", file_with_hash, mask, "--force", "-D",
                 "1,2", "--status", "--session", session_name])
        else:
            subprocess.call(
                ["xterm", "-e", "hashcat", "-m", str(hash_type), "-a", "3", file_with_hash, mask, "--force", "-D",
                 str(devices), "--status", "--session", session_name])
    except ValueError:
        rprint("[bold red]Error![/bold red] -> [italic]Session name, and Hash file must be a string[/italic].\n")


def restore_session() -> None:
    """
    Функция востанавливает прерванную сессию.
    """
    subprocess.call("clear")
    try:
        session_name = input("Enter a session name: ")
        subprocess.call(["xterm", "-e", "hashcat", "--session", session_name, "--restore"])
    except ValueError:
        rprint("[bold red]Error![/bold red] -> [italic]Session name must be a string[/italic].\n")


def main():
    try:
        rprint("[bold green]Hashcat version[/bold green]")
        subprocess.call(["sudo", "hashcat", "--version"])
        print()
    except:
        rprint("[bold red]Error![/bold red] -> [italic]You must install the hashcat[/italic]\n")
        sys.exit()

    for _ in track(range(100)):  # Прогресс бар
        time.sleep(0.01)

    subprocess.call("clear")

    rprint(r"""[blink green]
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

    hash_type = int()
    attack_type = str()
    devices = int()  # CPY, GPU или оба
    wordlist = str()
    mask = str()

    while True:
        rprint(f"\n[bold blue]Hash type:[/bold blue] {hash_type}")
        rprint(f"[bold blue]Attack type:[/bold blue] {attack_type}")
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
            hash_type = get_hash_type()
        elif response == 2:
            attack_type = get_attack_type()
        elif response == 3:
            devices = get_devices()
        elif response == 4:
            wordlist = get_wordlist()
        elif response == 5:
            if attack_type == "Wordlist":
                if None not in [hash_type, devices, wordlist]:
                    attack_with_wordlist(hash_type, devices, wordlist)
                else:
                    rprint(
                        "[bold red]Error![/bold red] -> [italic]You must correct the parameters for attack.[/italic]\n")
            elif attack_type == "Bruteforce":
                if None not in [hash_type, devices, mask]:
                    attack_with_mask(hash_type, devices, mask)
                else:
                    rprint(
                        "[bold red]Error![/bold red] -> [italic]You must correct the parameters for attack.[/italic]\n")
        elif response == 6:
            restore_session()
        elif response == 7:
            mask = get_mask()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:  # Если нажата Ctrl-C производи выход.
        rprint("\n[bold red]Cancelled...[/bold red]")
        time.sleep(1)

        subprocess.call("clear")
        sys.exit()
