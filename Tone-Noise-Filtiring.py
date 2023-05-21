import numpy as np 
import matplotlib.pyplot as plt
import sounddevice as sd 
from scipy.fftpack import fft 


t= np.linspace(0,3,12*1024)
arrFREQ2=[392,329.63,392,392,329.23,392,440,392,349.23,329.63]
arrFREQ1 =[0,0,0,0,0,0,0,0,0,0]
arrt = [0,0.33,0.66,0.99,1.32,1.65,1.98,2.31,2.64,2.97]
arrT = [0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.3]
tmp = [] 
x = 0
n = 0

# tmp array represent the diffrent between two unit steps ;
for j in range (0,10):
    u1 = np.where(t>= arrt[j],1,0)
    u11 = np.where(t>=(arrt[j] + arrT[j]) , 1 , 0 )
    tmp.append((u1-u11))
for i in range (0,10):
   
    x+=(np.sin(2*np.pi*arrFREQ1[i]*t) + np.sin(2*np.pi*arrFREQ2[i]*t))*tmp[i]
plt.title('Signal Time Domain')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.subplot(5,2,1)
plt.plot(t,x)
# sd.play(x,3*1024)

       ### MILESTONE 2###
 
N = 3*1024
f = np.linspace(0,512,int(N/2))
x_f = fft(x)
x_f = 2/N *np.abs(x_f[0:int(N/2)])
plt.subplot(5,2,2)
plt.plot(f,x_f)


f2 = np.random.randint(0,512)
f1 = np.random.randint(0,512)
noise = np.sin(2*f1*np.pi*t) + np.sin(2*f2*np.pi*t)
x_noise = x + noise 
plt.subplot(5,2,3)
plt.plot(t,x_noise)


f = np.linspace(0,512,int(N/2))
x_noise_f = fft(x_noise)
x_noise_f= 2/N *np.abs(x_noise_f[0:int(N/2)]) ## amplitude 
plt.subplot(5,2,4)
plt.plot(f,x_noise_f)


maximum_original_signal = np.round(np.max(x_f))


peak = []
for i in range (0,len(x_noise_f)):
    if (np.round(np.max(x_f)) < np.round(x_noise_f[i])):
        peak.append(x_noise_f[i])


filterf1 = f[np.where(x_noise_f== peak[0])]
filterf2 = f[np.where(x_noise_f== peak[1])]
filterf1 = np.round(filterf1)
filterf2 = np.round(filterf2)
x_filtered = x_noise - ( np.sin(2*np.pi*t*filterf1) + np.sin(2*np.pi*t*filterf2) )
plt.subplot(5,2,5)

plt.plot(t,x_filtered)
sd.play(x_filtered , 3*1024)
    

    











                          
    



























 
