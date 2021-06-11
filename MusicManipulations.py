# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:39:14 2019

@author: Tejas

Python Audio Manipulations
"""

################ Converting Mp3 to Wav format 
"""
### Install pydub and ffmpeg in your anaconda 

conda install -c conda-forge ffmpeg
conda install -c conda-forge pydub

"""


from pydub import AudioSegment
from scipy.io import wavfile
import sounddevice as sd
import numpy as np


sound = AudioSegment.from_mp3('Roar of the Revengers.mp3')
sound.export('Roar of the Revengers.wav', format = 'wav')

fs, data = wavfile.read('Roar of the Revengers.wav')

sd.play(data,fs)
sd.stop()


#song = AudioSegment.from_wav('Roar of the Revengers.wav')
#play(song)
#playsound('Roar of the Revengers.wav')

from sklearn.preprocessing import StandardScaler
data1 = StandardScaler().fit_transform(data)
data2 = data[:,1]
data3 = data2[0:fs]

sd.play(data2,fs)

import librosa

### Try to apply fft on the audio                   ### Not much of use, low decibel same sound
d = np.abs(librosa.core.stft(data1))
y_hat = librosa.istft(d)
y_hat
sd.play(y_hat, fs)


#### Remove only harmonic and other than harmonic sounds from the audio    ### percussive actually good work
y_harmonic, y_percussive = librosa.effects.hpss(data1)

sd.play(y_harmonic, fs) 
sd.play(y_percussive, fs)

sd.stop()

from scipy import signal
b, a = signal.butter(2, 0.15, 'highpass', analog = False) #first parameter is signal order and the second one refers to frequenc limit. I set limit 30 so that I can see only below 30 frequency signal component
output = signal.filtfilt(b, a, data1)
sd.play(output, fs)
sd.stop()

data3 = data*1.5
sd.play(data3,fs)


sd.stop()







