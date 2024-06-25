from array  import *

num = array('i',[1,2,3,4,5,6,7])
 
name = "raja"; 

num.insert(7, 8)
num.append(9)

a=9


for i in range(0, len(num)):
    if num[i] == a:
       print(i)
       print(True)
       break

print(num)





name = ["maga", "yamuna", "keerthana", "vijaya"]

search_string = "kanda"
name.insert(0,search_string)

for names in name:
    if names == search_string:
        print("true")
        break
else:
    print('false')

print(name)

