def rowcolcheck(r,c,lt):
    count = []
    ct = 0

    for t in range(c-1, -1, -1):            
        if trees[r][c] <= trees[r][t]:
            ct += 1
            # flag = False
            # print(f'No {t} is a long tree - LEFT')
            break
        ct += 1
    count.append(ct)
    
    ct = 0
    for t in range(c+1, lt):            
        if trees[r][c] <= trees[r][t]:
            ct += 1
            # flag = False
            # print(f'No {t} is a long tree - RIGHT')
            break
        ct += 1
    count.append(ct)
    
    ct = 0
    for t in range(r-1, -1, -1):            
        if trees[r][c] <= trees[t][c]:
            ct += 1
            # flag = False
            # print(f'No {t} is a long tree - UP')
            break
        ct += 1
    count.append(ct)
    
    ct = 0
    for t in range(r+1, lt):            
        if trees[r][c] <= trees[t][c]:
            ct += 1
            # flag = False
            # print(f'No {t} is a long tree - DOWN')
            break
        ct += 1
    count.append(ct)
    
    print(count)
    
    return count[0] * count[1] * count[2] * count[3]

f = open('input.txt','r')

trees = []

for l in f:
    tree = list(l.strip())
    trees.append(tree)

f.close()

count = len(trees) ** 2 - (len(trees)-2) ** 2
max_score = 0
for i in range(1,len(trees)-1):
    for j in range(1,len(trees)-1):
        score = rowcolcheck(i, j, len(trees))
        print(i,j,score)
        if score > max_score:
            x, y = i, j
            max_score = score
        
print(x, y, max_score)