import time
import os

m = input("Minute : ")
os.system("clear")
s = input("Seconde : ")
os.system("clear")


def chrono(x):
    minute = x // 60
    seconde = x % 60
    millième = (x % 1) * 1000
    os.system("clear")
    print(f"Temps : {minute:.0f}:{seconde:.0f}:{millième:.0f}")

début = time.time()

while True:
    x = time.time() - début
    chrono(x)
    time.sleep(0.01)
    if (x // 60) == int(m) and (round(x % 60)) == int(s):
        break