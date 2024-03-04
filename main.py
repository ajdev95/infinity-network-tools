import requests
from concurrent.futures import ThreadPoolExecutor
import time
from colorama import Fore, Style
from datetime import datetime
from bs4 import BeautifulSoup

current_time = datetime.now().strftime("%I:%M:%S %p")

def check_user_profile(username):
    try:
        response = requests.get(f"https://in8.network/users/{username}")

        if response.status_code == 200:
            balance = parse_balance(response.text)
            has_infinity_founder = parse_badge(response.text, "crown")
            has_staff = parse_badge(response.text, "Staff")
            has_developer = parse_badge(response.text, "Developer")
            has_bug_hunter = parse_badge(response.text, "bugHunter")
            has_premium = parse_badge(response.text, "Premium")
            
            print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTRED_EX}<+>{Fore.RESET} {Fore.RESET}{Fore.LIGHTRED_EX}{username}{Fore.RESET} is{Fore.LIGHTRED_EX} invalid!{Fore.RESET}{Fore.RESET} {Fore.LIGHTBLACK_EX}coins={Fore.RESET}{Fore.LIGHTWHITE_EX}{balance} coins {Fore.LIGHTBLACK_EX}infinity_founder={Fore.RESET}{has_infinity_founder} {Fore.LIGHTBLACK_EX}staff={Fore.RESET}{has_staff} {Fore.LIGHTBLACK_EX}developer={Fore.RESET}{has_developer} {Fore.LIGHTBLACK_EX}bug_hunter={Fore.RESET}{has_bug_hunter} {Fore.LIGHTBLACK_EX}premium={Fore.RESET}{has_premium}")
        else:
            print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTGREEN_EX}<+>{Fore.RESET} {Fore.RESET}{Fore.LIGHTGREEN_EX}{username}{Fore.RESET} is{Fore.LIGHTGREEN_EX} valid!")
    except requests.RequestException as e:
        print(f"error checking this username {username}, error={e}")

def parse_balance(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    balance_tag = soup.find('p', class_='coins')
    if balance_tag:
        balance = balance_tag.get_text(strip=True).split()[0]
        return balance
    return "0"

def parse_badge(html_text, badge_name):
    soup = BeautifulSoup(html_text, 'html.parser')
    badge_tags = soup.find_all('p', class_=lambda x: x and badge_name.lower() in x.lower())
    return bool(badge_tags)


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
