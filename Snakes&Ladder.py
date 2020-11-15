
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

