import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import crepe
from read_pv import getPvPaths

def detectPitch(audio_path):
    sf, audio = wavfile.read(audio_path)
    time, frequency, confidence, activation = crepe.predict(data, Fs, viterbi=True, step_size=8)

    # if confidence is below threshold, frequency becomes 0
    threshold = 0.5 # can be changed
    for i in range (len(frequency)):
        if (confidence < threshold): 
            frequency[i] = 0

    frequency.pop()

    return frequency
