"""
Ovo je rjesenje prvog zadatka vjezbe 4
"""

niz = input("Unesite niz znakova: ")
print(f"Duljina niza je {len(niz)}.")
print(f"Znak najveće vrijednosti je {max(niz)}")
print(f"Znak najmanje vrijednosti je {min(niz)}")
if len(niz)>1 :
    print(f"Drugi član niza je {niz[1]}")
print(f"Zadnji član niza je {niz[-1]}")
print(niz,niz,niz,sep=".")
if len(niz)>1 :
    print(niz[1:-1])
print(niz[::-1])
print(niz[1::2])
