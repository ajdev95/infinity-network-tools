import requests
from bs4 import BeautifulSoup

url = "https://in8.network/leaderboard"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

users = soup.find_all(class_='user')

print("Leaderboard:")
for i, user in enumerate(users):
    username = user.find(id='user').text.strip()
    coins = user.find(class_='user-coins').text.strip()
    print(f"#{i + 1} {username} - {coins}")
