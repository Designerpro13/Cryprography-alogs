HBD="Rhld.fnnc.sdws"

a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!}{,/':/n-1234567890. "

decr=""
key=int(input('Enter Pass key num: '))
for p in HBD:
    n_p=(a.find(p)+key)%len(a)
    decr+=a[n_p]
print(decr)
