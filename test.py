import random
import numpy as np

chords = {0: "I", 1: "ii", 2: "iii", 3: "IV", 4: "V", 5: "vi", 6: "vii°"}

L = np.array([[0, 5, 1, 6, 4, 7, 3],
              [0, 0, 0, 0, 8, 0, 3],
              [0, 1, 0, 1, 0, 10, 0],
              [2, 6, 0, 0, 5, 0, 4],
              [10, 0, 0, 0, 0, 4, 1],
              [0, 10, 0, 6, 1, 0, 0],
              [10, 0, 0, 0, 0, 2, 0]])


def rand_index(list_):
    rand_val = random.randint(1, sum(list_))
    ind = -1
    run_sum = 0
    while run_sum < rand_val:
        ind += 1
        run_sum += list_[ind]
    return ind


def matrix_walk(list_):
    steps = 7
    out_list = [0] * steps
    i = 0
    while i < (steps - 1) / 2:
        if (i + 1) != (steps - (i + 2)):
            out_list[i + 1] = rand_index(list_[out_list[i]])  # Step forwards from beginning
            # Step backwards from end
            out_list[steps - (i + 2)] = rand_index(list_.transpose()[out_list[steps - (i + 1)]])
        elif np.dot(list_[out_list[i]], list_.transpose()[out_list[steps - (i + 1)]]):  # Check for connection
            # Connect beginning and end
            out_list[i + 1] = rand_index(np.multiply(list_[out_list[i]], list_.transpose()[out_list[steps - (i + 1)]]))
        else:
            # Restart if no connection
            i = 0
        i += 1
    return out_list


progression = matrix_walk(L)
for i in range(len(progression)):
    progression[i] = chords[progression[i]]
print(progression)
