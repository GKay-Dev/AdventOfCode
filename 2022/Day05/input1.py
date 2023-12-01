import pandas as pd

f = open('input1.txt','r')

# pd.read_csv('input1.txt', sep=' ')

for l in f:
    l = l.replace('   ', '[a] ')
    l = l.replace('     ', '[a] [')
    # l = l.strip().split()
    print(l)

f.close()