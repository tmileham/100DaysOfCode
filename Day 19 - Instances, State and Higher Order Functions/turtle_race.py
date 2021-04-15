from turtle import Turtle, Screen
from random import randint

race_entrants = [
    {"name": "tom", "color": "red"},
    {"name": "keeley", "color": "pink"},
    {"name": "chris", "color": "blue"},
    {"name": "oli", "color": "green"},
    {"name": "rodney", "color": "brown"},
]

turtle_racers = []
screen = Screen()
screen.listen()

# Creates a list of Turtle Racer Names
turtle_racer_names_list = []
for entrant in race_entrants:
    turtle_racer_names_list.append(entrant["name"])

# Creates a list of objects from the list of dicts - race_entrants
def create_turtle_object(list: list):
    """Creates object from provided list of dictionarys with 2 key-value pairs - name, color"""
    for turtle in list:
        name = turtle["name"]
        turtle["name"] = Turtle(shape="turtle")
        turtle["name"].color(turtle["color"])
        turtle["name"].name = name
        turtle["name"].penup()
        turtle_racers.append(turtle["name"])


# Call the create turtle object function to create a list of turtle objects
create_turtle_object(race_entrants)


def place_bet():
    """Display text input on screen and return input as str"""
    return screen.textinput(
        "Place your bets!",
        "Who will win the race?\nThe racers in order are \n{0}".format(
            turtle_racer_names_list
        ).title(),
    )


bet = place_bet()


def race(turtle_racers_list, bet):
    """Func starts the race and returns the winner"""
    race_in_progress = True

    def starting_grid(turtle_racers_list):
        """Function to set up the starting grid"""
        starting_grid = 100

        for racer in turtle_racers_list:
            racer.setx(-470)
            racer.sety(starting_grid)
            starting_grid -= 50

    starting_grid(turtle_racers_list)

    while race_in_progress:
        for racer in turtle_racers_list:
            racer.forward(randint(10, 30))
            x_pos = racer.xcor()
            # print(racer.xcor())
            if x_pos > 455:
                print(f"{racer.name.title()} won")
                race_in_progress = False
                return racer.name


race_winner = race(turtle_racers, bet)

# Check the race_winner against the bet variable
if race_winner.lower() == bet.lower():
    print(f"Congratulations you won! {race_winner.title()} won the race!!")
else:
    print(f"Unlucky, you lost the bet. {race_winner.title()} won the race!!")


screen.exitonclick()