num_arr = [1, 2, 3, 5, 7, 12, 19, 31, 50, 81, 131, 212]

def binary_search(array, algind, viimind, num):
    kesk = (algind + viimind) // 2 #keskmine täisarv
    #print(str(kesk))
    if algind <= viimind:
        if array[kesk] == num: #äkki joppab keskmisega
            return kesk
        elif array[kesk] > num: #num suurem, esimene pool
            return binary_search(array, algind, kesk-1, num)
        else: #siis on num väiksem
            return binary_search(array, kesk+1, viimind, num)
        return num #func ei ole funky
    else:
        b = "no"
        return b
#kasutaja mõelda
leitav = int(input("Sisesta leitav: ")) #mis arvu otsite?
index = binary_search(num_arr, 0, len(num_arr), leitav)
#tahtsin puudumise korral et output tuleks
if index == "no":
    print("no")
else:
    print("Number peitis ennast", str(index), "kohas.")