from random import randint
alive = True
stamina = 10
def report(stamina):
    move=randint(0,9)
    print(move)
    if stamina>8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina>5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina>3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina>0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
def fight(stam): 
    while stam > 0:
      # won't enter this loop ever. The function will always return False.
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
        # chose a response from ( hit, attack, fight and run)
        # fight scene
        if "hit" in response or "attack" in response:
            less = randint(0, stam)
            stam -= less # subtract random int from stamina
            report(stam) 
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            return False
    return True

print ("A threatening alien wants to fight you!\n")
alive=fight(stamina)
if alive==True:
    print("the alien lives no and you, you sadly do not")
else:
    print("the alien has been vanquished. Good work")
    