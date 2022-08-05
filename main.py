from colorama import *
import os

os.system("clear")

print(Fore.GREEN + """
╔═══╗        ╔╗ ╔═╗╔═╗                        
║╔═╗║       ╔╝╚╗╚╗╚╝╔╝                        
║╚═╝║╔══╗╔═╗╚╗╔╝ ╚╗╔╝ ╔══╗╔══╗ ╔═╗ ╔═╗ ╔══╗╔═╗
║╔══╝║╔╗║║╔╝ ║║  ╔╝╚╗ ║╔═╝╚ ╗║ ║╔╗╗║╔╗╗║╔╗║║╔╝
║║   ║╚╝║║║  ║╚╗╔╝╔╗╚╗║╚═╗║╚╝╚╗║║║║║║║║║║═╣║║ 
╚╝   ╚══╝╚╝  ╚═╝╚═╝╚═╝╚══╝╚═══╝╚╝╚╝╚╝╚╝╚══╝╚╝ 
                        Version : 0.1
                        By : Nothing.Exe / QızılBash
                        Yardım İçin '-h'
""")
while True:
    portXcanner = input(Fore.GREEN + "PortXcanner => ")

    if portXcanner in ("-f"):
        import PortTaramaF
        continue
    
    if portXcanner in ("-c"):
        import PortTaramaC
        continue

    if portXcanner in ("-clear"):
        os.system('clear')
        continue

    if portXcanner in ("-exit"):
        exit()

    if portXcanner in ("-h"):
        print(Fore.GREEN + """
        -f => Full Tarama Yaparsınız
        -h => Yardım...
        -c => (Custom) Kişiselleştirilmiş Tarama
        -clear => Terminalli Temizler
        -exit => Çıkış
        """)
        continue