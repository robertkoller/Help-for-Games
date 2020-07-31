import time
import random
fire = False
x = 0
y= 0
while x < 3 and y < 3:
    print ("hello there i am you imagniary friend named cosmo.")
    print("i am here because you have washed ashore on this deserted island. You seem to have no memmories of your past.")
    print("well since we are on a island alone we should start working to survive.")
    choice1 = input("what should we do first. We can make a fire, work on making a small shelter, or start making tools. Say tools, fire, or shelter")
    
    #you are trying to exit the function if someone does not have a fire within 3 days
    #every day you go without a fire it should add 1 to x and when x is 3 you die. When
    # there is a fire then x turns to 0
    if choice1 == "fire":
        print("to make a fire you have to find sticks and green branches. you will need 5 wood.")
        firego = input("where do you want to go and gather wood? There are 6 places on the island, these places are shipwreck, stickplace, treeplace, mountains, pondplace, and huntinggrounds. Shipwreck, treeplace, and huntinggrouds aren't usable yet because you need equipment. Do you want to go to mountains, pondplace, or stickplace. Mtns has lots of rock, podplace water, and stickplace wood. Type where you want to go. mountains, pondplace, or stickplace.")
        if firego == "stickplace":
            gather = random.randint(4,10)
            wood = 0
            wood = gather
            print("You have collected",gather,"wood pieces")
            if wood >= 5:
                print("you have enough wood to make a fire. You used your 5 wood for it and now have 5 less.")
                wood = wood - 5
                x=0
                fire = True
                print("your return to your starting point and make a fire. This keeps you warm through the night and you have a good nights rest")
            else:
                x = x+1
                fire = False
                print("you did not gather enough wood. You have",wood,"wood while you needed 5 pieces.")
                print("your return to where you started and sleep uncomftrably in the night. Sleeping without a fire for 3 days straight will kill you from hypothermia")
        else :
            print("you through",firego,"and found 0 wood and then went back to your starting place. You slept uncomtrably without a fire. Just saying this is your first day without a fire if you go on without 2 more days of fire, so 3 days in total then you will die because of natural causes.")
        y=y+1
        
        print("okay you woke up and got ready for your second day in the wilderness.")
        if fire == True:
            print("okay you already made a fire so you will not need one for 3 days. Now you should focus on finding food and water.")
            print("you cannot hunt since you need tools and making tools requires time that right now you do not have. You 2 options are to go find water since you will dehydrate and die in 2 days or to go find some more wood so that you can hold water with a basket or have more wood just in case.")
            des1 = input("would you like to go and get wood or go drink from the lake at pondplace? FYI the water is okay for you to drink. Just know that if you go to pondplace you will consume 3 water from the pond and then go back but if you use wood to make a satch you can carry 3 water. Getting a satch will cost you 3 wood. Answer by saying water or wood")
            if des1 == "wood": #this is where we see where ther person will go for the second day 
                gather = random.randint(4,11)
                wood = gather + wood
                print("You got ",gather," wood from your journey and currently have ",wood,"wood.")
                ques1 = input(" Would you like to get a satch for 3 wood or save your wood for later. Remeber that if tommorow you don't get water you will die but you don't need a satch to get water. Answer by typing save or satch")
                if ques1 == "satch":
                    wood = wood -3
                    satchcount = 1
                    print("you now have a satch and ",wood,"wood")
                else:
                    print("okay didn't get a satch")
            else: #this is the option if you are to go to get water
                print("you got to pondplace and drank the water and felt refreshed. You now again have 3 days untill you dehydrate. Getting a satch will get you to keep water at home so you can use it whenever you want.")
                y = 0
                if wood >= 3:
                    print("you have",wood,"wood.")
                    ques1 = input("would you like a satch it will cost you 3 wood you can get it today if you want to. Answer by saying yes or no")
                    if ques1 == "yes":
                        satchcount = 1
                        wood = wood-3
                        print("okay you lost 3 wood and still have ",wood," left but you now have a satch so the next time you go for water you will be able to take some water back and next time not use 1 day for going to drink water.")
                    else:
                        print("you didn't get a satch and still have",wood," wood.")
                else:
                    print("sorry you don't have enough wood for a satch")
            if des1 == "wood":
                print("your second day has finished, you will die tommorom if you do not drink some water so that is really important")
                x=x+1
                y=y+1
            else:
                print("your second day has finished and you have drank water you go to sleep and sleep well")
                x = x+1
                y = 0

        else:
            print("today you are going to pondplace for water or stickplace for wood needed to get a fire. If you have enough wood then you can you can get a satch which wil save you 3 water for later. One satch costs 5 wood.")
        print("This is your second day on this deserted island. If you have not drunken water or had a fire at all then tommorrow you will be dead!!!")
        if y == 2:
            print("you need water fast or else you will die do you want to go to pondplace to drink water?")
            go_question = input("yes or no to if you want to go to pondplace.")
            if go_question == "yes":
                print("okay you went to pondplace and drank water. You feel refreshed and ready for action.")
                if wood > 2:
                    satchques = input("do you want a satch? It will get it so that if you have one when you are at pondplace you will fill it up and when you are thirsty you will not need to use a day going to pondplace but instead use water from the satch? They cost 3 wood say yes or no")
                    if satchques == "yes":
                        satchcount = satcount + 1
                        wood = wood - 3
                        print("good job you now have a satch.")
                if satchcount == 1:
                    print("you have a satch so you collect water in it. Next time you need water you will not have to travel and have the water with you at home.")
                    satchcount = satcount - 1
                    fullsatch = fullsatch + 1
                
print("you have died")
