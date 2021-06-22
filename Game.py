def game():
    print("Your adventure starts in the dark, gloomy streets of Hazanberg. This city is known for their advancements in nuclear technology.")
    print("Except today isn't any day, one of the larger nuclear plants has exploded. The radiation left from it causes the city to be uninhabitable.")
    print("The streets are stacked, and the radiation is causing the people to change into horrifying amalgams, they consume any living thing in their path.")
    print("Everyone who was able to get out has made it out safely and you're the only human left. You don't know but you seem to be immune to the radiation.")
    print(" ")
    print("Type 1 to choose the left option, type 2 for the right, and 3 if applicable.")
    print(" ")
    while True:
        leave = input("Do you leave the house, or no? ")
        if leave == "2":
            print("The amalgamations have sensed you, they break into the house and eat you alive. GAME OVER.")
            return False
        else:
            print("You take a baseball bat, food, and water in a backpack. You leave the house at day.")
        print("You start walking and soon you see.")
        print(" ")
        dire = input("There is a group of amalgams if front of you rushing at you, do you go left or right to escape? ")
        if dire == "1":
            print(" ")
            supermarket = input("You go left and see a supermarket, do you loot it or continue moving?")
            if supermarket == "1":
                print("You found the Blade of Shurima, you can now kill higher level amalgams.")
                backleft = input("Do you want to go back or continue moving?")
        else:
            rightamal = input("You go right and see a small group of amalgams, glowing red, do you fight or run?")
            if rightamal == "1":
                print("These are stronger amalgams, they tore you to shreds. GAME OVER.")
                return False
            else:
                back = input("These amalgams are too strong, stronger than the others. You decide to run back to the cross, and go left.")

class Solution:
    game()