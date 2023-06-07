import pypianoroll
import numpy as np
import os
from urllib.parse import unquote

def importMidiFiles():
    midi_paths = getMidiPaths()
    mid_arr = []

    for midi_path in midi_paths:
        mid = pypianoroll.read(midi_path)
        arr = [np.argmax(note) for note in mid.tracks[0].pianoroll]
        arr = convertMidi(arr)

        mid_arr.append(arr)

    song_list = getSongTitles()

    return mid_arr, song_list

def getMidiPaths():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    mid_path = os.path.join(cur_path, '../dataset/midi')

    midi_names = os.listdir(mid_path)
    midi_names.pop()
    path_list = [os.path.join(mid_path, midi) for midi in midi_names]
    
    return path_list

def convertMidi(arr):
    n_arr = list(filter(lambda a: a != 0, arr)) # remove silence

    # convert -> A = 0, A# = 1, B = 2, ...
    for i in range(len(n_arr)):
        n_arr[i] = (n_arr[i] % 12 + 3) % 12

    return n_arr

def getSongTitles():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    mid_path = os.path.join(cur_path, '../dataset/midi')

    midi_names = os.listdir(mid_path)
    fi = midi_names[-1]
    path = os.path.join(mid_path, fi)
    
    song_list = []
    with open(path, 'r') as f:
        i = 1
        for line in f:
            split = line[6:].split('\t')
            if (split[0] != '-'):
                song_list.append(split[0])
            else:
                song_list.append('Song ' + str(i))
            i += 1
            
    return song_list

def convertUnicode(uni):
    # unquoted = unquote(uni)
    # print(unquoted.decode('utf-8'))
    # format(ord("c"), "x")
    hex = [ format(ord(item), "x") for item in uni]
    # hex = [ item.encode('utf-8').hex() for item in uni ]
    # print(str(uni.decode('gbk')))
    print(hex)
    stri = ''
    h = ''
    for i in range(len(hex)):
        h += hex[i]
        if (i % 2 != 0):
            stri += '\\u' + h
            h = ''
    print(stri)
    
    print(stri.encode('ascii').decode('unicode-escape'))



if __name__ == '__main__':
    print(getSongTitles())
    # convertUnicode('´ÓºÜ¾ÃÒÔÇ°¿ªÊ¼')
    # c = u'%b4%d3%ba%dc%be%c3%d2%d4%c7%b0%bf%aa%ca%bc'