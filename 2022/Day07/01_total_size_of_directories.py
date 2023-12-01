def filestruct(drtry):
    dd = {}
    d = drtry
    dd[d] = 0

f = open('input.txt','r')
dirsize = {}
dirsizesum = 0
# f.readline()

for l in f:
    cmd = l.strip().split()
    if 'ls' in cmd or '..' in cmd:
        continue
    elif 'cd' in cmd:
        drtry = cmd[2]
        dirsize[drtry] = 0
    elif cmd[0] == 'dir':
        dirsize[drtry] = dict(cmd[1])
        dirsize[drtry][cmd[1]] = 0
    else:
        dirsize[drtry] += int(cmd[0])
f.close()

for k,v in dirsize.items():
    if v <= 100000:
        dirsizesum += v

print(dirsizesum)