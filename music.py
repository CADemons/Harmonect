"""
music.py - handles music

Primary author: Colin Rioux (@colinrioux)
Supporting authors: Linc Berkeley (@lincb)

"""
import math, time
import mingus.core.scales as scales
from mingus.midi import fluidsynth
from mingus.containers import Note
from mingus.containers import NoteContainer

fluidsynth.init("GeneralUser GS v1.471.sf2")

def processSteps(steps, prev_state=None, sc="Diatonic", start_key="C"):
    """
    Play music when a person is standing on a specific step.

    :type steps: Boolean Array
    :param steps: an array which is mapped to the current configuration of steps.

    :type prev_state: State
    :param prev_state: A state or the previous state, usually returned via one call of processSteps(). Optional.

    :type sc: String
    :param sc: Scale name. Optional.

    :type start_key: String
    :param start_key: Key to start the scale. Optional.

    :example:
    processSteps([True,False,False,False])
    ==> maps steps: step 1 = steps[0], step 2 = steps[1], etc etc.
    ==> for all true steps, play a specific note

    :returns current_state: Returns the current state of the what's playing, so you can call it again in another call of
    processSteps.
    """
    current_state = State(steps, sc, start_key)
    if (prev_state is not None):
        prev_state.play()
        print('Prev state:\n{0}'.format(prev_state))
    current_state.play()
    print('Current state:\n{0}'.format(current_state))
    return current_state

class State:

    """
    Stores a step state.
    :type steps: Boolean Array.
    :param steps: an array which is mapped to the current configuration of steps.

    :type sc: String
    :param sc: Scale name. Optional.

    :example:
    ex = State([True, True, False])

    """
    def __init__(self, steps, sc="Diatonic", start_key='C'):
        self.steps = steps
        self.sc = sc
        self.start_key = start_key
        self.map = self.__drawMap()

    def __str__(self):
        return 'Map: {0}\nScale: {1}\nStart Key: {2}'.format(self.map, self.sc, self.start_key)

    """
    Draws the map based on the current step progression.

    :private:

    """
    def __drawMap(self, oc=4):
        tmp = []
        scl = self.__scaleArray()
        k = 0
        s = self.steps
        while len(s) > 0:
            if k % 7 == 0 and k != 0:
                oc += 1
            if s[0]:
                tmp.append(Note(scl[0], oc))
            k += 1
            s.pop(0)
            scl.pop(0)
        return tmp

    """
    Builds scale.

    :private:

    """
    def __buildScale(self):
        octa = int(math.ceil((len(self.steps) / 7.0)))
        return {
            "Diatonic": scales.Diatonic(self.start_key, (3, 7), octa),
            "Ionian": scales.Ionian(self.start_key, octa),
            "Dorian": scales.Dorian(self.start_key, octa),
            "Phrygian": scales.Phrygian(self.start_key, octa),
            "Lydian": scales.Lydian(self.start_key, octa),
            "Mixolydian": scales.Mixolydian(self.start_key, octa),
            "Aeolian": scales.Aeolian(self.start_key, octa),
            "Locrian": scales.Locrian(self.start_key, octa),
            "Major": scales.Major(self.start_key, octa),
            "HarmonicMajor": scales.HarmonicMajor(self.start_key, octa),
            "NaturalMinor": scales.NaturalMinor(self.start_key, octa),
            "HarmonicMinor": scales.HarmonicMinor(self.start_key, octa),
            "MelodicMinor": scales.MelodicMinor(self.start_key, octa),
            "Bachian": scales.Bachian(self.start_key, octa),
            "MinorNeapolitan": scales.MinorNeapolitan(self.start_key, octa),
            "Chromatic": scales.Chromatic(self.start_key, int(math.ceil((len(self.steps) / 12.0)))),
            "WholeTone": scales.WholeTone(self.start_key, int(math.ceil((len(self.steps) / 6.0)))),
            "Octatonic": scales.Octatonic(self.start_key, int(math.ceil((len(self.steps) / 8.0))))
        }[self.sc]

    """
    Converts scale object to an array.

    :type scl: Scale Object
    :param scl: Ideally from func buildScale().

    :type mode: String
    :param mode: Scale mode. Valid values include: `asc` & `desc`. Optional.

    :private:

    """
    def __scaleArray(self, scl=None, mode="asc"):
        if scl is None: scl = self.__buildScale()
        return {
            "asc": scl.ascending(),
            "desc": scl.descending()
        }.get(mode, "Invalid mode!")

    """
    Play notes for each activiated step.

    :example:
    steps == [True, False]
    play() ==> plays "C"

    steps == [True, False, True]
    play() ==> plays "C", "E"

    """
    def play(self):
        fluidsynth.play_NoteContainer(NoteContainer(self.map))

if __name__ == '__main__':
    processSteps([True, True, False, False, False, False, True, False, True, True], None, "Diatonic", "A")
    time.sleep(4)  # 4 seconds is the sweet spot
