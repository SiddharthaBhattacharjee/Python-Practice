import sys
import os
import csv
fruits = [ ##items 
    {"item": "apple",
        "quantity": 5,
        "price": 0.95},
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    },
    {
        "item": "orange",
        "quantity": 7,
        "price": 0.99
    }]

keys = fruits[0].keys()

try:
   os.mkdir("./CSV")
except OSError as e:
   print("Directory exists")

'''
index = 0
for key in fruits:
    index += 1
    if index == 4:
        file_name = f"batch{index}.csv"
        with open("./CSV/" + f"batch{index}.csv", 'a', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(fruits)'''

index = 1
count=0
for dict_ in fruits:
   count +=1
   for k,v in dict_.items():
      print(dict_)
      file_name = f"batch{index}.csv"
      with open("./CSV/" + f"batch{index}.csv", 'a', newline='') as output_file:
            dict_writer = csv.writer(output_file)
            dict_writer.writerow([k,v])
   if count ==5:
      count = 0
      index += 1
      
      
