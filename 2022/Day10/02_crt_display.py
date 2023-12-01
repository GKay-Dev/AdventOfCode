def crtupdate(s, c):
    if s[len(c)] == '#':
        c += '#'
    else:
        c += '.'
    return c

f = open('input.txt','r')
x = 0
sprite = '###.....................................'
crt = ''

for l in f:

    l = l.strip().split()
    
    if l[0] == 'addx':
        for i in range(2):
            if len(crt) != 40:
                crt = crtupdate(sprite, crt)
            else:
                print(crt)
                crt = ''
                crt = crtupdate(sprite, crt)
            # print(crt)
        sprite = sprite.replace('#', '.')
        x += int(l[1])

        tempsprite = list(sprite)
        for itr in range(3):
            tempsprite[(x+itr)%40] = '#'
        sprite = ''.join(tempsprite)

        # sprite = sprite[:x] + '###' + sprite[x:]
        # print(x, l[1])
        # print(f'sprite (len = {len(sprite)}): {sprite}')
    else:
        if len(crt) != 40:
            crt = crtupdate(sprite, crt)
            # print(crt)
        else:
            print(crt)
            crt = ''
            crt = crtupdate(sprite, crt)

print(crt)

f.close()