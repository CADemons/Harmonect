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
    if (prev_state != None): 
        prev_state.play()
        print("Prev state", prev_state.map)
    current_state.play() 
    print("Current state", current_state.map)
    time.sleep(4) # 4 seconds is the sweet spot
    return current_state

class State:

    """
    Stores a step state.
    :type steps: Boolean Array.
    :param steps: an array which is mapped to the current configuration of steps.

    :type sc: scales.scaleName
    :param sc: a scales.Object from mingus that you'd like to play. By default, it's a standard Diatonic. Optional field

    :example:
    ex = State([True, True, False])
    
    """
    def __init__(self, steps, sc=scales.Diatonic):
        self.steps = steps
        self.sc = sc
        self.map = self.__drawMap()

    """
    Draws the map based on the current step progression.
    
    :private:

    """
    def __drawMap(self, oc=4):
        tmp = []
        dia = self.sc('C', (3,7),int(math.ceil((len(self.steps) / 7.0)))).ascending()
        k = 0 
        s = self.steps
        while (len(s) > 0):
            if k % 7 == 0 and k != 0:
                oc += 1
            if s[0]:
                tmp.append(Note(dia[0], oc))
            k += 1
            s.pop(0)
            dia.pop(0)
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
    def play(self):
        fluidsynth.play_NoteContainer(NoteContainer(self.map))


processSteps([True,True,False,False,False,False,False,False,True,True], State([False,False,True]))
# processSteps([True,True,False,False,False,False,False,False,True,True])