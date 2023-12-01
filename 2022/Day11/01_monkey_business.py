f = open('input.txt','r')
monkey = {}
monkey_inspect = {}
count = 20

# l = f.readline()
for l in f:
    if 'Monkey' in l:
        num = l.strip().split()[-1][0]
        monkey[num] = []
    elif 'Starting' in l:
        item = l.strip().split(', ')
        item[0] = item[0].split()[-1]
        monkey[num].extend([int(elem) for elem in item])
    else:
        pass

while count != 0:
    f.seek(0)
    num = '0'
    for l in f:
        if 'Operation' in l:
            print(f'Monkey {num}: {monkey[num]}')
            op = l.strip().split('= ')[-1]
            print(f'Operation: {op}')
            l = f.readline()
            test = int(l.strip().split()[-1])
            print(f'Test: Divisible by {test}')
            l = f.readline()
            tnewnum = l.strip().split()[-1]
            print(f'If True: throw to {tnewnum}')
            l = f.readline()
            fnewnum = l.strip().split()[-1]
            print(f'If false: throw to {fnewnum}')
            new_wrylvl = 0
            monkey_copy = monkey[num].copy()
            if count > (20 - len(monkey)):
                monkey_inspect[num] = 0
            i = 1
            for elem in monkey_copy:
                monkey_inspect[num] += 1
                old = int(elem)
                new = eval(op)
                print(f'After Operation: {new}')
                new_wrylvl = new // 3
                print(f'Monkey bored: {new_wrylvl}')
                if new_wrylvl % test == 0:
                    monkey[tnewnum].append(new_wrylvl)
                    monkey[num].pop(monkey[num].index(elem))
                else:
                    monkey[fnewnum].append(new_wrylvl)
                    monkey[num].pop(monkey[num].index(elem))
                print(f'After iteration {i}: {monkey}')
                i += 1
            print(f'After Inspection: {monkey}')
            print(f'Inspection Count: {monkey_inspect}')
            num = str(int(num)+1)
        else:
            pass

f.close()

print(monkey)
print(monkey_inspect)

inspect_count = list(monkey_inspect.values())
inspect_count.sort(reverse=True)
print(inspect_count[0] * inspect_count[1])