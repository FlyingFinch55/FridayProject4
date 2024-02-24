# Mad Lib Program - Creating a madlib story using user inputs

# User inputs
large_object = input("Enter the name of a large object: ")
plural_large_object = input("Enter a different big object (plural): ")
adjective = input("Enter an adjective: ")
body_part = input("Enter the name of a body part: ")
restaurant = input("Enter the name of a restaurant: ")
food_item_1 = input("Enter the name of a food item: ")
food_item_2 = input("Enter the name of a different food item: ")

# Madlib story
madlib_story = f"I've had a {adjective} day. This morning I dropped a box of {plural_large_object} on my {body_part}. " \
               f"Then at lunch, I went to {restaurant} for their delicious {food_item_1}, but the waiter brought me {food_item_2} " \
               f"which I was not hungry for. Finally, on my way home, I was cut off by a van with a {large_object} strapped to the roof."
