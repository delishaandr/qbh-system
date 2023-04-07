from read_pv import getPvPaths, makePvList
from audio_processing import detectPitch
import numpy as np

def buildTrainSet():
    paths = getPvPaths()

    all_pv = [] # 1107750 pitch vector, range 30 - 86
    all_freq = []

    for path in paths:
        audio_path = path + '.wav'
        pv_path = path + '.pv'

        freq_list = detectPitch(audio_path)
        pv_list = cleanData(freq_list, makePvList(pv_path))

        all_pv.append(pv_list)
        all_freq.append(freq_list)

    all_pv = list(np.concatenate(all_pv).flat)
    all_freq = list(np.concatenate(all_freq).flat)

    # TODO: split data set jadi 80% train, 10% test, 10% tuning
    #       liat distribusi pv dulu (matplotlib)

def cleanData(freq_list, pv_list):
    new_pv = []
    for i in range (len(pv_list)):
        if (freq_list[i] == 0):
            new_pv.append(0)
        else:
            new_pv.append(pv_list[i])

    return new_pv