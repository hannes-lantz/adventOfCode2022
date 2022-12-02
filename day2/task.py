from pathlib import Path
txt = Path('input.txt').read_text()

items = txt.split('\n')

rounds = []
for i in items:
    rounds.append(i.split(" "))


score = 0
for r in rounds:
    played = r[1]
    against = r[0]
    print("Round ", r)
    if against == 'A':
        if played ==   'X':
            score +=3
            score +=0
        elif played == 'Y':
            score +=1
            score +=3
        elif played == 'Z':
            score +=2
            score +=6

        print("My score is ", score)
    elif against == 'B':
        if played ==   'X':
            score +=1
            score +=0
        elif played == 'Y':
            score +=2
            score +=3 
        elif played == 'Z':
            score +=3
            score +=6 

        print("My score is ", score)
    elif against == 'C':
        if played ==   'X':
            score +=2
            score +=0 
        elif played == 'Y':
            score +=3
            score +=3 
        elif played == 'Z':
            score +=1
            score +=6

        print("Part one ", score)

print("My score is ", score)