import os
from instagram_private_api import Client
import instagram_private_api
import colorama
import getpass
red = colorama.Fore.RED
green = colorama.Fore.GREEN
cv = colorama.Fore.WHITE
os.system("clear")

banner = (red + """




  ____            _            _               _
 / ___|__ _      (_)_ __   ___| |__   ___  ___| | __
| |   / _` |_____| | '_ \ / __| '_ \ / _ \/ __| |/ /
| |__| (_| |_____| | | | | (__| | | |  __/ (__|   <
 \____\__,_|     |_|_| |_|\___|_| |_|\___|\___|_|\_\




""")

print(banner)


try:
    username = input(red + "[?] Entrer votre nom d'utilisateur --> ")
    password = getpass.getpass(red + "[?] Entrer votre  password --> ")
    client = Client(username=username,password=password)
    client.login()
    print(green + "[+]le mot de passe est valide")

except instagram_private_api.errors.ClientLoginError:
    print (red + "[?]le mot de passe est incorrect ou username :) " + cv)
    exit()
