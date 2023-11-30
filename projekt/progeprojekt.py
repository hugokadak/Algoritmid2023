import sys
from heapq import heapify, heappush, heappop
from tkinter import *
from tkinter import ttk


aken = Tk()
aken.title("LÜHIMATEEOTSIJA")
frm = ttk.Frame(aken, padding=10)
frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=aken.destroy).grid(column=1, row=0)

def show(): 
    label.config( text = clicked.get() )

options = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 

clicked1 = StringVar()
clicked1.set("Vali Algus koht")

clicked2 = StringVar()
clicked2.set("Vali Lõpp koht")

drop1 = OptionMenu( aken , clicked1 , *options ).grid(column=1,row=0) 
drop2 = OptionMenu( aken , clicked2 , *options ).grid(column=1,row=1) 


button1 = Button( aken , text = "VALI" , command = show ).grid(column=2,row=0)
button2 = Button( aken , text = "VALI" , command = show ).grid(column=2,row=1)
label = Label( aken , text = " " )
 
def dijkstra(graph, src, dest):
    inf = sys.maxsize
    node_data = {'Kuressaare':{'cost':inf, 'pred':[]},
                 'Haapsalu':{'cost':inf, 'pred':[]},
                 'Keila':{'cost':inf, 'pred':[]},
                 'Tallinn':{'cost':inf, 'pred':[]},
                 'Rapla':{'cost':inf, 'pred':[]},
                 'Pärnu':{'cost':inf, 'pred':[]},
                 'Valga':{'cost':inf, 'pred':[]},
                 'Viljandi':{'cost':inf, 'pred':[]},
                 'Paide':{'cost':inf, 'pred':[]},
                 'Tapa':{'cost':inf, 'pred':[]},
                 'Rakvere':{'cost':inf, 'pred':[]},
                 'Jõhvi':{'cost':inf, 'pred':[]},
                 'Tartu':{'cost':inf, 'pred':[]},
                 'Otepää':{'cost':inf, 'pred':[]},
                 'Võru':{'cost':inf, 'pred':[]},
                 'Narva':{'cost':inf, 'pred':[]}
                 }
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(8):
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]
                if cost < node_data[j]['cost']:
                    node_data[j]['cost'] = cost
                    node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                heappush(min_heap,(node_data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("lühim maa: " + str(node_data[dest]['cost']))
    print("lühim tee: " + str(node_data[dest]['pred'] + list(dest)))
    
if __name__ == "__main__":
    graph = {
        'Kuressaare':{'Pärnu': 154, 'Haapsalu': 157},
        'Haapsalu':{'Kuresaare': 157, 'Keila': 76, 'Rapla': 90},
        'Keila':{'Haapsalu': 76, 'Tallinn': 28},
        'Tallinn':{'Keila': 28, 'Pärnu': 127, 'Viljandi': 153, 'Rapla': 54, 'Tartu': 181,'Rakvere':100},
        'Rapla':{'Tallinn': 54, 'Haapsalu': 90, 'Paide': 59},
        'Pärnu':{'Tallinn': 127, 'Kuressaare': 154, 'Valga': 140, 'Viljandi': 92},
        'Valga':{'Pärnu': 140, 'Viljandi': 80, 'Tartu': 85, 'Otepää': 48, 'Võru': 70},
        'Viljandi':{'Valga': 80, 'Pärnu': 92, 'Tallinn': 153, 'Paide': 70, 'Tartu': 78},
        'Paide':{'Rapla': 59, 'Viljandi': 70, 'Tapa': 55, 'Tartu': 103},
        'Tapa':{'Paide': 55, 'Rakvere': 31,'Tartu': 126},
        'Rakevere':{'Jõhvi': 72, 'Tapa': 31, 'Tallinn': 100},
        'Jõhvi':{'Rakvere': 72, 'Tartu': 129, 'Narva': 50},
        'Narva':{'Jõhvi': 50},
        'Tartu':{'Jõhvi': 129, 'Viljandi': 78, 'Tallinn': 181, 'Tapa': 126, 'Valga': 85, 'Paide': 103, 'Otepää': 43, 'Võru': 71},
        'Otepää':{'Võru': 43, 'Tartu': 43, 'Valga': 48},
        'Võru':{'Tartu': 71, 'Valga': 70, 'Otepää': 43},
        }
    source = 'Kuressaare'
    destination = 'Võru'
    dijkstra(graph,source,destination)
aken.mainloop()