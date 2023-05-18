import numpy as np

def returnPvLabels(bins):
    pv_labels = []
    for bin in bins:
        labels = [np.argmax(x) for x in bin]
        pv_labels.append(labels)
    
    return pv_labels

def removePvSilence(pvs):
    for i in range(len(pvs)):
        pvs[i] = list(filter(lambda a: a != 0, pvs[i])) # remove all silence (0)
        pvs[i] = [x-1 for x in pvs[i]] # 0 -> A, 1 -> A#, ...

    return pvs
