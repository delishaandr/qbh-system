from general_ops import removeSilenceFromStart
from feature_extraction import extractPitch
import numpy as np
import os

def buildHummingSet(b_type = 'load'):
    cur_path = os.path.abspath(os.path.dirname(__file__))
    train_paths, test_paths, tune_paths = splitTrainingSet()

    if (b_type == 'build'):
        train_freqs, train_pvs = loadAudioPv(train_paths)
        test_freqs, test_pvs = loadAudioPv(test_paths)
        tune_freqs, tune_pvs = loadAudioPv(tune_paths)

        all_freqs = np.append(np.append(train_freqs, test_freqs, axis=0), tune_freqs, axis=0)
        all_pvs = np.append(np.append(train_pvs, test_pvs, axis=0), tune_pvs, axis=0)

        np.save(os.path.join(cur_path, '../ext/freqs'), all_freqs)
        np.save(os.path.join(cur_path, '../ext/pvs'), all_pvs)

    # load variables
    all_freqs = np.load(os.path.join(cur_path, '../ext/freqs.npy'))
    all_pvs = np.load(os.path.join(cur_path, '../ext/pvs.npy'))

    train_freqs = all_freqs[0:3638]
    train_pvs = all_pvs[0:3638]
    test_freqs = all_freqs[3638:4034]
    test_pvs = all_pvs[3638:4034]
    tune_freqs = all_freqs[4034:]
    tune_pvs = all_pvs[4034:]

    train_labels = [int(x[-5:])-1 for x in train_paths]
    test_labels = [int(x[-5:])-1 for x in test_paths]
    tune_labels = [int(x[-5:])-1 for x in tune_paths]

    return train_freqs, train_pvs, train_labels, test_freqs, test_pvs, test_labels, tune_freqs, tune_pvs, tune_labels

def loadAudioPv(paths):
    freqs = []
    pvs = []

    for path in paths:
        audio_path = path + '.wav'
        pv_path = path + '.pv'

        freq_list, start = extractPitch(audio_path)
        pv_list = makePvList(pv_path)

        # remove silence
        while (start != 0):
            pv_list, start = removeSilenceFromStart(pv_list, start)
            freq_list, start = removeSilenceFromStart(freq_list, start)
            if (all(x == 0 for x in pv_list)):
                start = 0

        # TODO: kalau isi list nol, hapus dari list
        if (all(x == 0 for x in pv_list)):
            continue
        
        freqs.append(freq_list)
        pvs.append(pv_list)
    
    return np.array(freqs), np.array(pvs)

def splitTrainingSet():
    train_paths = []
    test_paths = []
    tune_paths = []

    cur_path = os.path.abspath(os.path.dirname(__file__))
    hum_path = os.path.join(cur_path, '../dataset/hum')

    # Get year names
    years = os.listdir(hum_path)
    years.pop() # remove txt

    for year in years:
        year_path = os.path.join(hum_path, year)
        
        # Get person names
        persons = os.listdir(year_path)
        persons.pop() # remove txt

        for person in persons:
            person_path = os.path.join(year_path, person)
            path_list = []

            # terlalu banyak label yang 0 padahal tidak silence
            # if (year == 'year2008' and person == 'person00013'):
            #     continue
            
            for file in os.listdir(person_path):
                if file.endswith('.pv'):
                    path_list.append(os.path.join(person_path, file[:-3]))

            s_tr_te = 0
            s_te_tu = 0
            n = len(path_list)
            if (n < 10):
                s_tr_te = n-2
                s_te_tu = n-1
            else:
                len_train = n // 10 * 8 + n % 10
                # if (n < 15):
                #     len_train -= 2
                len_rest = n - len_train
                len_test = len_rest // 2

                s_tr_te = len_train
                s_te_tu = len_train + len_test

            train_paths = np.append(train_paths, path_list[0:s_tr_te]).tolist()
            test_paths = np.append(test_paths, path_list[s_tr_te:s_te_tu]).tolist()
            tune_paths = np.append(tune_paths, path_list[s_te_tu:n]).tolist()

    return train_paths, test_paths, tune_paths

def makePvList(pv_path):
    f = open(pv_path, 'r')
    pv_list = [round(float(line.rstrip('\n'))) for line in f]
    f.close()
    
    return pv_list

def getHummingPaths():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    hum_path = os.path.join(cur_path, '../dataset/hum')

    # Get year names
    years = os.listdir(hum_path)
    years.pop() # remove txt

    path_list = []

    for year in years:
        year_path = os.path.join(hum_path, year)
        
        # Get person names
        persons = os.listdir(year_path)
        persons.pop() # remove txt

        for person in persons:
            person_path = os.path.join(year_path, person)
            
            for file in os.listdir(person_path):
                if file.endswith('.pv'):
                    path_list.append(os.path.join(person_path, file[:-3]))
        
    return path_list

if __name__ == '__main__':
    tr, te, tu = splitTrainingSet()
    print(te[2])
    # print([int(x[-5:])-1 for x in tr])

    # tr_f, tr_p, te_f, te_p, tu_f, tu_p = buildHummingSet()
    # print(len(tr_f), len(te_f), len(tu_f))

    # cur_path = os.path.abspath(os.path.dirname(__file__))
    # r_freq = np.load(os.path.join(cur_path, '../ext/train_pvs.npy'))
    # e_freq = np.load(os.path.join(cur_path, '../ext/test_pvs.npy'))
    # u_freq = np.load(os.path.join(cur_path, '../ext/tune_pvs.npy'))
    # a_freq = np.load(os.path.join(cur_path, '../ext/pvs.npy'))
    # print(len(r_freq), len(e_freq), len(u_freq))

    # /dataset/hum\year2008\person00013
    #TODO: tambahin ke laporan kenapa yang ini dihapus