def parse():
    with open("beemoviescript.txt", "r") as f:
        lines = f.readlines()
        allofit = "".join(lines)
        words = allofit.replace("\n", "")
        # print(words)
        return words

def analyze(words):
    vals = list()
    cur = 0
    while cur < len(words):
        vals.append(ord(words[cur]))
        cur += ord(words[cur])
    print(vals)
    

analyze(parse())
