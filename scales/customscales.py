import os, yaml
import mingus.core.scales as scales

from mingus.core.keys import get_notes
from mingus.core.intervals import interval

def listNames():
    ls = os.listdir('.')
    tmp = []
    for item in ls:
        tmp.append(''.join(item.split('.yml')))
    return tmp

def test():
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    return notes * 1 + [notes[0]]

def build(i, sekey, iv):
    if i < 0:
        return
    return interval(doc['fn']['key'], sekey, iv) + build(i - 1, interval(doc['fn']['key'], sekey, iv), 1)

if __name__ == '__main__':
    #print(listNames())
    # print(doc['params']['one'])
    # print(get_notes('C'))
    # print(get_notes('c'))

    with open('test.yml', 'r') as f:
        doc = yaml.load(f)
    print(build(7, 'D', 1))
    print(eval(doc['fn']['name']+'("'+doc['fn']['params']+'")'))
    # cs = scales.Custom(doc['name'], doc['steps'], 'C')
    # print(cs)
    # print(cs.name)

