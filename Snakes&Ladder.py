import sys
import random
import time

TIME_LAPSE = 2
WIN_NUM = 100
DICE_FACE = 6

# ladder takes you up
ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

# snake takes you down
snakes = {
    98: 78,
    95: 75,
    93: 73,
    87: 24,
    64: 60,
    62: 19,
    56: 53,
    49: 11,
    48: 26,
    16: 6
}

player_turn_text = [
    "Your turn, roll on the dice.!!",
    "C'mon..let's roll the dice.!!",
    "Don't make others wait...roll.!!",
    "Lets roll.!!!",
    "",
]

snake_bite = [
    "bummer",
    "hisss....snake bite",
    "oh nooooo",
    "dang"
]

climb_ladder = [
    "woohoo",
    "wow",
    "nailed it",
    "yeah..."
]


def intro():
    msg = """
    Welcome to the Text-based Snakes and Ladder Game

    1. Enter your names as prompted by the game.
    2. Press ENTER key to roll the dice.
    3. Ladder helps you to go up while snake will pull you down.
    4. The first player to get to reach 100 is the winner.
    """
    print(msg)


# Player information and input
def get_player_names():
    player1_name = None
    while not player1_name:
        player1_name = input("Pls enter your correct name player-1: ").strip()
        input("Press enter to continue")

    player2_name = None
    while not player2_name:
        player2_name = input("Pls enter your correct name player-2: ").strip()
        input("Press enter to continue")

    return player1_name, player2_name


# number displayed on dice
def get_dice_value():
    time.sleep(TIME_LAPSE)
    dice_value = random.randint(1, DICE_FACE)
    print("You got  " + str(dice_value))
    return dice_value


# Module for snake bite
def got_snake_bite(prev_value, current_value, player_name):
    print("\n" + random.choice(snake_bite).upper() + " Hissssssss")
    print("\n" + player_name + "You Got Bitten Slipped from" +
          str(prev_value) + "to" + str(current_value))


# Module to climb ladder
def got_climb_ladder(prev_value, current_value, player_name):
    print("\n" + random.choice(climb_ladder).upper() + " _/ _/ _/ _/")
    print("\n" + player_name + "climbed the ladder from" +
          str(prev_value) + "to" + str(current_value))


# Player increment from one place to the other
def snake_ladder(player_name, current_value, dice_value):
    time.sleep(TIME_LAPSE)
    prev_value = current_value
    current_value = current_value + dice_value

    if current_value > WIN_NUM:
        print("You need " + str(WIN_NUM - prev_value) + " to Win .")
        return prev_value

    print("\n" + player_name + " moved from " + str(prev_value) + " to " + str
          (current_value))
    if current_value in snakes:
        final_value = snakes.get(current_value)
        got_snake_bite(current_value, final_value, player_name)

    elif current_value in ladders:
        final_value = ladders.get(current_value)
        got_climb_ladder(current_value, final_value, player_name)

    else:
        final_value = current_value

    return final_value


# Condition for winning
def check_win(player_name, position):
    time.sleep(TIME_LAPSE)
    if WIN_NUM == position:
        print("\n\nThats it\n\n" + player_name + "You dodged all the snakes")
        print("!!!!...YOU WON..!!!" + player_name)
        sys.exit(1)


def start():
    print()
    intro()
    time.sleep(TIME_LAPSE)
    player1_name, player2_name = get_player_names()
    time.sleep(TIME_LAPSE)
    # intro()
    # time.sleep(TIME_LAPSE)

    player1_current_position = 0
    player2_current_position = 0

    while True:
        time.sleep(TIME_LAPSE)
        input_1 = input("\n" + player1_name + ": " + random.choice(player_turn_text) + " Press ENTER to Roll the Dice ")# noqa
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(TIME_LAPSE)
        print(player1_name + " moving....")
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value) # noqa

        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ") # noqa
        print("\nRolling dice...")
        dice_value = get_dice_value()
        time.sleep(TIME_LAPSE)
        print(player2_name + " moving....")
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value) # noqa

        check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    start()
