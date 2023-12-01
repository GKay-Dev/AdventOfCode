f = open('input.txt','r')

score = 0

for l in f:

    opponent, result = l.strip().split()

    if opponent == 'A':
        if result == 'X':
            score += 3
        elif result == 'Y':
            score += 4
        else:
            score += 8
    elif opponent == 'B':
        if result == 'X':
            score += 1
        elif result == 'Y':
            score += 5
        else:
            score += 9
    else:
        if result == 'X':
            score += 2
        elif result == 'Y':
            score += 6
        else:
            score += 7

f.close()

print(score)