import os
import sys

path = sys.argv[1]
lst = os.listdir(path)
for f in lst:
	if f.endswith(".jpg") or f.endswith(".png"):
		cmd = "python run.py " + path+"/"+f
		print os.popen(cmd)
		var = raw_input("next?")
		if var=="n" or var=="no":
			break