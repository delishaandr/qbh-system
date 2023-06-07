import math
import numpy as np

def ruleBasedQBH(all_freqs):
    labels = []
    for freqs in all_freqs:
        labels.append(getFreqLabels(freqs))
    
    return labels

def getFreqLabels(freqs):
    label = []
    for freq in freqs:
        if (freq == 0): # ignore if silence
            label.append(0)
        else:
            m = round(12 * math.log(freq / 440, 2) + 69)
            label.append((m % 12 + 3) % 12 + 1)
    
    return label