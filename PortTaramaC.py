class porttaramaCUSTOM:
    from colorama import Fore, Style, init, Back
    import socket

    while True :
        try :
            print(Fore.GREEN)
            site = input(Fore.GREEN + "Ip Adresi => ")
            portsayisi = input(Fore.GREEN + "Kaç Port Tarasın [Max : 65535] = >")
            hedef = socket.gethostbyname(site)

            print(Fore.GREEN + "-==#==-" * 5)
            print("")
            print(Fore.GREEN + "Hedef taranıyor => " + hedef)
            print("")
            print(Fore.GREEN + "-==#==-" * 5)

            for port in range(1, portsayisi):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                sonuc = s.connect_ex((hedef, port))
                
                if sonuc == 0:
                    print(Fore.GREEN + "{} Numaralı Port Açık.".format(port))

                else :
                    print(Fore.RED + "Bu Aralıkta Açık Port Bulunamadı...")
                s.close()
                
        except Exception as e:
            print(Fore.RED + "Küçük Sorunlar Yaşandı... Sorununuz => ", e)