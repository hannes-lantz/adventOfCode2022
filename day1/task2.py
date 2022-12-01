from pathlib import Path
txt = Path('input.txt').read_text()

items = txt.replace('\n', ' ').split("  ")
max = 0
elfbag = []
for i in items:
    bag = i.split(" ")
    res = [eval(j) for j in bag]
    elfbag.append(sum(res))
    
score = sorted(elfbag, reverse=True)[0] + sorted(elfbag, reverse=True)[1] + sorted(elfbag, reverse=True)[2]

print("Top 3 Score is: ", score)