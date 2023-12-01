def tposupdate(hpos, tpos, pos):
    if hpos[pos] > tpos[pos]:
        tpos[pos] += 1
    elif hpos[pos] < tpos[pos]:
        tpos[pos] -= 1
    else:
        pass
    return tpos[pos]

def tposchange(hpos, tpos):    
    if hpos[0] - tpos[0] > 1:
        tpos[0] += 1
        tpos[1] = tposupdate(hpos, tpos, 1)    
    elif hpos[0] - tpos[0] < -1:
        tpos[0] -= 1
        tpos[1] = tposupdate(hpos, tpos, 1)
    else:
        pass
    if hpos[1] - tpos[1] > 1:
        tpos[1] += 1
        tpos[0] = tposupdate(hpos, tpos, 0)
    elif hpos[1] - tpos[1] < -1:
        tpos[1] -= 1
        tpos[0] = tposupdate(hpos, tpos, 0)
    else:
        pass
    return (hpos, tpos)

f = open('input.txt','r')

hpos = [0,0]
tpos = [0,0]
tset = set()

for l in f:    
    d, step = l.strip().split()
    step = int(step)
    print(d, step)
    
    for i in range(1, step+1):
        if d == 'R':
            hpos[0] += 1
            nhpos, ntpos = tposchange(hpos, tpos)
            tset.add(tuple(ntpos))
        elif d == 'L':
            hpos[0] -= 1
            nhpos, ntpos = tposchange(hpos, tpos)
            tset.add(tuple(ntpos))
        elif d == 'U':
            hpos[1] += 1
            nhpos, ntpos = tposchange(hpos, tpos)
            tset.add(tuple(ntpos))
        else:
            hpos[1] -= 1
            nhpos, ntpos = tposchange(hpos, tpos) 
            tset.add(tuple(ntpos))   
    
    print(nhpos, ntpos)

f.close()

print(f'Final Position: {nhpos} {ntpos}, and total positions occupied by tail is {len(tset)}.')
