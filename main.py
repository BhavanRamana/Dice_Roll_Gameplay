import random
def roll():
   roll = random.randint(1,6)
   return roll

while True:
    player =input("enter the num of players(1-4):")
    if player.isdigit():
        player = int(player)
        if player >=2 and player <= 4:
            break
        else:
          print(" between 2-4 players only")

    else:
        print("invalid,try again")

max_score=50
player_score=[0 for _ in range(player)]

while max(player_score)< max_score:

    for  player_id in range(player):
        print("\nplayer number", player_id + 1, "turn has just started!\n")
        current_score=0

        while True:
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":
                current_score=0
                break

            value = roll()
            if value==1:
                print("you rolled a 1! turn done!")
                current_score = 0
                break

            else:
                current_score += value
                print("you roled a:",value)

            print("your score is:", current_score)


        player_score[player_id] += current_score
        print("your total score is:",player_score[player_id])

    max_score = max(player_score)
    winning_idx = player_score.index(max_score)
    print("player number", winning_idx + 1,
          "is the winner with a score of:", max_score)

