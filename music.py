# music.py -
import math, time
import mingus.core.notes as notes
import mingus.core.scales as scales
from mingus.midi import fluidsynth
from mingus.containers import Note
from mingus.containers import NoteContainer

def processSteps(steps, prev_state=None):
    """
    Play music when a person is standing on a specific step.

    :type steps: Boolean Array
    :param steps: an array which is mapped to the current configuration of steps. 

    :example:
    processSteps([True,False,False,False])
    ==> maps steps: step 1 = steps[0], step 2 = steps[1], etc etc.
    ==> for all true steps, play a specific note
    
    :returns current_state: Returns the current state of the what's playing, so you can call it again in another call of 
    processSteps.  
    """
    fluidsynth.init("GeneralUser GS v1.471.sf2")
    current_state = State(steps)

    print("Current state", current_state.map)

    current_state.play(4) # 4 seconds is the sweet spot

    return current_state

class State:

    """
    Stores a step state.
    :type steps: Boolean Array.
    :param steps: an array which is mapped to the current configuration of steps.

    :example:
    ex = State([True, True, False])
    
    """
    def __init__(self, steps):
        self.steps = steps
        self.map = self.__mapNotes()

    """
    Draws the map based on the current step progression.
    
    :private:

    """
    def __drawMap(self):
        tmp = []
        dia = scales.Diatonic('C', (3,7),int(math.ceil((len(self.steps) / 7.0))))
        for x in range(0, len(self.steps)):
            if self.steps[x]:
                tmp.append(dia.ascending()[x])
        return tmp

    """
    Maps notes to the drawn map.

    :private:
    """

    def __mapNotes(self, oc=4):
        tmp = []
        ocm = oc
        added = []
        m = self.__drawMap()
        for x in range(0, len(m)):
            if x % 7 == 0 and x != 0:
                oc += 1
            if m[x] in added:
                ocm = oc + 1
                tmp.append(Note(m[x], ocm))
            else:
                tmp.append(Note(m[x], oc))
            added.append(m[x])
        
        return tmp

    """
    Play notes for each activiated step.
    
    :type t: Number
    :param t: Time, in seconds, for delay of chord
    :example:
    steps == [True, False]
    play() ==> plays "C" 

    steps == [True, False, True]
    play() ==> plays "C", "E"

    """
    def play(self, t):
        fluidsynth.play_NoteContainer(NoteContainer(self.map))
        time.sleep(t)


processSteps([True,False,True,False,False,False,False,True,False,True])