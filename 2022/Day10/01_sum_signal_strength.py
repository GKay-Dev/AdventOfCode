f = open('input.txt','r')
x = 1
cycle = 0
sigstr = 0
flag20 = flag60 = flag100 = flag140 = flag180 = flag220 = True
# i = 0

for l in f:
    
    l = l.strip().split()
    
    if l[0] == 'addx':
        cycle += 2
    else:
        cycle += 1
    
    if cycle >= 20 and flag20:
        sigstr += 20 * x
        flag20 = False
    elif cycle >= 60 and flag60:
        sigstr += 60 * x
        flag60 = False
    elif cycle >= 100 and flag100:
        sigstr += 100 * x
        flag100 = False
    elif cycle >= 140 and flag140:
        sigstr += 140 * x
        flag140 = False
    elif cycle >= 180 and flag180:
        sigstr += 180 * x
        flag180 = False
    elif cycle >= 220 and flag220:
        sigstr += 220 * x
        flag220 = False
    else:
        pass

    if len(l) > 1:
        xincr = int(l[1])
        x += xincr
    
    # i += 1
    # print(i, cycle, x, sigstr)

f.close()

print(sigstr)