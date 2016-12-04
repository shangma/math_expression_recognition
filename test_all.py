import os
import sys

path = sys.argv[1]
lst = os.listdir(path)
for f in lst:
	if f.endswith(".jpg") or f.endswith(".png"):
		print "Showing result of:\n"+path+"/"+f
		cmd = "python run.py " + path+"/"+f
		os.popen(cmd)

		#var = raw_input("next?")
		#if var=="n" or var=="no":
		#	break
