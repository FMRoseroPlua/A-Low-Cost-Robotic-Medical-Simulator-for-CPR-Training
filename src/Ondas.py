import pickle
import numpy as np
from random import randint

with open("sinusoidal.txt",'rb') as fp:
    sinusoidal= pickle.load(fp)
            
with open("bradisinusoidal.txt",'rb') as fp:
    bradisinusoidal=pickle.load(fp)  
            
with open("TV.txt",'rb') as fp:
    TV=pickle.load(fp)
        
with open("TSV.txt",'rb') as fp:
    TSV=pickle.load(fp)


print(sinusoidal)
print("\n")
print(bradisinusoidal)
print("\n")
print(TV)
print("\n")
print(TSV)
print("\n")
xv=np.arange(1,6.3,0.1)
FV=(0.89+(np.sin(xv/2)-np.sin(randint(2,8)*xv/2)-np.cos(7*xv/2)+np.sin((xv/2)-2.5)-np.cos(9*(xv/2)-2))/10)
#FV=(round(elem,4) for elem in FV)
print(FV)
print("\n")

xv=np.arange(1,3.2*randint(1,3),0.1)
Ffa=[]
Ffa.extend(0.89+(np.sin(xv*0.75)-np.sin(randint(2,8)*xv*0.75)-np.cos(7*xv*0.75)+np.sin((xv*0.75)-2.5)-np.cos(9*(xv*0.75)-2))/10)#53
qrsfa=[0.9008,0.8873,1.422,2.087,1.651,0.7245,0.545,0.6893,0.8344,0.9325]#10 #4max #7min
fauricular=[round(i,4) for i in Ffa]
fauricular.extend(qrsfa)
print(fauricular)
print("\n") 
