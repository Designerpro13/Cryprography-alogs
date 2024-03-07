HBD='Hey SN! {0}, this is your lovely twit!  HAPPY BIRTHDAY DEAR {1} - 17 Years of Charm and beauty {2} You are one of the people who give me the HOPE everytime {3} , You lucky charm!!  Wishing all success in your future...{4} A small suprise on my behalf for the B\'day Queen '
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!}{,/':/n-1234567890. "
ecr,decr="",""
key=int(input('Enter passkey num: '))
for p in HBD:
    n_p=(a.find(p)-key)%len(a)
    ecr+=a[n_p]
print(ecr)
