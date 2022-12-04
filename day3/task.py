from pathlib import Path
txt = Path('input.txt').read_text()

items = txt.split('\n')

def str2num(s):
        res=[]
        for i in s:
            if i.islower():
                res.append(ord(i)-96)
            else:
                    res.append(ord(i)-65+27)
        return ''.join('%02d'%i for i in res)

def slice_per(source, step):
    return [source[i:i+step] for i in range(0,len(source),step)]

score = []
for i in items:
    n = len(i)
    if n%2 == 0:
        c1 = i[0:n//2]
        c2 = i[n//2:]
        #print("First Half of String:",c1)
        #print("Second Half of String:",c2)
    else:
        c1 = i[0:(n//2+1)]
        c2 = i[(n//2+1):]
        #print("First Half of String:",c1)
        #print("Second Half of String:",c2)

    same = []
    for a in c1:
        for b in c2:
            if a == b:
                same.append(a)

    score.append(int(str2num(same[0])))


print("part1 ", sum(score))

x = []
groups = slice_per(items, 3)

for g in groups:
    same = []
    for a in g[0]:
        if a in g[1] and a in g[2]:
            same.append(a)
    
    x.append(int(str2num(same[0])))

print("part2 ", sum(x))
    
