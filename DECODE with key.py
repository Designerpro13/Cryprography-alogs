HBD="A0r5LGT5V3UW5mabl5bl5rhnk5eho0er5mpbmT55AtIIR5uBKMAwtR5wxtK5V,U5{5,-5R06kl5h.5va6kf56g95706nmr5V/U5Rhn56k05hg05h.5ma05i0hie05pah5 bo05f05ma05AHIx50o0krmbf05V'U5W5Rhn5en8dr58a6kfTT55Pblabg 56ee5ln880ll5bg5rhnk5.nmnk0444V:U5t5lf6ee5lnikbl05hg5fr570a6e.5.hk5ma05uY96r5Jn00g5"
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!}{,/':/n-1234567890. "
encr,decr="",""
key=int(input('Enter Pass key num: '))
for p in HBD:
    n_p=(a.find(p)+key)%len(a)
    decr+=a[n_p]
print(decr)
