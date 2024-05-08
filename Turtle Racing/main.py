import turtle
import random

WIDTH, HEIGHT = 500, 500
COLOURS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racers():
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print('Number not in range 2 - 10. Try again!')
        else:
            print('Input is not numeric. Try Again!')


def race(colours):
    turtles = create_turtles(colours)

    while True:
        for i, racer in enumerate(turtles):
            distance = random.randrange(1, 5)  # Adjusted distance range
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return i


def create_turtles(colours):
    turtles = []
    spacingx = WIDTH // (len(colours) + 1)
    for i, colour in enumerate(colours):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')
    screen.resizable(False, False)  # Prevent window resizing
    return screen  # Return the screen object


racers = get_number_of_racers()
screen = init_turtle()  # Get the screen object

random.shuffle(COLOURS)
colours = COLOURS[:racers]

winner_index = race(colours)
print(f"The winner was racer {winner_index + 1} with color: {colours[winner_index]}")

screen.mainloop()  # Keep the window open
