list100 = [1, 1, 1]
list200 = [2, 2, 2]
save_dict = dict()
for i in [100, 200]:
   exec(f"save_dict[i] = list{str(i)}")
print(save_dict)
