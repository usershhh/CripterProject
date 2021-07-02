# by Klayzz#0592

import os
from colorama import Fore
from hashlib import sha256

if os.name == 'nt':
    os.system("title Crypter by Klayzz#0592")


def clear():
    os.system("cls") if os.name == 'nt' else os.system("clear")


def exit():
    os.system("exit")


def main():
    clear()
    label()
    choice = input(Fore.MAGENTA + "[1] Crypt" + "\n[2] Decrypt" + "\n[3] Exit\n" + Fore.RESET)

    if choice == "1":
        crypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        exit()


def label():
    print(Fore.CYAN + """ 
                        ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓▓█████  ██▀███  
                        ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
                        ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
                        ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
                        ▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
                        ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░
                        ░   ░░ ▒░ ░░ ▒▓ ░▒▓░
                        ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░     ░ ░  ░  ░▒ ░ ▒░
                        ░          ░░   ░  ▒ ░░░         ░         ░     ░░   ░ 
                        ░ ░         ░      ░                       ░  ░   ░             by Klayzz#0592
                        ░                                                       

    """ + Fore.RESET)


def crypt():
    clear()
    if os.name == 'nt':
        os.system("title Crypter by Klayzz#0592")
    print(Fore.GREEN + """
                 ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄
                ▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  
                ██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪
                ▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·
                ·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀ 
     """ + Fore.RESET)
    input2 = input("Enter the name of the file to decrypt : ")
    output = input("Enter the name of the final file : ")
    key = input("Enter the key : ")
    key2 = sha256(key.encode("utf-8")).digest()
    with open(input2, "rb") as f_input:
        with open(output, "wb") as f_output:
            i = 0
            while f_input.peek():
                c = ord(f_input.read(1))
                j = i % len(key2)
                b = bytes([c ^ key2[j]])
                f_output.write(b)
                i = i + 1
    print(Fore.GREEN + "The file has been crypted" + Fore.RESET)
    input("\nPress to continue")
    main()


def decrypt():
    clear()
    if os.name == 'nt':
        os.system("title Decrypter by Klayzz#0592")
    print(Fore.RED + """
                 ·▄▄▄▄  ▄▄▄ . ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄
                 ██▪ ██ ▀▄.▀·▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  
                 ▐█· ▐█▌▐▀▀▪▄██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪
                 ██. ██ ▐█▄▄▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·
                 ▀▀▀▀▀•  ▀▀▀ ·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀ 
    """ + Fore.RESET)

    input2 = input("Enter the name of the file to decrypt : ")
    output = input("Enter the name of the final file : ")
    key = input("Enter the key : ")
    key2 = sha256(key.encode("utf-8")).digest()
    with open(input2, "rb") as f_input:
        with open(output, "wb") as f_output:
            i = 0
            while f_input.peek():
                c = ord(f_input.read(1))
                j = i % len(key2)
                b = bytes([c ^ key2[j]])
                f_output.write(b)
                i = i + 1
    print(Fore.GREEN + "The file has been decrypted" + Fore.RESET)
    input("\nPress to continue")
    main()


if __name__ == '__main__':
    main()