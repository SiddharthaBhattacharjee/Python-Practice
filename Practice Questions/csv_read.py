import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    dict_ = {}
    for row in reader:
        if(row[0].isnumeric()):
           dict_[row[0]] = [{"name":row[1]},{"Title":row[2]}]
print(dict_)
