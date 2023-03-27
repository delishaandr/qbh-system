import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import crepe
from read_pv import getPvPaths

def detectPitch(audio_path):
    sf, audio = wavfile.read(audio_path)
    time, frequency, confidence, activation = crepe.predict(audio, sf, viterbi=True, step_size=8)

    # if confidence is below threshold, frequency becomes 0
    threshold = 0.6 # can be changed for better accuracy
    for i in range (len(frequency)):
        if (confidence[i] < threshold): 
            frequency[i] = 0

    frequency = frequency[1:]

    return frequency
