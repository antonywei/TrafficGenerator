import subprocess
import time
import sys
import os


def main():
	server_Num=6
	for i in range(server_Num):
		fullcmd = "taskset -c "+str(2+i%2)+" ./bin/server -p "+str(5001+i)+" -d"
		print(fullcmd)
		subprocess.Popen(fullcmd,shell=True)

if __name__ == '__main__':
	main()