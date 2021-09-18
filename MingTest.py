from mingus.core import *
from mingus.containers import Note
import random
import math


# Class to manage voice parts
class Voice:

    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.part = []

    def get_part(self):
        return self.part

    def append_part(self, note_):
        self.part.append(note_)

    def check_parallel(self, part2, note_):
        return True

    def check_seventh(self, note_):
        return True

    def check_consecutive(self, part2, note_):
        return True

    def check_direct(self, part2, note_):
        return True

    def check_awkward(self, note_):
        return True

    def check_tendency(self, note_):
        return True

    def check_crossing(self, part2, note_):
        return True

    def check_overlap(self, part2, note_):
        return True

    def in_range(self, note_):
        return (int(note_) <= int(self.high)) and (int(note_) >= int(self.low))

    def check_spacing(self, part2, note_):
        return True

    def check_double(self, part2, note_):
        return True


# Define the four voices and their ranges
soprano = Voice(Note("C", 4), Note("G", 5))
alto    = Voice(Note("G", 3), Note("C", 5))
tenor   = Voice(Note("C", 3), Note("G", 4))
bass    = Voice(Note("E", 2), Note("C", 4))

# Generate a Random Key
val = random.randint(0, 29)
mykey = keys.get_key((val % 15)-7)[math.floor(val/15)]
