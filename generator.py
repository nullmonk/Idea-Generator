import sys, random

def read(filename):
    words = {}
    with open(filename) as inf:
        lines = inf.readlines()
        i = 0
        choices = ["verb", "adjective1", "adjective2", "noun", "ending"]
        for c in choices:
            words[c] = []
        for l in lines:
            l = l.strip()
            if l == "":
                continue
            if l == "++" and i < len(choices):
                i+=1
                continue
            elif i >= len(choices):
                print("Done")
                break
            words[choices[i]] += [l]
    return words

def generate(words):
    output = ""
    output += random.choice(words["verb"]) +" "

    if random.randint(1,7) == 1:
        output += random.choice(words["adjective1"]) +" "

    output += random.choice(words["adjective2"]) +" "
    output += random.choice(words["noun"]) +" "
    if random.randint(1,9) == 1:
        output += random.choice(words["ending"])
    return output



if len(sys.argv) < 2:
    filename = "wordlist.txt"
else:
    filename = sys.argv[1]
    
words = read(filename)

if len(sys.argv) > 2:
    try:
        count = int(sys.argv[2])
    except:
        pass
else:
    count = 2

for i in range(count):
    print(generate(words))
