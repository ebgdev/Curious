import turtle
import random

# Set up the turtle window
wn = turtle.Screen()
wn.setup(width=300, height=300)
wn.title("Coin Toss Game")
wn.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, 0)

# Define the function to simulate the coin toss
def coin_toss():
    # Randomly generate a number between 0 and 1
    num = random.randint(0, 1)
    if num == 0:
        result = "Heads"
    else:
        result = "Tails"
    return result

# Play the game
for i in range(20):
    # Simulate a coin toss
    result = coin_toss()

    # Display the result graphically
    t.color("white")
    t.write(result, align="center", font=("Arial", 36, "bold"))
    if i != 19:
        t.clear()

# Close the turtle window
wn.mainloop()
