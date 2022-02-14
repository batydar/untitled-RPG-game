
import random
import time

from evk import *

enerji=20





def savas():
    global para, slot1, slot2, mana, player, betki, aetki
    saldırgan=random.randint(0,1)
    if saldırgan==0:
        saldırgan=insan()
    else:
        saldırgan=canavar()
    a=1
    print("Savaş alanı içindesiniz\n")
    while a==1:
        print(f"{saldırgan.isim} size saldırıyor.\nHasar: {saldırgan.hasar}/Can: {saldırgan.can}\n")
        print(f"{player.can} canınız kaldı")
        time.sleep(1)
        hasar=saldırı()+etkiler()
        saldırgan.can-=hasar
        player.can-=saldırgan.hasar
        if "E"==input("İksir kullanacak mısınız?(E/h)"):
            iksirkullanma()
        if "E"==input("Büyü kullanacak mısınız(E/h)"):
            if büyüslot.isim==canbüyüsü.isim:
                if player.can+büyüslot.candoldurma>100:
                    player.can=100
                    mana-=2
            
            if büyüslot.isim==savunmabüyüsü.isim:
                player.can+=büyüslot.ekcan

            if büyüslot.isim==saldırıbüyüsü.isim:
                saldırgan.can-=büyüslot.hasar

        else:
            if mana+1>player.maxmana:
                mana+=0
            else:
                mana+=1
            
        time.sleep(1)        
        if saldırgan.can<=0:
            ödeme=random.randint(0,300)
            para+=ödeme
            print(f"Saldırgan öldü. {ödeme} altın düşürdü")
            a=0
        if player.can<=0:
            a=0
        
        
yapılabilecekler=["Savaş", "Silahmarket", ]

def loadfile():
    savefile= open('savegame.txt','r')
    kullaniciadi=savefile.readline()
    para=savefile.readline()
    enerji=savefile.readline()
    hikaye=savefile.readline()
    para=para.split("=")
    kullaniciadi=kullaniciadi.split("=")
    enerji=enerji.split("=")
    hikaye=hikaye.split("=")

    kullaniciadi=kullaniciadi[1]
    para=int(para[1])
    enerji=int(enerji[1])
    hikaye=int(hikaye[1])

    if kullaniciadi=="Baslangic":
        kullaniciadi=input("Kullanici ismi giriniz:\n")
    return enerji,kullaniciadi,para,hikaye

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
                para-=tüfek.fiyat-(slot1.fiyat)
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
    global player,envaterslot1,envaterslot2,envaterslot3,envaterslot4
    user_input=input("Hangi iksiri kullanacaksınız?\n1 {envaterslot1.isim}/2 {envaterslot2.isim}\n3 {envaterslot3.isim}/4 {envaterslot4.isim}")
    if user_input=="1":
        print(f"{envaterslot1.isim}'i kullandınız")
        if envaterslot1.candoldurma+player.can>=100:
            player.can=100+envaterslot1.canek
        else:
            player.can+envaterslot1.candoldurma+envaterslot1.canek
        envaterslot1=boşslot()
    if user_input=="2":
        print(f"{envaterslot2.isim}'i kullandınız")
        if envaterslot2.candoldurma+player.can>=100:
            player.can=100+envaterslot2.canek
        else:
            player.can+envaterslot2.candoldurma+envaterslot2.canek
        envaterslot2=boşslot()
    if user_input=="3":
        print(f"{envaterslot3.isim}'i kullandınız")
        if envaterslot3.candoldurma+player.can>=100:
            player.can=100+envaterslot3.canek
        else:
            player.can+envaterslot3.candoldurma+envaterslot3.canek
        envaterslot3=boşslot()
    if user_input=="4":
        print(f"{envaterslot4.isim}'i kullandınız")
        if envaterslot4.candoldurma+player.can>=100:
            player.can=100+envaterslot4.canek
        else:
            player.can+envaterslot4.candoldurma+envaterslot4.canek
        envaterslot4=boşslot()        

def saldırı():
    hasar=0 
    user_input=input(f"hangisi ile saldıracaksınız?\n{slot1.isim}\n{slot2.isim}\n")
    global aetki, betki
    
    if user_input=="el":
        if slot1.isim==el.isim or slot2.isim==el.isim:
            user_input=input("Yapabileceğiniz saldırılar. 'yumruk, tokat'\n")
            if user_input=="yumruk":
                hasar=el.hasar*2
            elif user_input=="tokat":
                hasar=el.hasar*1
        else:
            print("Bu silaha sahip değilsiniz")
            saldırı()


    elif user_input=="tabanca":
        if slot1.isim==tabanca.isim or slot2.isim==tabanca.isim:
            if slot1.isim==tabanca.isim:
                user_input=input("Yapabileceğiniz saldırılar. 'tekli atış, üçlü atış, reload'\n")
                if user_input=="tekli atış":
                    slot1.jarjör-=1
                    if tabanca.isabet>random.randint(0,100):
                        if tabanca.kritiksans>random.random():
                            hasar=tabanca.hasar*tabanca.kritiksans
                        else:
                            hasar=tabanca.hasar
                        aetki=1
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
                            aetki=1
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
                        betki=1
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
                            betki=1
                        else:
                            hasar=0
                            print("Iskaladınız")
                elif user_input=="reload":
                    slot2.jarjör=tabanca.jarjör

        else:
            print("Bu silaha sahip değilsiniz!")
            saldırı()
    
    
    elif user_input=="tüfek":
        if slot1.isim==tüfek.isim or slot2.isim==tüfek.isim:
            if slot1.isim==tüfek.isim:
                user_input==input("Yapabileceğiniz saldırılar. 'tekli atış, çift atış, reload'\n")
                if user_input=="tekli atış":
                    if slot1.jarjör>=1:
                        slot1.jarjör-=1
                        if tüfek.isabet>random.randint(0,100):
                            if tüfek.kritiksans>random.random():
                                hasar=tüfek.kritikartis*slot1.hasar
                            else:
                                hasar=slot1.hasar
                            aetki=1
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
                                aetki=1
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
                            betki=1
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
                                betki=1
                            else:
                                print("Iska!")
                    else:
                        print("Merminiz yetersiz")
                elif user_input=="reload":
                    slot1.jarjör=tüfek.jarjör
        else:
            print("Bu silah sizde bulunmuyor")  


    elif user_input==uzi.isim:
        if slot1.isim==uzi.isim or slot2.isim==uzi.isim:
            if slot1.isim==uzi.isim:
                user_input==input("Yapabileceğiniz saldırılar 'tekli atış, beşli atış, şarjörü boşalt, reload'\n")
                if user_input=="tekli atış":
                    if slot1.jarjör>=1:
                        slot1.jarjör-=1
                        if uzi.isabet>random.randint(0,100):
                            if uzi.kritiksans>random.random():
                                hasar=slot1.hasar*uzi.kritikartis
                            else:
                                hasar=slot1.hasar
                            aetki=1
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
                                aetki=1
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
                                aetki=1
                            else:
                                hasar+=0
                        else:
                            if uzi.isabet-25>random.randint(0,100):
                                hasar+=slot1.hasar
                                aetki=1
                            else:
                                hasar+=0
                    aetki=1
                elif user_input=="reload":
                    slot1.jarjör=uzi.jarjör
            elif slot2.isim==uzi.isim:
                user_input==input("Yapabileceğiniz saldırılar 'tekli atış, beşli atış, şarjörü boşalt, reload'\n")
                if user_input=="tekli atış":
                    if slot2.jarjör>=1:
                        slot2.jarjör-=1
                        if uzi.isabet>random.randint(0,100):
                            if uzi.kritiksans>random.random():
                                hasar=slot2.hasar*uzi.kritikartis
                            else:
                                hasar=slot2.hasar
                            betki=1
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
                                betki=1
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
    
    
    elif user_input==çakı.isim:
        if slot1.isim==çakı.isim or slot2.hasar==çakı.isim:
            if slot1.isim==çakı.isim:
                user_input=input("Yapabileceğiniz saldırılar.'sapla, salla'\n")
                if user_input=="sapla":
                    hasar=slot1.hasar
                elif user_input=="salla":
                    hasar=slot1.hasar
                aetki=1
            elif slot2.isim==çakı.isim:
                user_input=input("Yapabileceğiniz saldırılar.'sapla, salla'\n")
                if user_input=="sapla":          
                    hasar=slot1.hasar
                elif user_input=="salla":
                    hasar=slot1.hasar
                betki=1
        else:
            print("Bu silah sizde bulunmuyor")
            saldırı()
                
         
    elif user_input==bıçak.isim:
        if slot1.isim==bıçak.isim or slot2.isim==bıçak.isim:
            if slot1.isim==bıçak.isim:
                user_input=input("Yapabileceğiniz saldırılar. 'sapla, salla'\n")
                if user_input=="sapla":
                    hasar=slot1.hasar
                elif user_input=="salla":
                    hasar=slot1.hasar
                aetki=1
            elif slot2.isim==bıçak.isim:
                user_input=input("Yapabileceğiniz saldırılar. 'sapla, salla'\n")
                if user_input=="sapla":
                    hasar=slot2.hasar
                elif user_input=="salla":
                    hasar=slot2.hasar
                betki=1
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

    if hasar>0:
        etki=1

    return hasar

def envater():
    global slot1, slot2
    print(f"{slot1.isim}: hasar {slot1.hasar}/eşya lvl{slot1.level}/yanma lvl{slot1.yanmalvl}/yara lvl{slot1.yaralvl}/zehir lvl{slot1.zehirlvl}")
    print(f"{slot2.isim}: hasar {slot2.hasar}/eşya lvl{slot2.level}/yanma lvl{slot2.yanmalvl}/yara lvl{slot2.yaralvl}/zehir lvl{slot2.zehirlvl}")    

def uyku():
    global enerji,para
    para-=150
    enerji=10

def çalışma():
    global enerji,para
    enerji-=5
    para+=100

def büyücü():
    global büyüslot
    user_input=input(f"hangi büyüyü öğrenmek istersiniz?\n{canbüyüsü.isim}/1000|{saldırıbüyüsü.isim}/1000|{savunmabüyüsü.isim}/1000")
    if para>=1000:
        if user_input==canbüyüsü.isim:
            büyüslot=canbüyüsü()
        elif user_input==savunmabüyüsü.isim:
            büyüslot=savunmabüyüsü()
        elif user_input==saldırıbüyüsü.isim:
            büyüslot=saldırıbüyüsü()
        else:
            print("böyle bir büyü yok")
    else:
        print("paran yok")

def silahbüyü():
    global para
    user_input=input(f"1/{slot1.isim}|2/{slot2.isim} hangisini büyüleyeceksin\n")
    if user_input=="1":
        user_input=input(f"{slot1.level+1} level için {slot1.fiyat*2} ile yanma|{slot1.fiyat} ile zehir|{slot1.fiyat*3} ile yara\n(yanma,zehir,yara,hepsi)")
        if user_input=="yanma":
            if slot1.yanmalvl<slot1.level:
                if para>=slot1.fiyat*2: 
                    para-=slot1.fiyat*2
                    slot1.yanmalvl+=1
                    slot1.fiyat+=slot1.fiyat*2
                else:
                    print("paranız yetersiz")
            else:
                print("eşya seviyeniz yeterli değil")

        elif user_input=="zehir":
            if slot1.zehirlvl<=slot1.level:
                if para>=slot1.fiyat:
                    para-=slot1.fiyat
                    slot1.zehirlvl+=1
                    slot1.fiyat*=2
                else:
                    print("paranız yetersiz")
            else:
                print("eşya seviyeniz yeterli değil")

        elif user_input=="yara":
            if slot1.yaralvl<=slot1.level:
                if para>=slot1.fiyat*3:
                    para-=slot1.fiyat*3
                    slot1.yaralvl+=1
                    slot1.fiyat*=4
                else:
                    print("paranız yetersiz")
            else:
                print("eşya seviyeniz yeterli değil")

        elif user_input=="hepsi":
            if slot1.level<=slot1.yanmalvl:
                yanmae=0
            else:
                yanmae=1
            if slot1.level<=slot1.zehirlvl:
                zehire=0
            else:
                zehire=1
            if slot1.level<=slot1.yaralvl:
                yarae=0
            else:
                yarae=1
            
            if yarae==1 and yanmae==1 and zehire==0:
                print("coming soon")

    if user_input=="2":
        user_input=input(f"{slot2.level+1} level için {slot2.fiyat*2} ile yanma|{slot2.fiyat} ile zehir|{slot2.fiyat*3} ile yara\n(yanma,zehir,yara,hepsi)")
        if user_input=="yanma":
            if slot2.yanmalvl<slot2.level:
                if para>=slot2.fiyat*2: 
                    para-=slot2.fiyat*2
                    slot2.yanmalvl+=1
                    slot2.fiyat+=slot2.fiyat*2
                else:
                    print("paranız yetersiz")
            else:
                print("eşya seviyeniz yeterli değil")

        elif user_input=="zehir":
            if slot2.zehirlvl<=slot2.level:
                if para>=slot2.fiyat:
                    para-=slot2.fiyat
                    slot2.zehirlvl+=1
                    slot2.fiyat*=2
                else:
                    print("paranız yetersiz")
            else:
                print("eşya seviyeniz yeterli değil")

        elif user_input=="yara":
            if slot2.yaralvl<=slot2.level:
                if para>=slot2.fiyat*3:
                    para-=slot2.fiyat*3
                    slot2.yaralvl+=1
                    slot2.fiyat*=4
                else:
                    print("paranız yetersiz")
            else:
                print("eşya seviyeniz yeterli değil")

def etkiler():
    global aetki, betki
    if aetki==1:
        a=slot1.level
        aetki=0

    if betki==1:
        b=slot2.level
        betki=0

    while a>0:
        hasar=yanma("slot1")+zehir("slot1")+yara("slot1")
        a-=1
    
    while b>0:
        hasar=yanma("slot2")+zehir("slot2")+yara("slot2")
    

    return hasar

def yanma(slot):
    if slot=="slot1":
        hasar=slot1.yanmalvl*2
    elif slot=="slot2":
        hasar=slot2.yanmalvl*2
    return hasar

def zehir(slot):
    if slot=="slot1":
        hasar=slot1.zehirlvl*1
    elif slot=="slot2":
        hasar=slot2.zehirlvl*1
    return hasar

def yara(slot):
    if slot=="slot1":
        hasar=slot1.yaralvl*3
    elif slot=="slot2":
        hasar=slot2.yaralvl*3
    return hasar

def demirci():
    global slot1, slot2, para
    user_input=input(f"Hangi silahınızı yükselteceksiniz(1/{slot1.isim}/{slot1.fiyat*1.3} altın|2/{slot2.isim})/{slot2.fiyat*1.3} altın")
    if user_input=="1":
        if para>=slot1.fiyat*1.3:
            para-=slot1.fiyat*1.3
            slot1.fiyat+=slot1.fiyat*1.3
            slot1.level+=1
            slot1.hasar*=1.5
        else:
            print("Paranız yetersiz")
    
    elif user_input=="2":
        if para>=slot2.fiyat*1.3:
            para-=slot1.fiyat*1.3
            slot2.fiyat+=slot2.fiyat*1.3
            slot2.level+=1
            slot2.hasar*=1.5
        else:
            print("Paranız yetersiz")


oyunaçık=1

player=oyuncu()
slot1=el()
slot2=el()
envaterslot1=boşslot()
envaterslot2=boşslot()
envaterslot3=boşslot()
envaterslot4=boşslot()
büyüslot=boşbüyü()
mana=3

enerji, kullaniciadi, para, hikaye = loadfile()

def filesave(enerji, slot1, slot2, kullaniciadi, para, hikaye):
    para=para+slot1.fiyat+slot2.fiyat
    savefile= open('savegame.txt','w')
    savefile.write(f"kullaniciadi={kullaniciadi}")
    savefile.write(f"para={para}")
    savefile.write(f"enerji={enerji}")
    savefile.write(f"hikaye={hikaye}")
    savefile.close()

while oyunaçık==1:
    print('Oyundan çıkmak için "cıkıs" yazınız. Savaşmak için "savas" yazınız. Silah marketine gitmek için "silah market" yazınız. Paranızı görmek için "para" yazınız. Envaterinizi görmek için "envater" yazınız')
    print('Can doldurmak için "can doldur" yazınız. İksir almak için "iksir market" yazınız. Uyumak için "dinlen" yazınız. Çalışmak için "çalış" yazınız. Silahınıza özellik ekletmek için "silah büyü" yazınız')
    print('Büyü öğrenmek için "büyücü" yazınız. Oyunu kaydetmek için "kaydet" yazınız. Önceki save\'nizi yüklemek için "yükle" yazınız. Silahınızı geliştirmek için "demirci yazınız" ')
    user_input=input("(silah market, iksir market, envater, dinlen, çalış, büyücü, silah büyü, kaydet, yükle, para, cıkıs, demirci)\n")
    if user_input=="cıkıs":
        filesave(enerji, slot1, slot2, kullaniciadi, para)
        oyunaçık=0
    
    if user_input=="yükle":
        enerji, kullaniciadi, para = loadfile()

    if user_input=="kaydet":
        filesave(enerji, slot1, slot2, kullaniciadi, para)
        

    if enerji>0:        
        if user_input=="büyücü":
            büyücü()
        if user_input=="demirci":
            demirci()
        if user_input=="savas":
            savas()
            enerji-=1
        if user_input=="silah büyü":
            silahbüyü()
        if user_input=="iksir market":
            iksirmarket()
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
            enerji-=1
        if user_input=="çalış":
            çalışma()
        if user_input=="dinlen":
            uyku()
    else:
        if user_input=="dinlen":
            uyku()
        else:
            print("Uyuyakaldınız")
            player.can-=35
            enerji+=7

    user_input=user_input.split("/")
    if user_input[0]=="para-ekle":
        para+=int(user_input[1])

    print(f"enerjiniz {enerji}, canınız {player.can}")    
    if player.can<=0:
        print("Öldün")
        slot1=el
        slot2=el
        para=1000
        player.can=100
    
    time.sleep(2)