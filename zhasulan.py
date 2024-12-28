x = int(input(""))
lst= {}
ls = []
lt = []
for i in range(0, x):
    q = input("")
    w = int(input(""))
    lt.append(q)
    ls.append(w)
    lst[q] = w

for key, value in lst.items():
    for i in ls:
        if value == i:
            print(key)
            print(lt[ls.index(i)])

print(lst)
