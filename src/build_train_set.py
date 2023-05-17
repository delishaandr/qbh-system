import numpy as np
from load_humming_set import buildHummingSet

def buildTrainSet():
    tr_f, tr_p, tr_l, te_f, te_p, te_l, tu_f, tu_p, tu_l = buildHummingSet()

    # freqs -> reshape (len(freqs), 250, 1)
    tr_f = np.reshape(tr_f, (len(tr_f), 250, 1))
    te_f = np.reshape(te_f, (len(te_f), 250, 1))
    tu_f = np.reshape(tu_f, (len(tu_f), 250, 1))

    # pvs -> convert to labels (0..12), to binary list
    tr_p = makePvBin(tr_p)
    te_p = makePvBin(te_p)
    tu_p = makePvBin(tu_p)

    return tr_f, tr_p, tr_l, te_f, te_p, te_l, tu_f, tu_p, tu_l

def makePvBin(pvs):
    all_bin = []
    for pv in pvs:
        conv_pv = convertPv(pv)
        bin_pv = []
        for c in conv_pv:
            bin = [0 for i in range (13)]
            bin[c] = 1
            bin_pv.append[bin]
        all_bin.append(bin_pv)
    
    return np.array(all_bin)

def convertPv(pv):
    conv_pv = []
    for i in range (len(pv)):
        if (pv[i] == 0):
            conv_pv.append(0) # 0 -> silence
        else:
            conv_pv.append((pv[i] % 12 + 3) % 12 + 1) # 1 -> A, 2 -> A#, 3 -> B, ...