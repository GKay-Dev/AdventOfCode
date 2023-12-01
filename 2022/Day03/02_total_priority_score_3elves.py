f = open('input.txt','r')

score = 0

l = f.readline()
l4 = ''

while l != '':

    l1 = set(l)
    l2 = set(f.readline().strip())
    l3 = set(f.readline().strip())
    
    for elem in l1:
        if elem in l2 and elem in l3:
            if elem.isupper():
                score += ord(elem) - 38
            else:
                score += ord(elem) - 96

    l = f.readline().strip()

f.close()

print(score)