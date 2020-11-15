
# Player information and input
def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Please enter your correct name player-1: ").strip()

    player2_name = None
    while not player2_name:
        player2_name = input("Please enter your correct name player-2: ").strip()

    print("\nMatch will be played between '" + player1_name + "' and '" + player2_name + "'\n")
    return player1_name, player2_name

# number displayed on dice
def get_dice_value():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    dice_value = random.randint(1, DICE_FACE)
    print("You got  " + str(dice_value))
    return dice_value 

# Module for snake bite
def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
    print("\n" + player_name + " You Got Bittttennn🐍🐍🐍🐍 Slipped from " + str(old_value) + " to " + str(current_value))

# Module to climb ladder
def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))

# Player increment from one place to the other
def snake_ladder(player_name, current_value, dice_value):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > MAX_VAL:
        print("You need " + str(MAX_VAL - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value

# Condition for winning
def check_win(player_name, position):
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    if MAX_VAL == position:
        print("\n\n\Thats it.\n\n" + player_name + " You dodged all the snakes")
        print("!!!!...YOU WON..!!! " + player_name)
        sys.exit(1)    





