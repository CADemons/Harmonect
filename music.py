"""
music.py - handles music

Primary author: Colin Rioux (@colinrioux)
Supporting authors: Linc Berkeley (@lincb)

"""
import math, time
import numpy as np
import mingus.core.scales as scales
from mingus.midi import fluidsynth
from mingus.containers import Note
from mingus.containers import NoteContainer

fluidsynth.init("GeneralUser GS v1.471.sf2")

# def processSteps(steps, prev_state=None, sc="Diatonic", start_key="C"):
#     """
#     Play music when a person is standing on a specific step.

#     :type steps: Boolean Array
#     :param steps: an array which is mapped to the current configuration of steps.

#     :type prev_state: State
#     :param prev_state: A state or the previous state, usually returned via one call of processSteps(). Optional.

#     :type sc: String
#     :param sc: Scale name. Optional.

#     :type start_key: String
#     :param start_key: Key to start the scale. Optional.

#     :example:
#     processSteps([True,False,False,False])
#     ==> maps steps: step 1 = steps[0], step 2 = steps[1], etc etc.
#     ==> for all true steps, play a specific note

#     :returns current_state: Returns the current state of the what's playing, so you can call it again in another call of
#     processSteps.
#     """
#     current_state = State(steps, sc, start_key)
#     if (prev_state is not None):
#         prev_state.play()
#         print('Prev state:\n{0}'.format(prev_state))
#     current_state.play()
#     print('Current state:\n{0}'.format(current_state))
#     return current_state

class StepPlayer:

    """
    Stores a scale and intrument data. Able to quickly play any given step array.
    :type steps: int
    :param steps: The number of steps, corresponding to the number of possible notes.

    :type sc: String
    :param sc: Scale name. Optional.

    :example:
    ex = State([True, True, False])

    """
    def __init__(self, numSteps, scaleName="Diatonic", start_key='C'):
        self.numSteps = numSteps
        self.scaleName = scaleName
        self.start_key = start_key
        self.soundArr = self.__getSoundArr()

    def __str__(self):
        return 'Map: {0}\nScale: {1}\nStart Key: {2}'.format(self.soundArr, self.scaleName, self.start_key)

    """
    Creates an array of NoteContainers corresponding to the selected scale.
    """
    def __getSoundArr(self, startOc=4):
        tmp = []
        scl = self.__scaleArray()
        oc = startOc - 1
        firstNote = scl[0]
        for note in scl:
            if note == firstNote:
                oc += 1
            tmp.append(NoteContainer(Note(note, oc)))
        return tmp

    """
    Builds scale.

    :private:

    """
    def __buildScale(self):
        octa = int(math.ceil((self.numSteps / 7.0)))
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
            "Chromatic": scales.Chromatic(self.start_key, int(math.ceil((self.numSteps / 12.0)))),
            "WholeTone": scales.WholeTone(self.start_key, int(math.ceil((self.numSteps / 6.0)))),
            "Octatonic": scales.Octatonic(self.start_key, int(math.ceil((self.numSteps / 8.0))))
        }[self.scaleName]

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
    Plays music corresponding to the given array of steps.
    """
    def processSteps(self, steps, oldSteps=None):
        if oldSteps is not None:
            steps = getNewSteps(steps, oldSteps)
        for step, sound in zip(steps, self.soundArr):
            if step:
                fluidsynth.play_NoteContainer(sound)

    """
    Plays notes for each activiated step.

    :example:
    steps == [True, False]
    play() ==> plays "C"

    steps == [True, False, True]
    play() ==> plays "C", "E"

    """
    def play(self):
        fluidsynth.play_NoteContainer(NoteContainer(self.map))

"""
Finds the steps that are new in the current step array.

:type currentSteps: list
:param currentSteps: The current step array, such as one produced by step_detect.getStepArr

:type oldSteps: list
:param oldSteps: The old step array to subract, such as one produced by step_detect.getStepArr
"""
def getNewSteps(currentSteps, oldSteps):
    return np.logical_and(currentSteps, np.logical_not(oldSteps))

if __name__ == '__main__':
    player = StepPlayer(10, "Diatonic", "A")
    player.processSteps([True, True, False, False, False, False, True, False, True, True])
    print player
    time.sleep(4)  # 4 seconds is the sweet spot
