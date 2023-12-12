import heapq
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

#-------------------------------- algne aken -------------------------------
aken = Tk()
aken.geometry("976x800") #sen selle kaardi suurus
aken.title("LÜHIMA TEE OTSIJA")
frm = ttk.Frame(aken, padding=10)
frm.grid()

# --------------------- background image tkinterile -----------------------

image1 = Image.open("EESTIKARDDD.png")
tkimage = ImageTk.PhotoImage(image1)
panel1 = Label(aken, image=tkimage) #TÖÖÖÖÖÖÖÖÖÖÖTAAAAAAAAAAAAAB
panel1.grid(row=0, column=0, sticky=E)

# --------------------- dropdown menu & button ja tekstid -----------------
#rippmenüü
options = [ "Kuressaare", "Haapsalu", "Keila", "Tallinn",
            "Rapla", "Pärnu", "Valga", "Viljandi",
            "Paide", "Tapa", "Rakvere", "Jõhvi",
            "Narva", "Tartu", "Otepää", "Võru"] 
#stringvar-id
clicked1 = StringVar() #alg linn
clicked1.set("Vali Algus koht")
clicked2 = StringVar() #siht linn
clicked2.set("Vali Lõpp koht")
#dropdownmenu kaks tk
drop1 = OptionMenu( aken , clicked1 , *options )
drop1.grid(column=0,row=1)
drop2 = OptionMenu( aken , clicked2 , *options )
drop2.grid(column=0,row=2)

# ------------------------------- main funktsioon jooksmiseks --------------------------------
#function stringvar-ide muutmiseks ja dijkstra call-imiseks
def show(): #24k karat magic on see funktsioon
    algvarget = clicked1.get() #muidu oleks StringVar mis func dijkstra-le vale
    loppvarget = clicked2.get()
    linn_algsiht = "Leian lühima tee linnast {} linna {}".format(algvarget, loppvarget) #kaunis
    luhim_tee, path = dijkstra(graph, algvarget, loppvarget) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    teekond_label.config(text = linn_algsiht)#viimaks sain
    dikstratee_txt = "Lühim tee linnast {} linna {}: {} km.".format(algvarget, loppvarget, luhim_tee) #viimaks
    dijkstra_tee.config(text = dikstratee_txt) #output muudetav config kaugus km-tes
    failide_nimekiri = laula_mu_pilti('*.png ', path) #avab piltide kausta ja uurib faile
    pildi_lisaja(failide_nimekiri) #pildi lisaja lisab pildid tkinteri imagesse

#põhjas asuvad teksti osad
teekond_label = Label( aken , text ="..." )
teekond_label.grid(column=0,row=4)
dijkstra_tee = Label( aken, text="Vajutades Kinnita proovib Dijkstra algoritm leida lühima tee.")
dijkstra_tee.grid(column=0,row=5)
#nupp
button1 = Button( aken , text = "Kinnita" , command = show )
button1.grid(column=0,row=3)#sama siin

# --------------- dijkstra funktsioon lühima tee leidmiseks ------------------
def dijkstra(graph, algus, sihtlinn):
    linnade_kaugused_alg = {node: float('infinity') for node in graph} #ei ole avastatud? - kaugus inf
    linnade_kaugused_alg[algus] = 0 #esimese linna kaugus 0 ikka
    eelis_jarts = [(0, algus)] #arr lühima tee jaoks
    eelnev = {node: None for node in graph}
    while eelis_jarts: #evil while tsükkel
        hetke_kaal, uuritav_linn = heapq.heappop(eelis_jarts) #heapq ftw
        if hetke_kaal > linnade_kaugused_alg[uuritav_linn]:
            continue #raskeid teid ei taha
        if uuritav_linn == sihtlinn: #pihtas põhjas
            break
        for ymber_linn, teekaugus in graph[uuritav_linn].items(): #less evil for tsükkel
            kaugus = hetke_kaal + teekaugus #kaugused ++++
            if kaugus < linnade_kaugused_alg[ymber_linn]:
                linnade_kaugused_alg[ymber_linn] = kaugus
                eelnev[ymber_linn] = uuritav_linn #update linn järgmiseks
                heapq.heappush(eelis_jarts, (kaugus, ymber_linn)) #puuuuuuuuuuuuuuuuush
    path = [] #teekond
    viimane = sihtlinn
    while viimane is not None: # weak tsükkel
        path.insert(0, viimane) #lisa array-sse (kaugus, linn)
        viimane = eelnev[viimane] # kuniks sihtlinna jõutud
    return linnade_kaugused_alg[sihtlinn], path # viiiimaks

# ----------------------- programmi algandmed jn. -------------------------
#graaf
graph = {
        'Kuressaare':{'Pärnu': 154, 'Haapsalu': 157},
        'Haapsalu':{'Kuressaare': 157, 'Keila': 76, 'Rapla': 90},
        'Keila':{'Haapsalu': 76, 'Tallinn': 28},
        'Tallinn':{'Keila': 28, 'Pärnu': 127, 'Viljandi': 153, 'Rapla': 54, 'Tartu': 181,'Rakvere':100},
        'Rapla':{'Tallinn': 54, 'Haapsalu': 90, 'Paide': 59},
        'Pärnu':{'Tallinn': 127, 'Kuressaare': 154, 'Valga': 140, 'Viljandi': 92},
        'Valga':{'Pärnu': 140, 'Viljandi': 80, 'Tartu': 85, 'Otepää': 48, 'Võru': 70},
        'Viljandi':{'Valga': 80, 'Pärnu': 92, 'Tallinn': 153, 'Paide': 70, 'Tartu': 78},
        'Paide':{'Rapla': 59, 'Viljandi': 70, 'Tapa': 55, 'Tartu': 103},
        'Tapa':{'Paide': 55, 'Rakvere': 31,'Tartu': 126},
        'Rakvere':{'Jõhvi': 72, 'Tapa': 31, 'Tallinn': 100},
        'Jõhvi':{'Rakvere': 72, 'Tartu': 129, 'Narva': 50},
        'Narva':{'Jõhvi': 50},
        'Tartu':{'Jõhvi': 129, 'Viljandi': 78, 'Tallinn': 181, 'Tapa': 126, 'Valga': 85, 'Paide': 103, 'Otepää': 43, 'Võru': 71},
        'Otepää':{'Võru': 43, 'Tartu': 43, 'Valga': 48},
        'Võru':{'Tartu': 71, 'Valga': 70, 'Otepää': 43},
}

#--------------------------------------------------- image adder testrunner ----------------------------------

def laula_mu_pilti(name, dijk_tee): #big bren funktsioon
    failide_loend = [] #blank for files
    for i in range(len(dijk_tee)-1): #path suurus -1, kuna mdu out of range
        linn1 = dijk_tee[i] #linn esimene
        linn2 = dijk_tee[i+1] # linn järgmine
        for root, dir, files in os.walk("./"): #tglt root, dir useless aga need tekivad mdu samasse arraysse
            for filename in files:
                a = filename #big brain moment 2
                b = a.split(".")
                c = b[0].split("-")
                if linn1 in c and linn2 in c: #töötab, leiab ilusti pildid üles
                    failide_loend.append(filename)
    return failide_loend #failid milles on teekonna node-ide pildid

#--------------------------- pildi lisaja tkinteri backgroundile --------------------------

def pildi_lisaja(piltide_kaust):
    pilt1 = Image.open("EESTIKARDDD.png") #bg image
    for file in piltide_kaust:
        teekond1 = Image.open(file)
        pilt1.paste(teekond1, (0,0), teekond1) #lisa iga teekonna foto for tsükliga pildile
    tkpildike = ImageTk.PhotoImage(pilt1) #tee sellest pilt
    paneelmaja = Label(aken, image=tkpildike)
    paneelmaja.grid(row=0,column=0, sticky=E) #lisa tkinterisse
    aken.mainloop()#selleta see hakkab jebima, jätan siia
aken.mainloop()

# ----------------------------------------- timm --------------------------------------------