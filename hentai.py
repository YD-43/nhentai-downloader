from NHentai.nhentai import NHentai
import requests
import os
import time
from PIL import Image
if os.name == 'nt':
    slash = '\\'
elif os.name == 'posix':
    slash = '/'
slace = slice(4)

class Fore:
    RESET = "\033[39m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    LIGHTGRAY_EX = "\033[37m"
    DARKGRAY_EX = "\033[90m"
    LIGHTRED_EX = "\033[91m"
    LIGHTGREEN_EX = "\033[92m"
    LIGHTYELLOW_EX = "\033[93m"
    LIGHTBLUE_EX = "\033[94m"
    LIGHTMAGENTA_EX = "\033[95m"
    LIGHTCYAN_EX = "\033[96m"
    WHITE = "\033[97m"



dur = "sauce"
parent_dir = os.getcwd()
home = os.path.join(parent_dir + slash, dur)
if os.path.exists(home) == False:
    os.mkdir(home)

nhentai = NHentai()
x=input(Fore.CYAN + "\nsix digits: ")
doujin = nhentai.get_doujin(id=x)

souce = os.path.join(home, doujin.id)
if os.path.exists(souce) == False:
    os.mkdir(souce)

print("Downloading " + doujin.title + "...")
start=time.time()
for n in range(doujin.total_pages):
    sitetosee = doujin.images[n]
    r = requests.get(sitetosee)
    dj = (str(souce) + str(slash) + str(int(n) + 1) + '.dltemp')

    with open(dj, "wb") as f:
        f.write(r.content)
        filename=dj.split(".")
        img = Image.open(dj)
        target_name = filename[0] + ".jpg"
        rgb_image = img.convert('RGB')
        rgb_image.save(target_name)
        os.remove(dj)
        print(Fore.YELLOW + "Downloaded page " + str(n+1))
stop=(time.time()-start)
print(Fore.GREEN + "Download Complete! - Download took " + stop.split('.') + " seconds")
