## Functions in Python ##

# to define a function in python, you use the def keyword
# after the def keyword is the name of the function
# finally, two parenthesis come after (for arguments) and then a colon (:)

# in this example, I created the argument fav_food, and then inside the function, I'm printing a message
# for the message, i concatenate a string with the info from the argument that I get when I call the function
def main(fav_food):
    print("Your favorite food is " + fav_food)

# here, when I call the function, inside the parenthesis, I'm telling Python that the value of fav_food will be up to the user by using the input() function.
main(input("What is your favorite food? "))