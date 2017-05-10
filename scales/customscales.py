import os, yaml
import mingus.core.scales as scales

from mingus.core.keys import get_notes
from mingus.core.intervals import interval, second

def listNames():
    ls = os.listdir('.')
    tmp = []
    for item in ls:
        tmp.append(''.join(item.split('.yml')))
    return tmp

def test():
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    return notes * 1 + [notes[0]]

def buildFn(pos, key):
    p = pos.split(',')
    print(p[0])
    return {
        "second": second(p[1], key),
        "interval": interval(key, p[1], int(p[2] if 2 < len(p) else -1))
    }[p[0]]


if __name__ == '__main__':
    #print(listNames())
    # print(doc['params']['one'])
    # print(get_notes('C'))
    # print(get_notes('c'))

    with open('major.yml', 'r') as f:
        doc = yaml.load(f)
    # tmp = [doc['key']]
    # for item in doc['logic'].split(' '):
    #     tmp.append(buildFn(item, doc['key']))
    #     print tmp
    # #print tmp
    print(doc['ascending'])

