# meil on olemas andmeid
lifolist = [4,"a",69]
#saab programmi kasutada niikaua kuni listis on andemid
while lifolist != None:
    print("Kas soovite lisada infot - jah , ei")
    xx = input()
    if xx == "jah":
        #lisame listi informatsiooni viimasele kohale
        info = input("sisesta siia infot")
        print(len(lifolist))
        xd = (len(lifolist)-0)
        lifolist.insert(xd,info)
        print(lifolist)
    if xx == "ei":
        print("Kas soovita infot välja võtta? - jah , ei ")
        info2 = input()
        if info2 == "jah":
            #eemaldame viimase elemendi listist
            lifolist = lifolist[:-1]
            print(lifolist)
        if info2 == "ei":
            print("Head päeva jätku!")

            
            


