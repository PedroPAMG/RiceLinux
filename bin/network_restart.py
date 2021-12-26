import os
import time

def command(comm):
    os.system(comm)

command('ifconfig eth0 down')
time.sleep(1)
command('ifconfig eth0 up')