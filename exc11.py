list1 = [1,2,3,4,5]
list2 = [9,8,7,6]
x = 0

for i in list1:
    if i in list2:
        x += 1
if x > 0:
    print(True)
    
