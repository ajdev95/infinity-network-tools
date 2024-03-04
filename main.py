import requests
from concurrent.futures import ThreadPoolExecutor
import time
from colorama import Fore, Style
from datetime import datetime, timezone

current_time = datetime.now().strftime("%I:%M:%S %p")

def check_user_profile(username):
    try:
        response = requests.get(f"https://in8.network/users/{username}")

        if response.status_code == 200:
            print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTRED_EX}<+>{Fore.RESET} {Fore.RESET} {Fore.LIGHTRED_EX}{username}{Fore.RESET} is{Fore.LIGHTRED_EX} invalid! {Fore.RESET}")
        else:
            print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTGREEN_EX}<+>{Fore.RESET} {Fore.RESET} {Fore.LIGHTGREEN_EX}{username}{Fore.RESET} is{Fore.LIGHTGREEN_EX} valid! {Fore.RESET}")
    except requests.RequestException as e:
        print(f"error checking this username {username}, error={e}")

def read_and_check_usernames(filename):
    try:
        with open(filename, 'r') as file:
            usernames = file.read().splitlines()

        print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTGREEN_EX}<+>{Fore.RESET} {Fore.RESET}Successfully read the usernames from the file")
        print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTBLUE_EX}<+>{Fore.RESET} {Fore.RESET}Checking usernames please wait..")

        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(check_user_profile, usernames)
        
    except IOError as e:
        print(f"{Fore.RED}{Style.BRIGHT}Error reading file: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

start_time = time.time()
read_and_check_usernames('usernames.txt')
end_time = time.time()
print(f"\n{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTGREEN_EX}<+>{Fore.RESET} {Fore.RESET}Successfully checked all usernames in the file {Fore.LIGHTBLACK_EX}time={Fore.RESET}{Fore.LIGHTWHITE_EX}{end_time - start_time:.2f}s..")