import csv

g = {'Maths':80,'Physics':70,'Chemistry':70,'CS':70,'English':80}

with open('data.csv','a') as csvfile:
    wrt = csv.writer(csvfile)

    for key,value in g.items():
        wrt.writerow([key,value])
        
