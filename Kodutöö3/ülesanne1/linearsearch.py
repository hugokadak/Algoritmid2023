num_arr = [1, 2, 3, 5, 7, 12, 19, 31, 50, 81, 131, 212]

def num_find(array, num):
    a = "no" #saata kui ei ole
    b = len(array)
    for i in range(b):
        if array[i] == num: #for tsükkel teeb kõik ära
            a = "array index: " + str(i) + ", what does it mean?"
    return a #sneaky muutuja vahetus
leitav = int(input("Sisesta leitav Fibonacci number: "))
print(num_find(num_arr, leitav))
