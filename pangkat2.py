import sys
import os
import time
import random
import socket

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.4)

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
c = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"

angka1 = input(y+"Masukan Angka Yang Mau Dipangkat"+r+":")
angka2 = input(y+"Pangkat Berapa"+r+":")
print y+"loading",mengetik('........')
os.system('sleep 1')
os.system('clear')
print g+"pangkat dari"+w+" ",angka1," "+g+"dan"+w+" ",angka2," "+g+"adalah"+r
print(        angka1 ** angka2)
