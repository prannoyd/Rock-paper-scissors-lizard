# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    if(name=='rock'):
        num=0
    elif(name=='Spock'):
        num=1
    elif(name=='paper'):
         num=2
    elif(name=='lizard'):
         num=3
    elif(name=='scissors'):
         num=4
    else:
         print "err"
    return num
        


    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    if(number==0):
        name='rock'
    elif(number==1):
        name='Spock'
    elif(number==2):
         name='paper'
    elif(number==3):
        name='lizard'
    elif(number==4):
         name='scissors'
    else:
         print "err"
    return name
    # delete the following pass statement and fill in your code below
    pass
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    print"---------------------------"
    print "You chose "+player_choice
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0, 4)
    comp_choice=number_to_name(comp_number)
    print 'The computer chose '+comp_choice
    diff=(player_number-comp_number)%5

    if(diff ==1 or diff==2):
        print "You won!"
    elif(diff ==3 or diff==4):
        print "You Lost!"
    else:
        print "You tied!"
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


