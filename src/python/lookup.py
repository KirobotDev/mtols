import requests
from colorama import Fore
import os
import time
import platform
import subprocess
from pathlib import Path

def clear() -> str:
    oss = platform.system()

    if oss == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def personal() -> str | int:
    print(f"""{Fore.BLUE}
    ▄▄█▀██▄      ▄▄█▀███▄    ▄▄█▀██▄      ▄▄▄█▀▄▄    ▄▄█▀█▄▄      ▄▄▀▄  ▄▄▄    ▄▄█▀█▄▄      ▄▄█
      ■▀  ▀███   █■▀▀ ▀██▀    ■▀  ▀███   ▄█■▀▀▀███   █■▀  ▀███    .█▀▐█  ▐▌█    ■▀  ▀███    █■▀
    ██▌    ▐▄█▌  █▀▄▄█▄      ██▌    ▐██▌ ▐█▄     ▀▀  ██     ▐■█▌  █▀  ██▌ ▐█▌  █▀     ▐▄█▌  █▀
    ▐▌▀█▄  ▄█▀▀  ▐▌          ▐▌▐█▄  ▄▀▀    ▀▀▀█▄█▄▄  ▐█▌     ▐▀██ ▐▌  ▐▄ █  █  ▐▌  ▀▀█▄▐▐██ ▐▌
    ■   ▀▀▀      ■ ▄▄██▄▄▄   ■  ▀█ ▄▄  ▄▄ ▄▀▄▄  ▄█▀▀  ▀█▄   ▄██▀  ■    ▐▄ █▐▌  ■      ▀  █▌ ■ ▄▄██▄▄▄
    ▀            ▀▀▀  ▀▀▀    ▀    ▀▀■▄ █▀  ▀▀▀▀▀▀        ▀▀▀      ▀     ▀▀▀▀   ▀        ▀▀  ▀▀▀  ▀▀▀
{Fore.WHITE}""")

    nom = input("Met le nom de famille que tu veux rechercher : ")
    prenom = input("Met le prénom que tu veux rechercher : ")
    page = input("Choisis le nombre de page que tu veux recuperer : ")

    r = requests.post("https://api.brixhub.ru/api/v1/search", json={
        "nom_famille": nom,
        "prenom": prenom,
        "per_page": page,
    })

    if r.status_code == 200:
        resp = r.json()
        results = resp["data"]["results"]

        for result in results:
            for key, value in result.items():
                print(f"{key} : {value}")
                time.sleep(1)

def discord() -> int:
    print(f"""{Fore.RED}
      ▄▄█▀█▄▄      ▄▄█▀██▄    ▄▄▄█▀▄▄    ▄▄█▀███▄    ▄▄█▀█▄▄      ▄▄█▀██▄      ▄▄█▀█▄▄
     █■▀  ▀███    █■▀▀ ▀█▀  ▄█■▀▀▀███   █■▀▀ ▀██▀   █■▀  ▀███     ■▀  ▀███    █■▀  ▀███
    █▀     ▐■█▌  █▀        ▐█▄     ▀▀  █▀          ██     ▐■█▌  ██▌    ▐██▌  █▀     ▐■█▌
    ▐▌      ▐▀██ ▐▌          ▀▀▀█▄█▄▄  ▐▌          ▐█▌     ▐▀██ ▐▌▐█▄  ▄▀▀   ▐▌      ▐▀██
    ■      ▄██▀  ■          ▄▀▄▄  ▄█▀▀ ■ ▄▄██▄▄▄    ▀█▄   ▄██▀  ■  ▀█ ▄▄  ▄▄ ■      ▄██▀
    ▀   ▀▀▀      ▀           ▀▀▀▀▀▀    ▀▀▀  ▀▀▀        ▀▀▀      ▀    ▀▀■▄ █▀ ▀   ▀▀▀
            {Fore.WHITE}""")

    discord_id = int(input("Met l'id discord que tu veux rechercher : "))
    page = input("Choisis le nombre de page que tu veux recuperer : ")

    r = requests.post("https://api.brixhub.ru/api/v1/search", json={
        "discord_id": discord_id,
        "per_page": page,
    })

    if r.status_code == 200:
        resp = r.json()
        results = resp["data"]["results"]

        for result in results:
            for key, value in result.items():
                print(f"{key} : {value}")
                time.sleep(1)

def email() -> str | int:
    print(f"""{Fore.YELLOW}
      ▄▄█▀███▄    ▄▄█▄         ▄▄█▀█▄▄      ▄▄█▀██▄    ▄▄█
     █■▀▀ ▀██▀   █■▀▀█▄██▄     ■▀  ▀███    █■▀▀ ▀█▀   █■▀
     █▀▄▄█▄      ██  ▄▀ ▀■█▌  █▀     ▐▄█▌  █▀         █▀
    ▐▌          ▐█      ▐▀█▌ ▐▌  ▀▀█▄▐▐██ ▐▌         ▐▌
    ■ ▄▄██▄▄▄   ■       ██▀  ■      ▀  █▌ ■          ■ ▄▄██▄▄▄
    ▀▀▀  ▀▀▀    ▀      █▀    ▀        ▀▀  ▀          ▀▀▀  ▀▀▀
          {Fore.WHITE}""")

    email = input("Met l'email que tu veux rechercher : ")
    page = input("Choisis le nombre de page que tu veux recuperer : ")


    r = requests.post("https://api.brixhub.ru/api/v1/search", json={
        "email": email,
        "per_page": page,
    })

    if r.status_code == 200:
        resp = r.json()
        results = resp["data"]["results"]

        for result in results:
            for key, value in result.items():
                print(f"{key} : {value}")
                time.sleep(1)

def main():
    choice = input(f"""{Fore.GREEN}
               ▄▄█▀███▄    ▄▄█▌  ▄▄     ▄▄█▀█▄▄      ▄▄█▀██▄    ▄▄█▀███▄    ▄▄█▀███▄
              █■▀▀ ▀██▀    ■▀   ▐██▌   █■▀  ▀███    █■▀▀ ▀█▀   █■▀▀ ▀██▀   █■▀▀ ▀██▀
             █▀          █▀     ▐▄█▌  ██     ▐■█▌  █▀         █▀          █▀▄▄█▄
            ▐▌          ▐▌ ▀▀▀▄▄▐▐██ ▐█▌     ▐▀██ ▐▌         ▐▌          ▐▌
            ■ ▄▄██▄▄▄   ■▌     ▀  █▌  ▀█▄   ▄██▀  ■          ■ ▄▄██▄▄▄   ■ ▄▄██▄▄▄
            ▀▀▀  ▀▀▀     ▀       ▀▀      ▀▀▀      ▀          ▀▀▀  ▀▀▀    ▀▀▀  ▀▀▀
{Fore.WHITE}
          1. Personal       4. Retour

          2. discord

          3. email

          Fais ton choix : """)

    if choice == "1":
        clear()
        personal()

    elif choice == "2":
        clear()
        discord()

    elif choice == "3":
        clear()
        email()

    elif choice == "4":
        clear()

        ROOT = Path(__file__).resolve().parents[2]
        TOOLS = ROOT / "tools.exe"

        subprocess.run([str(TOOLS)])

if __name__ == "__main__":
    while True:
        clear()
        main()
