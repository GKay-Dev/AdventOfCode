f = open('input.txt','r')

count = 0
max_count = 0

for l in f:
    if l.strip() != '':
        count += int(l)
        if count > max_count:
            max_count = count
    else:
        count = 0

f.close()

print(max_count)