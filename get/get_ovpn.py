import os
import random 
from random import randint

os.system("wget http://www.vpngate.net/api/iphone/ -O table.csv")

lines = [line for line in open("table.csv")]
l = lines[random.randint(3, 7)].split(',')[-1]

with open("test.txt", "w") as f:
	f.write(l)

with open("need.ovpn", "w") as f:
	f.write(os.popen("base64 -d test.txt").read())


os.system("rm test.txt")
os.system("rm table.csv")
