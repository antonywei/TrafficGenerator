import subprocess
import time
import sys
import math
import os

#dataset=[300,310,320,330,340,350,360,370,380,390,400,400,390,380,370,360,350,340,330,320,310,300]

#dataset=numpy.sin(numpy.arange(1,30,0.03))
#define bandwidth change rate
min_rate=500
max_rate=1000

#define period time
basic_flow_period = 500
add_flow_period = 200
interval = 50
add_times= 4

flow_raw = "taskset -c 0 ./bin/client -b 300 -c conf/client_config.txt -t "+str(basic_flow_period)+" -l flows.txt -s 123 -r bin/result.py"
flow_add_header = "taskset -c 1 ./bin/client -b 100 "
flow_add_tail = " -t "+str(add_flow_period)+" -l flows.txt -s 123 -r bin/result.py"

subprocess.Popen(flow_raw,shell=True)
time.sleep(interval)
for i in range(1,add_times+1):
    fullcmd = flow_add_header+"-c conf/client_config"+str(i)+".txt" + flow_add_tail
    subprocess.Popen(fullcmd,shell=True)
    time.sleep(interval)

