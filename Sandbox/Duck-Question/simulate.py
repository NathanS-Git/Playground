import random

runs = 100_000
successes = 0
n = 6

for run in range(runs):
    ducks = []
    for _ in range(n):
        ducks.append((random.random(),random.random()))

    all_false_1 = True
    all_true_1 = True

    all_false_2 = True
    all_true_2 = True

    for d_x,d_y in ducks:
        if d_x+d_y < 1:
            all_false_1 = False
        else:
            all_true_1 = False

        if d_y-d_x < 0:
            all_false_2 = False
        else:
            all_true_2 = False

    if any((all_false_1,all_true_1,all_false_2,all_false_2)):
        successes += 1

print(runs,successes,successes/runs)
