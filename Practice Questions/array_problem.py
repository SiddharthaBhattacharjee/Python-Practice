list = ['ben','kenny',',','=','Sean',100,'tag242']
olist = []
for a in list:
   if str(a).isalnum():
      olist.append(a)
print(olist)
