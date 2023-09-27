import tkinter as tk
import random


def montyhall(times):

    # This variable stores the number of wins after "times" number of games.
    wins = 0

    # This loop plays the game "times" number of times.
    for time in range(times):

        # This list represents the doors that can be opened by the contestant or the game host.
        doors = [0, 0, 0]

        # This list represents the choices the contestant can make.
        # They can open 0 (1st), 1 (2nd), or 2 (3rd) door.
        selections = [0, 1, 2]

        # The position of the car is randomly decided.
        car_position = random.randint(0, 2)

        # The car is then spawned behind that door.
        # The 0's in the doors list represent the goats while 1 represents the car.
        doors[car_position] = 1

        # The contestant chooses a door at random.
        contestant_door = random.choice(selections)

        # Contestant's door is then removed from the list of possible selections.
        # i.e. it can not be chosen/selected by the host.
        selections.remove(contestant_door)

        # This loop goes through the remaining available selections and opens the door with a goat behind it.
        for door in selections:
            # If selection has a goat behind it.
            if doors[door] == 0:
                # Remove/Open that door/selection.
                selections.remove(door)
                break

        # Now that the contestant's initial selection and a goat has been removed from the possible selections,
        # The contestant selects the only available door.
        contestant_door = selections[0]

        # If there is a car (1) in contestant's final choice
        if doors[contestant_door] == 1:
            # Increase the number of wins by 1.
            wins += 1

    # Return the final number of wins as the function's value.
    return wins


# Calculates the win percentage out of 1000 games.
win_percentage = montyhall(1000) * 100 / 1000

# Creates a window with TKinter
window = tk.Tk()

# Creates a Label Element to display in the window and displays the win percentage.
information = tk.Label(
    text=win_percentage,
    width=20,
    height=6
)

# Packs or places the information label in the window.
information.pack()
# Loops the window until it is closed.
window.mainloop()
