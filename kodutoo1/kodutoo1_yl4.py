taisarvud = [1, 3, 2, 5, 4, 7, 6, 9, 10, 8, 124, 34, 513, 15] #loend numbritega
sorted_taisarvud = sorted(taisarvud) #ülesanne nõudis loendi sorteerimist

def binaar_otsing(loend, otsitav):
    algus_index = 0                #numbrid siin muutuvad niiet hea neid alguses panna.
    list_pikk = len(loend)         #indeksid hakkavad listi tükeldades muutuma
    viimane_index = list_pikk-1
    keskmine_index = (algus_index+viimane_index)//2
    keskmine_number = loend[keskmine_index]
    while True:
        if algus_index == viimane_index:
            if keskmine_number != otsitav: # kohe välistada number kui see ei asu loendis
                return "Ei ole loendis"
        
        elif keskmine_number == otsitav: #ideaalses maailmas kui otsitav on täpselt keskel
            return keskmine_index
        
        elif keskmine_number > otsitav:
            viimane_index = keskmine_index - 1   # essa pool kui nr on keskmisest suurem
            keskmine_index = (algus_index + viimane_index) // 2
            keskmine_number = loend[keskmine_index]
            if keskmine_number == otsitav:
                return keskmine_index
        
        elif keskmine_number < otsitav:
            algus_index = keskmine_index + 1     # teine pool kui nr on keskmisest väiksem
            viimane_index = list_pikk -1
            keskmine_index = (algus_index+viimane_index) // 2
            keskmine_number = loend[keskmine_index]
            if keskmine_number == otsitav:
                return keskmine_index
#print(sorted_taisarvud)
print("Binaarne otsinguprogramm loendist kindla numbri järjendi leidmiseks.")
inputleitav = int(input("Sisesta otsitav arv: "))  #user input et mis numbrit otsib
print("Leiame selle numbri indeksi teie jaoks...")
print(binaar_otsing(sorted_taisarvud, inputleitav)) #output print
            