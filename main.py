import os
import sys
import time
from colorama import init, Fore

init(autoreset=True)

def banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.GREEN + "       AUTOSCRIPT AI - SMART WORKSPACE UTILITY")
    print(Fore.CYAN + "=" * 50)

def organize_files(target_directory):
    print(Fore.YELLOW + f"\n[*] Scanning directory: {target_directory}")
    if not os.path.exists(target_directory):
        print(Fore.RED + "[!] Directory not found!")
        return

    files = os.listdir(target_directory)
    count = 0
    for file in files:
        if os.path.isfile(os.path.join(target_directory, file)):
            ext = file.split('.')[-1].lower()
            if ext:
                ext_dir = os.path.join(target_directory, ext.upper() + "_Files")
                os.makedirs(ext_dir, exist_ok=True)
                os.rename(os.path.join(target_directory, file), os.path.join(ext_dir, file))
                print(Fore.GREEN + f"[+] Moved: {file} -> {ext.upper()}_Files/")
                count += 1
    print(Fore.CYAN + f"\n[V] Successfully organized {count} files!")

def main():
    banner()
    while True:
        print(Fore.WHITE + "\nSelect an Option:")
        print("1. Organize Workspace Files")
        print("2. System Info Summary")
        print("3. Exit")
        
        choice = input(Fore.YELLOW + "\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            path = input(Fore.WHITE + "Enter folder path to organize: ").strip()
            organize_files(path)
        elif choice == '2':
            print(Fore.GREEN + "\n[+] System Platform:", sys.platform)
            print(Fore.GREEN + "[+] Current Working Directory:", os.getcwd())
            print(Fore.GREEN + "[+] Python Version:", sys.version.split()[0])
        elif choice == '3':
            print(Fore.CYAN + "Exiting... Happy Coding!")
            break
        else:
            print(Fore.RED + "[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
