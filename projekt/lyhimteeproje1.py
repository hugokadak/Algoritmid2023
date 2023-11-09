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
    node_data = {'Tartu':{'cost':inf, 'pred':[]},
                 'Võru':{'cost':inf, 'pred':[]},
                 'Valga':{'cost':inf, 'pred':[]},
                 'Viljandi':{'cost':inf, 'pred':[]},
                 'Pärnu':{'cost':inf, 'pred':[]},
                 'Kuressaare':{'cost':inf, 'pred':[]},
                 'Tallinn':{'cost':inf, 'pred':[]},
                 'Rakvere':{'cost':inf, 'pred':[]},
                 'Jõhvi':{'cost':inf, 'pred':[]}
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
        'Tartu': {'Võru': 60, 'Viljandi': 90, 'Tallinn': 190, 'Jõhvi': 120, 'Valga': 90},
        'Võru': {'Tartu': 60, 'Valga': 40},
        'Valga': {'Tartu': 90, 'Võru': 40, 'Viljandi': 80, 'Pärnu': 100},
        'Viljandi': {'Tartu': 90, 'Valga': 80, 'Pärnu': 100, 'Tallinn': 150},
        'Pärnu': {'Kuressaare': 120, 'Viljandi': 100, 'Valga': 100, 'Tallinn': 150, 'Rakvere': 200},
        'Kuressaare': {'Pärnu': 120, 'Tallinn': 150},
        'Tallinn': {'Kuressaare': 150, 'Tartu': 190, 'Pärnu': 150, 'Jõhvi': 100, 'Rakvere': 60},
        'Rakvere': {'Tallinn': 60, 'Pärnu': 200, 'Jõhvi': 40},
        'Jõhvi': {'Tartu': 120, 'Rakvere': 40, 'Tallinn': 100}
        }
    source = 'Tartu'
    destination = 'Rakvere'
    dijkstra(graph,source,destination)
aken.mainloop()
