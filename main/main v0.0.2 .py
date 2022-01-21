from inspect import ismemberdescriptor
import random
import time
from evk import *

savefile= open('savegame.txt','r')
kullaniciadi=savefile.readline()
para=savefile.readline()
para=para.split("=")
kullaniciadi=kullaniciadi.split("=")

kullaniciadi=kullaniciadi[1]
para=int(para[1])

if kullaniciadi=="Baslangic":
    kullaniciadi=input("Kullanici ismi giriniz:\n")



def savas():
    global para
    saldırgan=random.randint(0,1)
    if saldırgan==0:
        saldırgan=insan()
    else:
        saldırgan=canavar()
    a=1
    print("Savaş alanı içindesiniz\n")
    while a==1:
        print(f"{saldırgan.isim} size saldırıyor.\nHasar: {saldırgan.hasar}/Can: {saldırgan.can}\n")
        hasar=saldırı()
        saldırgan.can-=hasar
        player.can-=saldırgan.hasar
        time.sleep(1)
        if saldırgan.can<=0:
            ödeme=random.randint(0,300)
            para+=ödeme
            print(f"Saldırgan öldü. {ödeme} altın düşürdü")
            a=0
        if player.can==0:
            print("Öldünüz")
            slot1=el()
            slot2=el()
            para=1000
            a=0
        
        
player=oyuncu()
slot1=el()
slot2=el()
envaterslot1=boşslot()
envaterslot2=boşslot()
envaterslot3=boşslot()
envaterslot4=boşslot()
büyüslot=saldırıbüyüsü()



yapılabilecekler=["Savaş", "Silahmarket", ]

def silahmarket():
    global para
    global slot1
    global slot2
    user_input=input(f"Hangi slotunuzu değiştireceksiniz (1 {slot1.isim}/2 {slot2.isim})")
    if user_input=="1":
        print(f"Markete hoşgeldiniz. elimizde \n1 {tabanca.isim}/{tabanca.fiyat} altın\n2 {tüfek.isim}/{tüfek.fiyat} altın\n3 {uzi.isim}/{uzi.fiyat} altın\n4 {çakı.isim}/{çakı.fiyat} altın\n5 {bıçak.isim}/{bıçak.fiyat} altın")
        user_input=input()
        if user_input=="1":
            if slot1.fiyat+para>=tabanca.fiyat:
                para-=tabanca.fiyat-(slot1.fiyat)
                slot1=tabanca()
            else:
                print("Paranız yetersiz")
        elif user_input=="2":
            if slot1.fiyat+para>=tüfek.fiyat:
                para-=tabanca.fiyat-(slot1.fiyat)
                slot1=tüfek()
            else: 
                print("Paranız yetersiz")
        elif user_input=="3":
            if slot1.fiyat+para>=uzi.fiyat:
                para-=uzi.fiyat-(slot1.fiyat)
                slot1=uzi()
            else:
                print("Paranız yetersiz")
        elif user_input=="4":
            if slot1.fiyat+para>=çakı.fiyat:
                para-=çakı.fiyat-(slot1.fiyat)
                slot1=çakı()
            else:
                print("Paranız yetersiz")
        elif user_input=="5":
            if slot1.fiyat+para>=bıçak.fiyat:
                para-=bıçak.fiyat-(slot1.fiyat)
                slot1=bıçak()
            else:
                print("Paranız yetersiz")
        else:
            print("Böyle bir silah yok yada kullanmanıza izin verilmiyor")
    elif user_input=="2":
        print(f"Markete hoşgeldiniz. elimizde \n1 {tabanca.isim}/{tabanca.fiyat} altın\n2 {tüfek.isim}/{tüfek.fiyat} altın\n3 {uzi.isim}/{uzi.fiyat} altın\n4 {çakı.isim}/{çakı.fiyat} altın\n5 {bıçak.isim}/{bıçak.fiyat} altın")
        user_input=input()
        if user_input=="1":
            if slot2.fiyat+para>=tabanca.fiyat:
                para-=tabanca.fiyat-(slot2.fiyat)
                slot2=tabanca()
            else:
                print("Paranız yetersiz")
        elif user_input=="2":
            if slot2.fiyat+para>=tüfek.fiyat:
                para-=tabanca.fiyat-(slot2.fiyat)
                slot2=tüfek()
            else: 
                print("Paranız yetersiz")
        elif user_input=="3":
            if slot2.fiyat+para>=uzi.fiyat:
                para-=uzi.fiyat-(slot2.fiyat)
                slot2=uzi()
            else:
                print("Paranız yetersiz")
        elif user_input=="4":
            if slot2.fiyat+para>=çakı.fiyat:
                para-=çakı.fiyat-(slot2.fiyat)
                slot2=çakı()
            else:
                print("Paranız yetersiz")
        elif user_input=="5":
            if slot2.fiyat+para>=bıçak.fiyat:
                para-=bıçak.fiyat-(slot2.fiyat)
                slot2=bıçak()
            else:
                print("Paranız yetersiz")        

def iksirmarket():
    global envaterslot1,envaterslot2,envaterslot3,envaterslot4
    user_input=input(f"Hangi slota iksir alacaksınız\nslot1: {envaterslot1.isim}/slot2: {envaterslot2.isim}\nslot3: {envaterslot3.isim}/slot4: {envaterslot4.isim}")
    if user_input=="slot1":
        user_input=input(f"{kcan.isim}/{kcan.fiyat} altın - {ocan.isim}/{ocan.fiyat} altın - {bcan.isim}/{bcan.fiyat} altın")
        if user_input==kcan.isim:
            envaterslot1=kcan()
        elif user_input==ocan.isim:
            envaterslot1=ocan()
        elif user_input==bcan.isim:
            envaterslot1=bcan()
    elif user_input=="slot2":
        user_input=input(f"{kcan.isim}/{kcan.fiyat} altın - {ocan.isim}/{ocan.fiyat} altın - {bcan.isim}/{bcan.fiyat} altın")
        if user_input==kcan.isim:
            envaterslot2=kcan()
        elif user_input==ocan.isim:
            envaterslot2=ocan()
        elif user_input==bcan.isim:
            envaterslot2=bcan()
    elif user_input=="slot3":
        user_input=input(f"{kcan.isim}/{kcan.fiyat} altın - {ocan.isim}/{ocan.fiyat} altın - {bcan.isim}/{bcan.fiyat} altın")
        if user_input==kcan.isim:
            envaterslot3=kcan()
        elif user_input==ocan.isim:
            envaterslot3=ocan()
        elif user_input==bcan.isim:
            envaterslot3=bcan()
    elif user_input=="slot4":
        user_input=input(f"{kcan.isim}/{kcan.fiyat} altın - {ocan.isim}/{ocan.fiyat} altın - {bcan.isim}/{bcan.fiyat} altın")
        if user_input==kcan.isim:
            envaterslot4=kcan()
        elif user_input==ocan.isim:
            envaterslot4=ocan()
        elif user_input==bcan.isim:
            envaterslot4=bcan()

def iksirkullanma():
    user_input=input("")

def saldırı():
    hasar=0 
    user_input=input(f"hangisi ile saldıracaksınız?\n{slot1.isim}\n{slot2.isim}\n")
    
    
    if user_input=="el":
        if slot1.isim=="el" or slot2.isim=="el":
            user_input=input("Yapabileceğiniz saldırılar. 'yumruk, tokat'\n")
            if user_input=="yumruk":
                hasar=el.hasar*2
            elif user_input=="tokat":
                hasar=el.hasar*1
        else:
            print("Bu silaha sahip değilsiniz")
            saldırı()


    elif user_input=="tabanca":
        if slot1.isim=="tabanca" or slot2.isim=="tabanca":
            if slot1.isim=="tabanca":
                user_input=input("Yapabileceğiniz saldırılar. 'tekli atış, üçlü atış, reload'\n")
                if user_input=="tekli atış":
                    slot1.jarjör-=1
                    if tabanca.isabet>random.randint(0,100):
                        if tabanca.kritiksans>random.random():
                            hasar=tabanca.hasar*tabanca.kritiksans
                        else:
                            hasar=tabanca.hasar
                    else:
                        print("Merminiz isabet etmedi")
                elif user_input("üçlü atış"):
                    hasar=0
                    for i in range(0,3):
                        slot1.jarjör-=1
                        if tabanca.isabet-i*5>random.randint(0,100):
                            if tabanca.kritiksans>random.random():
                                hasar+=slot1.hasar*tabanca.kritiksans
                            else:
                                hasar=slot1.hasar
                        else:
                            hasar=0
                            print("Iskaladınız")
                elif user_input=="reload":
                    slot1.jarjör=tabanca.jarjör

            else:
                user_input=input("Yapabileceğiniz saldırılar. 'tekli atış, üçlü atış, reload'\n")
                if user_input=="tekli atış":
                    slot2.jarjör-=1
                    if tabanca.isabet>random.randint(0,100):
                        if tabanca.kritiksans>random.random():
                            hasar=slot1.hasar*tabanca.kritiksans
                        else:
                            hasar=slot1.hasar
                    else:
                        print("Merminiz isabet etmedi")
                elif user_input("üçlü atış"):
                    for i in range(0,3):
                        slot2.jarjör-=1
                        if tabanca.isabet-i*5>random.randint(0,100):
                            if tabanca.kritiksans>random.random():
                                hasar+=tabanca.hasar*tabanca.kritiksans
                            else:
                                hasar=tabanca.hasar
                        else:
                            hasar=0
                            print("Iskaladınız")
                elif user_input=="reload":
                    slot2.jarjör=tabanca.jarjör

        else:
            print("Bu silaha sahip değilsiniz!")
            saldırı()
    
    
    elif user_input=="tüfek":
        if slot1.isim=="tüfek" or slot2.isim=="tüfek":
            if slot1.isim=="tüfek":
                user_input==input("Yapabileceğiniz saldırılar. 'tekli atış, çift atış, reload'\n")
                if user_input=="tekli atış":
                    if slot1.jarjör>=1:
                        slot1.jarjör-=1
                        if tüfek.isabet>random.randint(0,100):
                            if tüfek.kritiksans>random.random():
                                hasar=tüfek.kritikartis*slot1.hasar
                            else:
                                hasar=slot1.hasar
                        else:
                            print("Iska!")
                    else:
                        print("Jarjörünüzde yeterince mermi yok")
                        savas()
                elif user_input=="çift atış":
                    if slot1.jarjör>=2:
                        for i in range(0,1):
                            slot1.jarjör-=1
                            if tüfek.isabet-i*10>random.randint(0,100):
                                if tüfek.kritiksans>random.random():
                                    hasar=tüfek.kritikartis*slot1.hasar
                                else:
                                    hasar=slot1.hasar
                            else:
                                print("Iska!")
                    else:
                        print("Merminiz yetersiz")
                elif user_input=="reload":
                    slot1.jarjör=tüfek.jarjör
            else:
                user_input==input("Yapabileceğiniz saldırılar. 'tekli atış, çift atış, reload'\n")
                if user_input=="tekli atış":
                    if slot2.jarjör>=1:
                        slot2.jarjör-=1
                        if tüfek.isabet>random.randint(0,100):
                            if tüfek.kritiksans>random.random():
                                hasar=tüfek.kritikartis*slot2.hasar
                            else:
                                hasar=slot2.hasar
                        else:
                            print("Iska!")
                    else:
                        print("Jarjörünüzde yeterince mermi yok")
                        savas()
                elif user_input=="çift atış":
                    if slot2.jarjör>=2:
                        for i in range(0,1):
                            slot2.jarjör-=1
                            if tüfek.isabet-i*10>random.randint(0,100):
                                if tüfek.kritiksans>random.random():
                                    hasar+=tüfek.kritikartis*slot1.hasar
                                else:
                                    hasar+=slot2.hasar
                            else:
                                print("Iska!")
                    else:
                        print("Merminiz yetersiz")
                elif user_input=="reload":
                    slot1.jarjör=tüfek.jarjör
        else:
            print("Bu silah sizde bulunmuyor")  


    elif user_input=="uzi":
        if slot1.isim=="uzi" or slot2.isim=="uzi":
            if slot1.isim=="uzi":
                user_input==input("Yapabileceğiniz saldırılar 'tekli atış, beşli atış, şarjörü boşalt, reload'\n")
                if user_input=="tekli atış":
                    if slot1.jarjör>=1:
                        slot1.jarjör-=1
                        if uzi.isabet>random.randint(0,100):
                            if uzi.kritiksans>random.random():
                                hasar=slot1.hasar*uzi.kritikartis
                            else:
                                hasar=slot1.hasar
                        else:
                            print("Iska!")
                    else:
                        print("Merminiz yetersiz")
                elif user_input=="beşli atış":
                    if slot1.jarjör>=5:
                        for i in range(0,4):
                            slot1.jarjör-=1
                            if uzi.isabet-i*5>random.randint(0,100):
                                if uzi.kritiksans-i*0.05>random.random():
                                    hasar+=slot1.hasar*uzi.kritikartis
                                else:
                                    hasar+=slot1.hasar
                            else:
                                print("Iska!")
                    else:
                        print("Merminiz yetersiz")
                elif user_input=="şarjörü boşalt":
                    for i in range(0,slot1.jarjör):
                        slot1.jarjör-=1
                        if i<=10:
                            if uzi.isabet-i*random.randint(0,5)/2>random.randint(0,100):
                                hasar+=slot1.hasar
                            else:
                                hasar+=0
                        else:
                            if uzi.isabet-25>random.randint(0,100):
                                hasar+=slot1.hasar
                            else:
                                hasar+=0
                elif user_input=="reload":
                    slot1.jarjör=uzi.jarjör
            elif slot2.isim=="uzi":
                user_input==input("Yapabileceğiniz saldırılar 'tekli atış, beşli atış, şarjörü boşalt, reload'\n")
                if user_input=="tekli atış":
                    if slot2.jarjör>=1:
                        slot2.jarjör-=1
                        if uzi.isabet>random.randint(0,100):
                            if uzi.kritiksans>random.random():
                                hasar=slot2.hasar*uzi.kritikartis
                            else:
                                hasar=slot2.hasar
                        else:
                            print("Iska!")
                    else:
                        print("Merminiz yetersiz")
                elif user_input=="beşli atış":
                    if slot2.jarjör>=5:
                        for i in range(0,4):
                            slot2.jarjör-=1
                            if uzi.isabet-i*5>random.randint(0,100):
                                if uzi.kritiksans-i*0.05>random.random():
                                    hasar+=slot2.hasar*uzi.kritikartis
                                else:
                                    hasar+=slot2.hasar
                            else:
                                print("Iska!")
                    else:
                        print("Merminiz yetersiz")
                elif user_input=="şarjörü boşalt":
                    for i in range(0,slot2.jarjör):
                        slot2.jarjör-=1
                        if i<=10:
                            if uzi.isabet-i*random.randint(0,5)/2>random.randint(0,100):
                                hasar+=slot2.hasar
                            else:
                                hasar+=0
                        else:
                            if uzi.isabet-25>random.randint(0,100):
                                hasar+=slot2.hasar
                            else:
                                hasar+=0
                                print("Iska!")
                elif user_input=="reload":
                    slot2.jarjör=uzi.jarjör                    
        else:
            print("Bu silah sizde bulunmuyor")
            saldırı()                
    
    
    elif user_input=="çakı":
        if slot1.isim=="çakı" or slot2.hasar=="çakı":
            if slot1.isim=="çakı":
                user_input=input("Yapabileceğiniz saldırılar.'sapla, salla'\n")
                if user_input=="sapla":
                    hasar=slot1.hasar
                elif user_input=="salla":
                    hasar=slot1.hasar
            elif slot2.isim=="çakı":
                user_input=input("Yapabileceğiniz saldırılar.'sapla, salla'\n")
                if user_input=="sapla":          
                    hasar=slot1.hasar
                elif user_input=="salla":
                    hasar=slot1.hasar
        else:
            print("Bu silah sizde bulunmuyor")
            saldırı()
                
         
    elif user_input=="bıçak":
        if slot1.isim=="bıçak" or slot2.isim=="bıçak":
            if slot1.isim=="bıçak":
                user_input=input("Yapabileceğiniz saldırılar. 'sapla, salla'\n")
                if user_input=="sapla":
                    hasar=slot1.hasar
                elif user_input=="salla":
                    hasar=slot1.hasar
            elif slot2.isim=="bıçak":
                user_input=input("Yapabileceğiniz saldırılar. 'sapla, salla'\n")
                if user_input=="sapla":
                    hasar=slot2.hasar
                elif user_input=="salla":
                    hasar=slot2.hasar
        else:
            print("Bu silah sizde bulunmuyor")
            saldırı()


    elif user_input=="Batydar's sword":
        if slot1.isim=="Batydar's sword":
            hasar=slot1.hasar

    
    elif user_input=="Klavye":
        if slot2.isim=="Klavye":
            print("Bu silah kullanılmıyor")


    else:
        print("Böyle bir silah yok")
        saldırı()


    return hasar

def envater():
    print(f"{slot1.isim}/hasar {slot1.hasar}, {slot2.isim}/hasar {slot2.hasar}\n ")



oyunaçık=1

while oyunaçık==1:
    user_input=input('Oyundan çıkmak için "cıkıs" yazınız. Savaşmak için "savas" yazınız. Silah marketine gitmek için "silah market" yazınız. Paranızı görmek için "para" yazınız. Envaterinizi görmek için "envater" yazınız\nCan doldurmak için "can doldur" yazınız. İksir almak için "iksir market" yazınız.\n')
    if user_input=="cıkıs":
        oyunaçık=0
        para=para+slot1.fiyat+slot2.fiyat
        savefile= open('savegame.txt','w')
        savefile.write(f"kullaniciadi={kullaniciadi}")
        savefile.write(f"para={para}")
        savefile.close()
    if user_input=="savas":
        savas()
    if user_input=="silah market":
        silahmarket()
    if user_input=="para":
        print(f"Paranız: {para} altın")
    if user_input=="envater":
        envater()
    if user_input=="BW":
        slot1=op.bsword()
    if user_input=="can doldur":
        player.can=100