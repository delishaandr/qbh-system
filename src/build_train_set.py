from audio_processing import detectPitch
import numpy as np
import os

def buildTrainSet(): # yang dipanggil ini aja
    paths = getPvPaths()

    all_freq = []
    all_pv = [] # 1107750 pitch vector, range 30 - 86

    for path in paths:
        audio_path = path + '.wav'
        pv_path = path + '.pv'

        freq_list = detectPitch(audio_path)
        pv_list = cleanData(freq_list, makePvList(pv_path))

        all_freq.append(freq_list)
        all_pv.append(pv_list)

    all_freq = list(np.concatenate(all_freq).flat)
    all_pv = list(np.concatenate(all_pv).flat)

    return all_freq, all_pv

    # TODO: split data set jadi 80% train, 10% test, 10% tuning
    #       liat distribusi pv dulu (matplotlib)

# Return list of paths to .pv files
def getPvPaths():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    train_path = os.path.join(cur_path, '../train')

    # Get year names
    years = os.listdir(train_path)
    years.pop() # remove txt

    path_list = []

    for year in years:
        year_path = os.path.join(train_path, year)
        
        # Get person names
        persons = os.listdir(year_path)
        persons.pop() # remove txt

        for person in persons:
            person_path = os.path.join(year_path, person)
            
            for file in os.listdir(person_path):
                if file.endswith('.pv'):
                    path_list.append(os.path.join(person_path, file[:-3]))
        
    return path_list

def makePvList(pv_path):
    f = open(pv_path, 'r')
    pv_list = [round(float(line.rstrip('\n'))) for line in f]
    f.close()
    
    return pv_list

def cleanData(freq_list, pv_list):
    new_pv = []
    for i in range (len(pv_list)):
        if (freq_list[i] == 0):
            new_pv.append(0)
        else:
            new_pv.append(pv_list[i])

    return new_pv

if __name__ == "__main__":
    pv, freq = buildTrainSet()

    print(pv)
    print(freq)