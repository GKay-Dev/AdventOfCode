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

f = open('test_input_2.txt','r')

hpos = [0,0]
tpos = [[0,0]] * 9
ntpos = [[0,0]] * 9
# fhpos = [0,0]
# ftpos = [0,0]
tset = set()

for l in f:    
    d, step = l.strip().split()
    step = int(step)
    print(d, step)
    
    for i in range(1, step+1):
        if d == 'R':
            hpos[0] += 1
            # nhpos = hpos
            for j in range(len(tpos)):
                # if fhpos != nhpos or ftpos != ntpos:
                #     fhpos = nhpos
                #     ftpos = ntpos
                # nhpos, ntpos = tposchange(nhpos, tpos[j])
                nhpos, ntpos[j] = tposchange(hpos, tpos[j])
                # print(nhpos, ntpos[j])
            tset.add(tuple(ntpos[8]))
        elif d == 'L':
            hpos[0] -= 1
            for j in range(len(tpos)):
                nhpos, ntpos[j] = tposchange(hpos, tpos[j])
                # print(nhpos, ntpos[j])
            tset.add(tuple(ntpos[8]))
        elif d == 'U':
            hpos[1] += 1
            for j in range(len(tpos)):
                nhpos, ntpos[j] = tposchange(hpos, tpos[j])
                # print(nhpos, ntpos[j])
            tset.add(tuple(ntpos[8]))
        else:
            hpos[1] -= 1
            for j in range(len(tpos)):
                nhpos, ntpos[j] = tposchange(hpos, tpos[j])
                # print(nhpos, ntpos[j])
            tset.add(tuple(ntpos[8]))   
    
    print(nhpos, ntpos)

f.close()

print(f'Final Position: {nhpos} {ntpos}, and total positions occupied by tail is {len(tset)}.')
