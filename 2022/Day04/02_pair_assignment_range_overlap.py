f = open('input.txt','r')

count = 0

for l in f:

    a, b = l.strip().split(',')
    astart, aend = map(int, a.split('-'))
    bstart, bend = map(int, b.split('-'))

    if bstart <= astart <= bend or bstart <= aend <= bend or astart <= bstart <= aend or astart <= bend <= aend:
        count += 1

f.close()

print(count)