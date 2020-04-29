import os
l = os.listdir("get")

for x in l:
	if ".py" or ".sh" in x:
		os.system("bash get/"+x)