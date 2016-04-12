# your code goes here
import sys
from random import randint
filename = sys.argv[1]


def build_restaurant_dict(filename):
    """Prints the ratings of each restaurant in passed file.

       Format of passed file should have each restaurant and score
       seperated by a colon on an individual line.
       E.g. Restaurant Name:score
    """
    log_file = open(filename)
    
    restaurant_scores = {}

    # Iterate through each line in log_file to determine the restaurant
    # and its corresponding score. Adds the restaurant as a key to the
    # restaurant_scores dictionary, with the score as the value.
    for line in log_file:
        clean_line = line.rstrip()
        tokens = clean_line.split(":")
        restaurant, score = tokens
        restaurant_scores[restaurant] = score
    
    log_file.close()
    return restaurant_scores


def print_ordered_scores(restaurant_scores):
    """Takes a dictionary of restaurant_scores and prints them in a readable format"""

    restaurant_scores = restaurant_scores.items()
    restaurant_scores.sort()

    # Prints restaurant name and score in sentence format.
    for restaurant, score in restaurant_scores:
        print "%s is rated at %s." % (restaurant, score)

    pass


def add_restaurant(restaurant_scores):
    """Prompts user for the name & score of new restaurant and adds it the dictionary.

       restaurant_scores: Dictionary of restaurants and their scores.
    """
    new_restaurant = raw_input("What is the name of the restaurant you'd like to add? - ")
    new_score = raw_input("What is the score for %s? - " % (new_restaurant))
    restaurant_scores[new_restaurant] = new_score
    return restaurant_scores


def random_update(restaurant_scores):
    """Provides user with a random restaurant and prompts them to update the score.

       restaurant_scores: Dictionary of restaurants and their scores.
    """
    restaurant_names = restaurant_scores.keys()
    random_index = randint(0,(len(restaurant_names)-1))
    update_name = restaurant_names[random_index]
    update_score = raw_input("What is your new score for %s? - " % (update_name))
    restaurant_scores[update_name] = update_score
    print "Great, the new score for %s is %s" % (update_name, update_score)
    return restaurant_scores


# Prompts user for user name and builds dictionary from opened file.
user_name = raw_input("Hello! What is your name? - ")
restaurant_scores = build_restaurant_dict(filename)

# Prompts user for choice and executes actions dependent upon choice until they exit.
while True:
    print "\n"
    print "What would you like to do?"
    print "1 - Add a new restaurant and rating."
    print "2 - Update an existing restaurant and rating at random."
    print "3 - Print existing restaurants and ratings."
    print "q - Exit program."
    print "\n"
    choice = raw_input("What would you like to do? Choose 1, 2, 3, or 4. - ")

    if choice == "1":
        print "\n"
        restaurant_scores = add_restaurant(restaurant_scores)
    elif choice == "2":
        print "\n"
        restaurant_scores = random_update(restaurant_scores)
    elif choice == "3":
        print "\n"
        print_ordered_scores(restaurant_scores)
    elif choice == "q":
        print "\n"
        print "Thank you for using our program. The final scores are:"
        print_ordered_scores(restaurant_scores)
        break
    else:
        print "\n"
        print "That's not a valid choice, try again."


# Expects user to pass filename as the second part of their python command.


#print_restaurant_scores(filename)
