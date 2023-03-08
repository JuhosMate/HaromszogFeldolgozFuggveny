import math

#függvények
def HaromszogKerulete(aa, bb, cc):
    return aa + bb + cc

def HaromszogTerulete(aa, bb, cc):
    s = HaromszogKerulete(aa, bb, cc) / 2
    TT = math.sqrt( s*(s-aa)*(s-bb)*(s-cc) )
    return TT

#0
print("Háromszög feldolgozása függvények segítségével.")

#1
temp = input("Kérem az oldalakat ';'-el elválasztva:")
reszletek = temp.split(';')
a=float(reszletek[0].replace(',' , '.'))
b=float(reszletek[1].replace(',' , '.'))
c=float(reszletek[2].replace(',' , '.'))

#2
K = HaromszogKerulete(a, b, c)
T = HaromszogTerulete(a, b, c)

#3
print(f"A(z) {a:.2f}cm, {b:.2f}cm és {c:.2f}cm oldalhosszúságú háromszög kerülete: {K:.2f}cm.")
print(f"A(z) {a:.2f}cm, {b:.2f}cm és {c:.2f}cm oldalhosszúságú háromszög területe: {T:.2f}cm^2.")