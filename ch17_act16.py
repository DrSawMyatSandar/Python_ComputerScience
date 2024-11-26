#ch17_activity16
import time
from time import sleep
start='n'
while start!='y':
    start=input("Press y to start")
    for sequence in range(16):
        light=['red','red and amber','green','amber'][sequence%4]
        print(light)
        time.sleep(1.5)
