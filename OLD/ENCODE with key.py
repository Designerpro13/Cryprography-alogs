HBD="Sime good text"

a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!}{,/':/n-1234567890. "

encr= ""
key=int(input('Enter Pass key num: '))
for p in HBD:
    n_p=(a.find(p)-key)%len(a)
    encr+=a[n_p]
print(encr)