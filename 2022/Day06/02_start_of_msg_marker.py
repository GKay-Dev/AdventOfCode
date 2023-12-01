f = open('input.txt','r')

l = f.readline()

f.close()

for i in range(len(l)-13):
    
    flag = True
    ll = l[i:i+14]
    
    for elem in ll:
        if ll.count(elem) > 1:
            flag = False
            break
    if flag:
        break

print(i+14)