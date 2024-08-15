import os
os.system("pip install requests")
os.system("pip install pystyle")
import requests
import threading
from pystyle import *
banner = '''
 ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ ██╗███████╗████████╗ █████╗ ███╗   ██╗
 ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║
 █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝██║███████╗   ██║   ███████║██╔██╗ ██║
 ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗██║╚════██║   ██║   ██╔══██║██║╚██╗██║
 ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║██║███████║   ██║   ██║  ██║██║ ╚████║
 ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝

         ╔══════════════════════════════════════════════╗
         ║               admin panel finder             ║
         ║              coded by qwexsa                 ║
         ║               discord:qawexsa                ║
         ║        For Educational Purposes Only         ║
         ╚══════════════════════════════════════════════╝'''

print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))

print('\033[33;1;4;40m' + "admin panel arama scriptime hoşgeldin dostum" + '\033[0m')
print('\033[337;1;4;40m' + "discord : qawexsa" + '\033[0m')
url = input('\033[36;1;4;40m' + "admin panelini bulmak istediğin sitenin url gir : " + '\033[0m')

def kontrol_yeri_babba(admin_sayfaları):
    for oc in admin_sayfaları:
        if not url.startswith("http"):
            full_url = f"https://{url}/{oc}"
        else:
            full_url = f"{url}/{oc}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print('\033[32;1;4;40m' + f"Giriş başarılı! {full_url}" + '\033[0m')
            with open("başarılı.txt", "a", encoding="utf-8") as f_out:
                f_out.write(full_url + "\n")
        else:
            print('\033[31;1;4;40m' + f"Giriş başarısız! {full_url}" + '\033[0m')

def worker(admin_sayfaları):
    kontrol_yeri_babba(admin_sayfaları)

with open("admin.txt", "r", encoding="utf-8") as f:
    admin_sayfaları = [line.strip() for line in f.readlines()]

num_workers = 7
chunk_size = len(admin_sayfaları) // num_workers
threads = []

for i in range(num_workers):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_workers - 1 else len(admin_sayfaları)
    thread = threading.Thread(target=worker, args=(admin_sayfaları[start:end],))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
