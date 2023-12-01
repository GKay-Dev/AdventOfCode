f = open('input.txt','r')

score = 0

for l in f:

    opponent, player = l.strip().split()

    if player == 'Z':
        if opponent == 'A':
            score += 3
        elif opponent == 'B':
            score += 9
        else:
            score += 6
    elif player == 'Y':
        if opponent == 'A':
            score += 8
        elif opponent == 'C':
            score += 2
        else:
            score += 5
    else:
        if opponent == 'B':
            score += 1
        elif opponent == 'C':
            score += 7
        else:
            score += 4

f.close()

print(score)