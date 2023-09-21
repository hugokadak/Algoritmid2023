
def fibo_seq(n):
    if n <= 1:
        return n # 0 ja 1 korral pole eriti muud kui saata 0 ja 1 tagasi
    else:
        return fibo_seq(n-1) + fibo_seq(n-2) # ühest suurem number tagastab endast kahe väiksema arvu summa
    
nums = int(input("Sisesta Fibonacci numbrite kogus: ")) #saab ise valida palju numbreid

if nums < 0:
    print("Error: ei tohi olla negatiivne") #neg fibo ei saa
else:
    print("Fibonacci numbrijada pikkusega", nums)
    for i in range(nums): #kordab func nums korda
        print(fibo_seq(i)) #fibo_seq func et fibonacci numbreid saada
