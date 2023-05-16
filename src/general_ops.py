import numpy as np

def padList(li):
    pad = 250 - len(li)
    new_li = np.append(li, np.zeros(pad, dtype=int))

    return new_li

def removeSilence(li):
    end_loop = False
    i = 0

    while (end_loop == False):
        if (li[i] == 0):
            i += 1
        else:
            if (all(x == 0 for x in li[i+1:i+5])):
                i += 1
            else:
                end_loop = True
        if (i == len(li)):
            end_loop = True

    return li[i:len(li)], i

def removeSilenceFromStart(li, start):
    new_li = padList(li[start:len(li)])
    new_li, st = removeSilence(new_li)
    new_li = padList(new_li)

    return new_li, st

if __name__ == '__main__':
    arr = [0,0,0,1]
    print(all(x == 0 for x in arr))