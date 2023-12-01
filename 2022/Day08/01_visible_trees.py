def rowcolcheck(r,c,lt):
    flag = True
    for t in range(c-1, -1, -1):            
        if trees[r][c] <= trees[r][t]:
            flag = False
            print(f'No {t} is {flag} - LEFT')
            break
    if flag:
        print(f'No {t} is {flag}  - LEFT')
        return 1
    else:
        flag = True
    
    for t in range(c+1, lt):            
        if trees[r][c] <= trees[r][t]:
            flag = False
            print(f'No {t} is {flag} - RIGHT')
            break
    if flag:
        print(f'No {t} is {flag} - RIGHT')
        return 1
    else:
        flag = True
    
    for t in range(r-1, -1, -1):            
        if trees[r][c] <= trees[t][c]:
            flag = False
            print(f'No {t} is {flag} - UP')
            break
    if flag:
        print(f'No {t} is {flag} - UP')
        return 1
    else:
        flag = True
    
    for t in range(r+1, lt):            
        if trees[r][c] <= trees[t][c]:
            flag = False
            print(f'No {t} is {flag} - DOWN')
            break
    if flag:
        print(f'No {t} is {flag} - DOWN')
        return 1
    
    return 0

f = open('input.txt','r')

trees = []

for l in f:
    tree = list(l.strip())
    trees.append(tree)

f.close()

count = len(trees) ** 2 - (len(trees)-2) ** 2

for i in range(1,len(trees)-1):
    for j in range(1,len(trees)-1):
        count += rowcolcheck(i, j, len(trees))
        print(i,j,count)

        
print(count)