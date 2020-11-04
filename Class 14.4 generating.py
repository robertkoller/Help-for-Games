import random

def generate(lenWord):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    newWord = ""
    for c in range(lenWord):
        newWord = newWord + alphabet[random.randrange(27)]
    return newWord

def score(newWord,originalWord):
    b = 0
    for x in range(len(originalWord)):
        if originalWord[x] == newWord[x]:
            b = b + 1
    return int(b/len(newWord)*100)

def check(score):
    if score == 100:
        return True
    else:
        return False


l1 = []
x = "rob"
b = generate(len(x))
c = score(b,x)
ac = 1
while check(c) == False:
    if l1.get(b) == None:
        l1.append(b)
    else:
        print(str(c) + " " + b)
    b = generate(len(x))
    c = score(b,x)
    ac = ac + 1
    
print(str(c) + " " + b)
print("that worked after ",ac,"tries.")

    
            
    
            
        
    
