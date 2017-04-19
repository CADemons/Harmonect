# music.py - 
import math
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
	current_state = State(steps)

	# while loop so it continues to play via current state definied by an initialization of a state object.
	
	#fluidsynth.init("GeneralUser GS v1.471.sf2")
	print(current_state.map)
	#print(scales.Diatonic("C", (3, 7), 2))

	#fluidsynth.play_Note(Note("C"))
	current_state.play()
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
		for x in range(0, len(self.steps)-1):
			tmp.append(dia.ascending()[x])
		return tmp

	"""
	Maps notes to the drawn map.

	:private:
	"""

	def __mapNotes(self, oc=4):
		tmp = []
		m = self.__drawMap()
		for x in range(0, len(m)-1):
			if (x % 7 == 0 and x != 0):
				oc += 1
			tmp.append(Note(m[x], oc))
		return tmp

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



processSteps([True,False,False,False,False,False,False,True,False,True])
#print(notes.int_to_note(9))