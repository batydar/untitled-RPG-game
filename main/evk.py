#Ateşli silahlar
class tabanca():
    isim="Tabanca"
    hasar=15
    jarjör=12
    isabet=77
    beklemesüresi=1 #tur
    kritiksans=0.30
    kritikartis=1.5
    fiyat=200 #altın

class tüfek():
    isim="Tüfek"
    hasar=50
    jarjör=7
    isabet=80
    beklemesüresi=5 #tur
    kritiksans=0.44
    kritikartis=3.0
    fiyat=800 #altın

class uzi():
    isim="Uzi"
    hasar=10
    jarjör=30
    isabet=30
    beklemesüresi=3 #tur
    kritiksans=0.11
    kritikartis=1.3
    fiyat=1300 #altın

#mesafeli silahlar
class çakı():
    isim="Çakı"
    jarjör=-1
    hasar=5
    atıs=1
    beklemesuresi=0 #tur
    kritiksans=0
    fiyat=30 #altın

class bıçak():
    isim="Bıçak"
    jarjör=-1
    hasar=10
    atıs=1
    beklemesuresi=0 #tur
    kritiksans=0.3
    kritikartis=2
    fiyat=200 #altın    

class el():
    isim="El"
    hasar=3
    jarjör=-1
    atıs=1
    beklemesuresi=0
    kritiksans=0
    kritikartis=2
    fiyat=0

class op():
    class bsword():
        isim="Batydar's sword"
        hasar=999999999999999
        beklemesüresi=0
        kritiksans=1
        kritikartis=1
        fiyat=9999999999999

    class klavye():
        isim="Klavye"
        beklemesüresi=100
        fiyat=10000 #altın


#karakterler
class oyuncu():
    can=100
    hasar=0

class insan():
    isim="insan"
    can=100
    hasar=tabanca.hasar

class canavar():
    isim="canavar"
    can=250
    hasar=40

class ilkboss():
    isim="boss"
    can=1000
    hasar=30

#zırhlar

class seviye1zırh():
    zırh=10

class seviye2zırh():
    zırh=20
    hasar=10

class seviye3zırh():
    zırh=40
    hasar=20

class seviye4zırh():
    zırh=50
    hasar=25    


#iksirler

class canbüyüsü():
    isim="canbüyüsü"
    candoldurma=10

class savunmabüyüsü():
    isim="savunmabüyüsü"
    ekcan=30

class saldırıbüyüsü():
    isim="saldırı büyüsü"
    hasar=20

class boşslot():
    isim="boş slot"
    candoldurma=0
    canek=0

class kcan():
    isim="küçük can"
    candoldurma=25
    canek=5
    fiyat=80

class ocan():
    isim="orta can"
    candoldurma=60
    canek=20
    fiyat=300

class bcan():
    isim="büyük can"
    candoldurma=100
    canek=50
    fiyat=800