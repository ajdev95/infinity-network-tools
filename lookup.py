import requests
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

            print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTGREEN_EX}<+>{Fore.RESET} {Fore.RESET}{Fore.LIGHTWHITE_EX}User's info:{Fore.RESET} {Fore.LIGHTBLACK_EX}username={Fore.RESET}{Fore.LIGHTWHITE_EX}{username}{Fore.LIGHTBLACK_EX} coins={Fore.RESET}{Fore.LIGHTWHITE_EX}{balance} coins {Fore.LIGHTCYAN_EX}||{Fore.RESET} {Fore.LIGHTBLACK_EX}infinity_founder={Fore.RESET}{str(has_infinity_founder).lower()} {Fore.LIGHTBLACK_EX}staff={Fore.RESET}{str(has_staff).lower()} {Fore.LIGHTBLACK_EX}developer={Fore.RESET}{str(has_developer).lower()} {Fore.LIGHTBLACK_EX}bug_hunter={Fore.RESET}{str(has_bug_hunter).lower()} {Fore.LIGHTBLACK_EX}premium={Fore.RESET}{str(has_premium).lower()}")
        else:
            print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTGREEN_EX}<+>{Fore.RESET} {Fore.RESET} User is not token, meaning I don't have information on it! {Fore.LIGHTBLACK_EX}username={Fore.RESET}{username}")
    except requests.RequestException as e:
        print(f"Error checking the username {Fore.LIGHTBLACK_EX}username={Fore.RESET}{Fore.LIGHTWHITE_EX}{username}{Fore.RESET} {Fore.LIGHTBLACK_EX}error={Fore.RESET}{Fore.LIGHTWHITE_EX}{e}{Fore.RESET}")

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


def check(username):
    try:
        print(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTBLUE_EX}<+>{Fore.RESET} {Fore.RESET}Checking the user {Fore.LIGHTBLACK_EX}username={Fore.RESET}{Fore.LIGHTWHITE_EX}{username}{Fore.RESET} please wait..")
        check_user_profile(username)
    except Exception as e:
        print(f"{Fore.RED}{Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

username = input(f"{Fore.LIGHTBLACK_EX}{current_time}{Fore.RESET} {Fore.LIGHTYELLOW_EX}<+>{Fore.RESET} {Fore.LIGHTMAGENTA_EX}Enter the username you want to lookup: ")

check(username)
