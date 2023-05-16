import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from general_ops import padList, removeSilence
import crepe

def extractPitch(audio_path):
    sf, audio = wavfile.read(audio_path)
    time, frequency, confidence, activation = crepe.predict(audio, sf, viterbi=True, step_size=32)

    # if confidence is below threshold, frequency becomes 0
    threshold = 0.6 # can be changed for better accuracy
    for i in range (len(frequency)):
        if (confidence[i] < threshold): 
            frequency[i] = 0

    frequency = frequency[1:]
    frequency, st = removeSilentStart(frequency)
    frequency

    return frequency, st

def removeSilentStart(freqs):
    new_freqs, st = removeSilence(freqs)

    if (len(new_freqs) < 250):
        new_freqs = padList(new_freqs)
    elif (len(new_freqs) > 250):
        new_freqs = new_freqs[:250]

    return new_freqs, st

if __name__ == '__main__':
    path = 'd:/coolyeah/IF4092-TA2/TA/qbh-lstm-sdtw/dataset/hum\year2003/person00001/00019.wav'

    freq, st = extractPitch(path)