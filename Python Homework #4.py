b = input("Tell me a word and see who can make as many substrings as they can. ")
print("please dont repeat a substring that you have already used.")
nn = 1
lis = []
counter3 = 0
z = 0
i = 1
counter = 0
print("you are trying to create as many substrings that start with an consonants.")
#use lists to make not repeat the same thing
while i == 1:
    x = input("start making substrings. ")
    lis.append(x)
    
    for q in range(len(lis)):
        #cant get it to repeat, help needed
        if lis[q] == x:
            print("You already put that now you will restart")
            counter3 = counter3 + 1
            print (len(lis))
            
    if counter3 == 3:
        continue
    print("")
    if x[0] == "a" or x[0] == "e" or x[0] == "i" or x[0] == "o" or x[0] == "u":
        print("That starts with a vowel!")
    else:
        z = z + 1
        bb = b.count(x)
        counter = counter + bb
    ii = input("Do you want to keep adding substrings? If yes then press enter if not press 0 then enter. ")
    print("")
    if ii == "0":
        i = 0
print("You have",counter,"points.")


z = 0
print("okay now it is the other players turn.")
print("you are trying to print only vowels now")
counter2 = 0
while nn == 1:
    x = input("start making substrings. ")
    print("")
    if x[0] == "a" or x[0] == "e" or x[0] == "i" or x[0] == "o" or x[0] == "u":
        z = z+1
        bb = b.count(x)
        counter2 = counter2 + bb
        if x == "ana":
            counter2  = counter2 + 1
    else:
        print("that starts with a consonants.")
    vv = input("Do you want to keep adding substrings? If yes then press enter if not press 0 then enter. ")
    print("")
    if vv == "0":
        nn = 0
print("Player 2 has",counter2,"points.")
    
    

if counter2 < counter:
    print("Player 1 wins with",counter," points while Player 2 only had",counter2," points!")
elif counter == counter2:
    print("you both have",counter," points and are tied.")
else:
    print("Player 2 wins with",counter2," points while Player 2 only had",counter," points!")
