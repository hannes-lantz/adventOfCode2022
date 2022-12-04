from pathlib import Path
txt = Path('input.txt').read_text()

items = txt.split('\n')

fullycontains=0
overlaps=0
for i in items:
    pair = i.split(',')
    elf1 = pair[0].split('-')
    elf2 = pair[1].split('-')
    one = set(range(int(elf1[0]),int(elf1[1])+1))
    two = set(range(int(elf2[0]),int(elf2[1])+1))
    
    if(one.issubset(two) or two.issubset(one)):
        fullycontains += 1

    if(len(set(one).intersection(set(two))) > 0):
        overlaps += 1

print(fullycontains)
print(overlaps)