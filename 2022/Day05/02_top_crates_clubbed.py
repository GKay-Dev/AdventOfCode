f = open('input.txt','r')

stack = [['S','L','W'],['J','T','N','Q'],['S','C','H','F','J'],['T','R','M','W','N','G','B'],['T','R','L','S','D','H','Q','B'],['M','J','B','V','F','H','R','L'],['D','W','R','N','J','M'],['B','Z','T','F','H','N','D','J'],['H','L','Q','N','B','F','T']]

for i in range(10):
    f.readline()

for l in f:
    
    a, count, b, sstack, c, estack = l.strip().split()
    sstack = int(sstack) - 1
    estack = int(estack) - 1
    scount = len(stack[sstack]) - int(count)
    
    stack[estack].extend(stack[sstack][scount:])
    stack[sstack] = stack[sstack][:scount]
    # print(stack[estack], stack[sstack])

f.close()

print(stack[0][-1], stack[1][-1], stack[2][-1], stack[3][-1], stack[4][-1], stack[5][-1], stack[6][-1], stack[7][-1], stack[8][-1], sep = '')
