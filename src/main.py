from read_pv import getPvPaths, makePvList
from audio_processing import detectPitch

paths = getPvPaths()

for path in paths:
    audio_path = path + '.wav'
    pv_path = path + '.pv'

    pv_list = makePvList(pv_path)
    freq = detectPitch(audio_path)

    # TODO: tiap pv list, freq dipake buat training model
    #       4 freq -> 1 pv

    # print
    for i in range (len(pv_list)):
        print('('+ str(freq[i*4]) + ' ' + str(freq[i*4+1]) + ' ' + str(freq[i*4+2]) + ' ' + str(freq[i*4]) + ') => ' + str(pv_list[i]))

    break