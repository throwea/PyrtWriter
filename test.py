import random
import numpy as np
from mingus.core import *
from mingus.containers import Note
import Voice
import math

#TODO:
# - figure out how to transmit midi to physical score
# - figure out how to structure the notes for each part so that it is readable for the Voice class
# - find a representation for notes. Remember some notes have enharmonic representations

#global variables
soprano_range = Voice(Note("C", 4), Note("G", 5))
alto_range    = Voice(Note("G", 3), Note("C", 5))
tenor_range   = Voice(Note("C", 3), Note("G", 4))
bass_range    = Voice(Note("E", 2), Note("C", 4))

# chords = {0: "I", 1: "ii", 2: "iii", 3: "IV", 4: "V", 5: "vi", 6: "vii°"}
# L = np.array([[0, 5, 1, 6, 4, 7, 3],
#               [0, 0, 0, 0, 8, 0, 3],
#               [0, 1, 0, 1, 0, 10, 0],
#               [2, 6, 0, 0, 5, 0, 4],
#               [10, 0, 0, 0, 0, 4, 1],
#               [0, 10, 0, 6, 1, 0, 0],
#               [10, 0, 0, 0, 0, 2, 0]])
# progression = matrix_walk(L)
# for i in range(len(progression)):
#     progression[i] = chords[progression[i]]
# print(progression)

class pyrtWriter():

    def __init__(self):

        self.key = self.generate_random_key()
        self.transitionMatrix = np.array([[0, 5, 1, 6, 4, 7, 3],
              [0, 0, 0, 0, 8, 0, 3],
              [0, 1, 0, 1, 0, 10, 0],
              [2, 6, 0, 0, 5, 0, 4],
              [10, 0, 0, 0, 0, 4, 1],
              [0, 10, 0, 6, 1, 0, 0],
              [10, 0, 0, 0, 0, 2, 0]])
        self.bass_voice = []
        self.tenor_voice = []
        self.alto_voice = []
        self.soprano_voice = []

    def rand_index(self):
        rand_val = random.randint(1, sum(self.transitionMatrix))
        ind = -1
        run_sum = 0
        while run_sum < rand_val:
            ind += 1
            run_sum += self.transitionMatrix[ind]
        return ind

    def matrix_walk(self):
        steps = 7
        out_list = [0] * steps
        i = 0
        while i < (steps - 1) / 2:
            if (i + 1) != (steps - (i + 2)):
                out_list[i + 1] = self.rand_index(self.transitionMatrix[out_list[i]])  # Step forwards from beginning
                # Step backwards from end
                out_list[steps - (i + 2)] = self.rand_index(self.transitionMatrix.transpose()[out_list[steps - (i + 1)]])
            elif np.dot(self.transitionMatrix[out_list[i]], self.transitionMatrix.transpose()[out_list[steps - (i + 1)]]):  # Check for connection
                # Connect beginning and end
                out_list[i + 1] = self.rand_index(
                    np.multiply(self.transitionMatrix[out_list[i]], self.transitionMatrix.transpose()[out_list[steps - (i + 1)]]))
            else:
                # Restart if no connection
                i = 0
            i += 1
        return out_list

    def generate_random_key(self):
        val = random.randint(0, 29)
        mykey = keys.get_key((val % 15) - 7)[math.floor(val / 15)]
        self.key = mykey

    def write_harmony(self):
        """
        When we write the harmony. We want each voices notes to be stacked so that we can analyze them.
        1. We want to select a key
        2. Get all notes in that key
        3. Get all chords in that key
        4. use transition matrix to create progression
        5. Use voice and Pyrt writer to realize the chords
        :return:
        """
        notes = scales.get_notes(self.key)
        chords = chords.triads(self.key)




