# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:09:09 2019

@author: Tejas
"""

from pydub import AudioSegment
from scipy.io import wavfile  #anaconda
import sounddevice as sd
import numpy as np           #anaconda
import random


sound = AudioSegment.from_mp3('Roar of the Revengers.mp3')
sound.export('Roar of the Revengers.wav', format = 'wav')

fs, data = wavfile.read('Roar of the Revengers.wav')

data = data[0:2000000]

data1 = data[ :,0]

#sd.play(data,fs)
#sd.stop()

###########  RSA Algorithm Start ############3

def gcd(a, h):
    while(1):
        temp = a%h
        if(temp == 0):
            return h;
        a = h
        h = temp
    


p = 37
q = 23
n = p*q
totient = (p-1)*(q-1)
e = random.randrange(1, totient)
#Use Euclid's Algorithm to verify that e and phi(n) are comprime
g = gcd(e, totient)
while g != 1:
    e = random.randrange(1, totient)
    g = gcd(e, totient)

    
def multiplicative_inverse(e, phi):
    d = None
    i = 1
    exit = False
    while not exit:
        temp1 = phi*i +1
        d = float(temp1/e)
        d_int = int(d)
        i += 1
        if(d_int == d):
            exit=True
    return int(d)
       

#choosing d such that it satisfies d*e = 1 + k * totient
#d = (1 + (k*totient))/e   # 5
d = multiplicative_inverse(e, totient)
"""
msg = 700

############### Encryption       

c = (msg ** d) % n

c = int(np.power(msg, d))     # 248832
c = math.fmod(c, n)     ### 3


################# Decryption
import math

m = (c ** e) % n

m = np.power(c, e)       # 9.5396
m = math.fmod(m, n)     ### 12.0 
"""



################ Encryption of Data1
c_list = []  ## encrypted list

for i in range(0, len(data1)):
    current_msg = data1[i]
    current_c = Decimal(0)
    current_c = np.power(current_msg, e)
    current_c = math.fmod(current_c, n)
    
    c_list.append(current_c)
   

## c_list.append(np.power(data1[i], e))
## [c_list.append(np.power(data1[i], e)) for i in data1]
c_song = np.array(c_list)   #encrypted song
#sd.play(c_song)

m_dec = []  #decrypted list

for i1 in range(0, len(c_list)):
    current_m = np.power(c_list[i1], d)
    current_m = math.fmod(current_m, n)
    
    #c_dec.append(current_c)
    m_dec.append(current_m)
    
m_song = np.array(m_dec)
sd.play(m_song, fs)   ### decrypted song
sd.stop()

m_song = np.array(m_dec)



import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

compare(c_list, m_dec)




