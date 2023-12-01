f = open('input.txt','r')

count = 0
max_count = [0,0,0]
mc_len = len(max_count)

for l in f:
    if l.strip() != '':
        count += int(l)
    else:
        for i in range(mc_len):
            if count > max_count[i]:
                max_count.insert(i, count)
                max_count = max_count[:mc_len]
                break
        count = 0

f.close()

print(sum(max_count))