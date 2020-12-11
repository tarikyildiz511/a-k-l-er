isim = input("isminizi giriniz")
sevisim = input("sevgilinizin ismini giriniz")
ask = len(isim)+len(sevisim)
if len(isim)>len(sevisim):
    ask-=5
else:
    ask +=3
    ask*=52
    ask = ask /(100+len(sevisim))

if ask>10:
    ask = 10

else:
    ask = round(ask)



print(f"{isim} ve {sevisim} {ask} ask puanı")