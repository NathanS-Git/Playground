import numpy as np
import decimal as dec

dec.getcontext().prec = 1000

a = dec.Decimal(1)
b = dec.Decimal(1/dec.Decimal(2).sqrt())
t = dec.Decimal(1/4)
p = dec.Decimal(1)

with open("pi.txt","r") as f:
    actual_pi = dec.Decimal(f.readline())

for N in range(100):
    print(f"{N}",end='\r')
    a_n = (a+b)/2
    b_n = (a*b)**dec.Decimal(1/2)
    t_n = t - p*(a-a_n)**2
    p_n = 2*p

    pi = ((a_n+b_n)**2)/(4*t_n)
    a,b,t,p = a_n,b_n,t_n,p_n

    if round(actual_pi,998) == round(pi,998):
        print(f"Same after {N} iterations.")
        break
#print(f"{actual_pi:.500f}")
#print(f"{pi:.500f}")