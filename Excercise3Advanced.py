dictionary = {
    "first_name": input('What is your first name?'),
    "second_name": input('What is your second name?'),
    "age": int(input('What is your age?')),
    "hometown": input('Where is your hometown located in?'),
} #For the variables I've created a dictionary so that I wouldnt be hardcoding in all of the transcripts. It acts as one folder for the variables.

for key, value in dictionary.items():
    print(value) 
    # I've created a loop that would gather the values of the variables presented in the dictionary and be able to display them without clutter.

"""
I went with my peers to conspire a way to be able to enhance the visuals (eg.) Making the lines shorter
And Found the way which was to add loops so the code wouldn't be cluttered and so it could run all of the data and variables
in one orderly transcript.
"""


 
