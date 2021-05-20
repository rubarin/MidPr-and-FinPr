import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    
gamecount = 0
wincount = 0
losecount = 0
rollcount = 0
win_roll = {1: 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0, 25 : 0}
loss_roll = {1:0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0,  25 : 0}

while gamecount != 100:
    rollcount = 0
    die_values = roll_dice()
    rollcount +=1  # first roll
    display_dice(die_values)

# determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    if sum_of_dice in (7, 11):
        if rollcount in win_roll:
            wincount += 1
            gamecount += 1
            win_roll[rollcount] += 1
            game_status = 'WON'
        else:
            win_roll[rollcount] = 1
    elif sum_of_dice in (2, 3, 12):
        if rollcount in loss_roll:
            losecount += 1
            gamecount += 1
            loss_roll[rollcount] += 1
            game_status = 'LOST'
        else:
            loss_roll[rollcount] = 1
        
    else:  # remember point
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        

# continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        rollcount += 1
        display_dice(die_values)
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:
            if rollcount in win_roll:# win by making point
                game_status = 'WON'
                wincount += 1
                win_roll[rollcount] += 1
                gamecount += 1
            else:
                win_roll[rollcount] = 1
        elif sum_of_dice == 7:
            if rollcount in win_roll:# lose by rolling 7
                game_status = 'LOST'
                losecount += 1
                loss_roll[rollcount] += 1
                gamecount += 1
            else:
                loss_roll[rollcount] = 1
        

print(f' Percentage of wins:', ((wincount / gamecount)*100))
print(f' Percentage of losses:', ((losecount / gamecount)*100))

d3 = {k: round(((win_roll[k]+loss_roll[k])/gamecount)*100) for k in win_roll.keys() & loss_roll}
print("Rolls\t% Resolved on this roll")
for i in d3:
    print("{}\t{}".format(i,d3[i]))
