import os
from time import sleep 

cur=os.getcwd()
cur=cur+"/qr"
while 1:
    y=os.listdir(cur)
    if len(y)!=0:
        os.system("lpr -P HL-1110-series ./qr/"+str(y[0]))
        print(y[0])
        os.remove(os.getcwd()+"/qr/"+str(y[0]))
        print("printing")
        break

    sleep(2)
