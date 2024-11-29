#აქ მინდა დროის სხვაობა ვაჩვენო გენერატორსა და for loop ს შორის

#უბრალოდ დავითვალოთ და ჩამოვწერო რიცხვები 1 დან 10000000 მდე

#დროის დასანახად შემოვიტანოთ time  და გავწეროთ ყველაფერი შემდეგნაირად
"""
import time

# Using list comprehension
start = time.time()
s = [x**2 for x in range(1000000)]
finish = time.time()
print(finish - start)

# Using a for loop
start_for = time.time()
ls = []
for n in range(1000000):
    ls.append(n**2)
finish_for = time.time()
print(finish_for - start_for)


#მაგალითად 

ls = (x for x in range(1000000000000))

for i in ls:
    if i> 10000000:
        break
    print(i, end="")

print(ls)
"""