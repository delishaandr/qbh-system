import pypianoroll
import numpy as np
import os

def importMidiFiles():
    midi_paths = getMidiPaths()
    mid_arr = []

    for midi_path in midi_paths:
        mid = pypianoroll.read(midi_path)
        arr = [np.argmax(note) for note in mid.tracks[0].pianoroll]
        arr = convertMidi(arr)

        mid_arr.append(arr)

    return mid_arr

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

if __name__ == '__main__':
    mid_list = importMidiFiles()
    print(mid_list[1])