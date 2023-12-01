f = open('input.txt','r')

score = 0

for l in f:

    l = l.strip()
    l1 = set(l[:len(l)//2])
    l2 = set(l[len(l)//2:])

    for elem in l1:
        if elem in l2:
            if elem.isupper():
                score += ord(elem) - 38
            else:
                score += ord(elem) - 96

f.close()

print(score)